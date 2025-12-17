#!/usr/bin/env python3
"""
Create calculation holder and comprehensive group summaries.

Reads `Cleaned_data.csv` in repository root, computes aggregate metrics for
Severity, Pure Premium and claims frequency, writes an empty/filled
calculations holder and per-group summaries into `pricing_final_outputs/`.

Usage:
    python scripts/create_calculations_and_summaries.py 
    python scripts/create_calculations_and_summaries.py --input path/to/Cleaned_data.csv \
        --groups Veh_value Gender Area

"""
from __future__ import annotations
import argparse
import os
import sys
from typing import List

import pandas as pd


def normalize_colname(name: str) -> str:
    return ''.join(ch.lower() for ch in name if ch.isalnum())


def find_columns(df: pd.DataFrame, desired: List[str]) -> List[str]:
    # Map normalized name -> actual name
    norm_map = {normalize_colname(c): c for c in df.columns}
    found = []
    for d in desired:
        key = normalize_colname(d)
        if key in norm_map:
            found.append(norm_map[key])
    return found


def ensure_output_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def write_calculation_holder(df: pd.DataFrame, metrics: List[str], out_csv: str) -> None:
    rows = []
    for m in metrics:
        series = pd.to_numeric(df[m], errors='coerce')
        rows.append({
            'metric': m,
            'total': float(series.sum(skipna=True)),
            'mean': float(series.mean(skipna=True)),
            'min': float(series.min(skipna=True)),
            'max': float(series.max(skipna=True)),
            'count': int(series.count()),
        })
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_csv, index=False)


def build_group_summaries(df: pd.DataFrame, groups: List[str], metrics: List[str], out_dir: str) -> List[str]:
    saved_files = []
    extra_numeric = find_columns(df, ['Exposure', 'Claims_cost', 'Number_of_recorded_claims'])
    for g in groups:
        if g not in df.columns:
            continue
        agg_cols = metrics + extra_numeric
        # Keep only present columns
        agg_cols = [c for c in agg_cols if c in df.columns]
        if not agg_cols:
            continue
        grouped = df.groupby(g)[agg_cols].agg(['sum', 'mean', 'min', 'max', 'count'])
        # flatten columns
        grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
        grouped = grouped.reset_index()
        out_path = os.path.join(out_dir, f'summary_{g}.csv')
        grouped.to_csv(out_path, index=False)
        saved_files.append(out_path)
    return saved_files


def build_comprehensive_summary(saved_files: List[str], out_csv: str) -> None:
    parts = []
    for f in saved_files:
        tmp = pd.read_csv(f)
        # infer group column name from filename
        basename = os.path.basename(f)
        grp = basename.replace('summary_', '').replace('.csv', '')
        tmp.insert(0, 'group_col', grp)
        # rename first column to group_value if not already
        if tmp.shape[1] > 1:
            # assume the second column is the group value (original index)
            cols = list(tmp.columns)
            cols[1] = 'group_value'
            tmp.columns = cols
        parts.append(tmp)
    if parts:
        pd.concat(parts, ignore_index=True).to_csv(out_csv, index=False)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input', '-i', default='Cleaned_data.csv', help='Path to cleaned CSV')
    p.add_argument('--outdir', '-o', default='pricing_final_outputs', help='Directory to save outputs')
    p.add_argument('--groups', '-g', nargs='*', help='Group columns to summarize (optional)')
    return p.parse_args()


def main():
    args = parse_args()
    if not os.path.exists(args.input):
        print(f"Input file not found: {args.input}")
        sys.exit(2)

    df = pd.read_csv(args.input)

    # detect metric columns robustly
    desired_metrics = ['Severity', 'Pure_Premium', 'claims_Frequency', 'Pure_premium', 'Pure premium']
    metrics = find_columns(df, desired_metrics)
    # normalize to the canonical names used in output
    if not metrics:
        print('No target metric columns found in input. Expected one of: ' + ','.join(desired_metrics))
        sys.exit(3)

    ensure_output_dir(args.outdir)

    calc_holder_path = os.path.join(args.outdir, 'calculation_holder.csv')
    write_calculation_holder(df, metrics, calc_holder_path)

    # prepare group list
    if args.groups and len(args.groups) > 0:
        groups = [g for g in args.groups if g in df.columns]
    else:
        # default groups commonly present in dataset
        default_groups = ['Veh_value', 'Veh_body', 'Veh_age', 'Gender', 'Area', 'Age_category', 'Veh_value_categories', 'Claims_cost_categories']
        groups = [g for g in default_groups if g in df.columns]

    saved = build_group_summaries(df, groups, metrics, args.outdir)

    comprehensive_path = os.path.join(args.outdir, 'comprehensive_group_summary.csv')
    build_comprehensive_summary(saved, comprehensive_path)

    print('Wrote:')
    print(' -', calc_holder_path)
    for f in saved:
        print(' -', f)
    print(' -', comprehensive_path)


if __name__ == '__main__':
    main()
