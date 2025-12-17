#!/usr/bin/env python3
"""
Generate Power BI model documentation (Markdown) by scanning CSV tables in the repository.

Output: `docs/powerbi_model_documentation.md`

The script lists all tables (CSV files), their columns and inferred types, simple statistics,
and a Measures section with suggested DAX for calculated metrics commonly used in this project.
"""
from __future__ import annotations
import os
import glob
import textwrap
from typing import List

import pandas as pd


ROOT = os.path.abspath(os.path.dirname(__file__) + os.sep + '..')
OUT_DIR = os.path.join(ROOT, 'docs')
os.makedirs(OUT_DIR, exist_ok=True)


def find_csv_files(root: str) -> List[str]:
    patterns = [os.path.join(root, '*.csv'), os.path.join(root, 'DataSet', '*.csv'), os.path.join(root, 'pricing_final_outputs', '*.csv')]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    # de-duplicate and sort
    files = sorted(list(dict.fromkeys(files)))
    return files


def summarize_table(path: str) -> str:
    df = pd.read_csv(path)
    name = os.path.basename(path)
    md = [f"### Table: `{name}`", '']
    md.append('| Column | Inferred Type | Non-null Count | Unique | Sample Values |')
    md.append('|---|---:|---:|---:|---|')
    for c in df.columns:
        ser = df[c]
        dtype = str(ser.dtype)
        non_null = int(ser.count())
        try:
            unique = int(ser.nunique(dropna=True))
        except Exception:
            unique = 'N/A'
        sample = ', '.join(map(str, ser.dropna().unique()[:5]))
        sample = (sample[:80] + '...') if len(sample) > 80 else sample
        md.append(f'| `{c}` | `{dtype}` | {non_null} | {unique} | {sample} |')
    md.append('')
    # small summary stats for numeric cols
    num = df.select_dtypes(include=['number'])
    if not num.empty:
        md.append('**Numeric columns summary (mean/min/max)**')
        md.append('')
        md.append('| Column | Mean | Min | Max |')
        md.append('|---|---:|---:|---:|')
        for c in num.columns:
            md.append(f'| `{c}` | {num[c].mean():.4f} | {num[c].min():.4f} | {num[c].max():.4f} |')
        md.append('')
    return '\n'.join(md)


def detect_measures(file_paths: List[str]) -> List[str]:
    # Look through CSVs for common calculated metric columns
    measure_names = set()
    targets = ['Severity', 'severity', 'Pure_Premium', 'Pure_premium', 'Pure premium', 'claims_Frequency', 'claims_frequency', 'actual_claims_relativity', 'actual_claims_relativity']
    for p in file_paths:
        try:
            df = pd.read_csv(p)
        except Exception:
            continue
        cols = [c for c in df.columns]
        for t in targets:
            for c in cols:
                if ''.join(ch.lower() for ch in c if ch.isalnum()).find(''.join(ch.lower() for ch in t if ch.isalnum())) >= 0:
                    measure_names.add(c)
    return sorted(measure_names)


def write_documentation(out_path: str):
    csvs = find_csv_files(ROOT)
    lines = []
    lines.append('# Power BI Model Documentation')
    lines.append('')
    lines.append('This document was generated automatically by `scripts/generate_powerbi_documentation.py`. It lists tables (CSV files found in the repository), their columns and basic statistics, and a suggested Measures section with common DAX expressions used in the project.')
    lines.append('')

    if not csvs:
        lines.append('_No CSV tables were found in the repository._')
    else:
        lines.append('## Tables')
        lines.append('')
        for p in csvs:
            lines.append(summarize_table(p))

    # Measures (inferred)
    measures = detect_measures(csvs)
    lines.append('')
    lines.append('## Measures (Detected / Suggested)')
    lines.append('')
    if measures:
        lines.append('The script detected the following measure-like columns in dataset files:')
        lines.append('')
        for m in measures:
            lines.append(f'- `{m}`')
    else:
        lines.append('_No calculated measures detected automatically._')

    lines.append('')
    lines.append('### Suggested DAX formulas')
    lines.append("These DAX expressions are suggested based on the project's existing calculations (also present in the project notebook).")
    lines.append('Adjust field names to match your model when creating measures in Power BI:')
    lines.append('')
    dax_snippets = {
        'Severity': 'Severity = IF([Number_of_recorded_claims] <> 0, [Claims_cost] / [Number_of_recorded_claims], 0)',
        'Claims Frequency': 'Claims_Frequency = DIVIDE([Number_of_recorded_claims], [Exposure], 0)',
        'Pure Premium': 'Pure_Premium = [Severity] * [Claims_Frequency]',
        'Overall Pure Premium': 'Overall_Pure_Premium = DIVIDE(SUM([Claims_cost]), SUM([Exposure]), 0)',
        'Actual Claims Relativity': 'Actual_Claims_Relativity = DIVIDE([Pure_Premium], [Overall_Pure_Premium], 0)'
    }
    for k, v in dax_snippets.items():
        lines.append(f'**{k}**:')
        lines.append('')
        lines.append('```dax')
        lines.append(v)
        lines.append('```')
        lines.append('')

    # Additional documentation sections
    lines.append('## Recommended documentation to add (manual)')
    lines.append('')
    lines.append(textwrap.dedent('''
    - Business descriptions for each table and column (what the field means, units, cardinality).
    - Grain of the table (row-level meaning, e.g., policy-period, transaction-level).
    - Data source and refresh schedule.
    - Keys and relationships (primary/foreign keys) between tables.
    - Any transformations applied in Power Query or ETL steps.
    - Calculation logic and validation notes for measures.
    - Data quality notes and known issues.
    - Owner/Contact for each table/measure.
    '''))

    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))


if __name__ == '__main__':
    out_path = os.path.join(OUT_DIR, 'powerbi_model_documentation.md')
    write_documentation(out_path)
    print('Wrote', out_path)
