# Power BI Model Documentation

This document was generated automatically by `scripts/generate_powerbi_documentation.py`. It lists tables (CSV files found in the repository), their columns and basic statistics, and a suggested Measures section with common DAX expressions used in the project.

## Tables

### Table: `Cleaned_data.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Unnamed: 0` | `int64` | 67340 | 67340 | 0, 1, 2, 3, 4 |
| `Veh_value` | `float64` | 67340 | 985 | 10600.0, 10300.0, 32600.0, 41400.0, 7200.0 |
| `Exposure` | `float64` | 67340 | 367 | 0.303901437, 0.648870637, 0.569472964, 0.317590691, 0.854209446 |
| `Claim_recorded` | `int64` | 67340 | 2 | 0, 1 |
| `Number_of_recorded_claims` | `int64` | 67340 | 5 | 0, 1, 2, 3, 4 |
| `Claims_cost` | `float64` | 67340 | 3165 | 0.0, 669.5099993, 806.6099987, 401.8054514, 1811.709997 |
| `Veh_body` | `object` | 67340 | 13 | HBACK, UTE, STNWG, HDTOP, PANVN |
| `Veh_age` | `int64` | 67340 | 4 | 3, 2, 4, 1 |
| `Gender` | `object` | 67340 | 2 | F, M |
| `Area` | `object` | 67340 | 6 | C, A, E, D, B |
| `Age_category` | `int64` | 67340 | 6 | 2, 4, 6, 3, 5 |
| `Claims_cost_categories` | `object` | 67340 | 5 | Claims_cost 0, Claims_cost 1-10k, Claims_cost 10k-20k, Claims_cost 20k-30k, Clai... |
| `Veh_value_categories` | `object` | 67340 | 4 | Veh_value up to 100k, Veh_value between 100k and 200k, Veh_value between 200k an... |
| `Severity` | `float64` | 67340 | 2136 | 0.0, 670.0, 807.0, 402.0, 906.0 |
| `claims_Frequency` | `float64` | 67340 | 503 | 0.0, 2.06355932340669, 1.0061983468330202, 1.8540609139291064, 3.056485356230419 |
| `Pure_Premium` | `float64` | 67340 | 2878 | 0.0, 1383.0, 812.0, 745.0, 2769.0 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Unnamed: 0` | 33877.8621 | 0.0000 | 67855.0000 |
| `Veh_value` | 17795.1743 | 1800.0000 | 345600.0000 |
| `Exposure` | 0.4676 | 0.0027 | 0.9993 |
| `Claim_recorded` | 0.0673 | 0.0000 | 1.0000 |
| `Number_of_recorded_claims` | 0.0719 | 0.0000 | 4.0000 |
| `Claims_cost` | 120.0033 | 0.0000 | 36502.1398 |
| `Veh_age` | 2.6725 | 1.0000 | 4.0000 |
| `Age_category` | 3.4851 | 1.0000 | 6.0000 |
| `Severity` | 113.5673 | 0.0000 | 36502.0000 |
| `claims_Frequency` | 0.2016 | 0.0000 | 365.2500 |
| `Pure_Premium` | 556.3127 | 0.0000 | 3142976.0000 |

### Table: `Cross_Validation_Results.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `resampler` | `object` | 25 | 5 | EditedNearestNeighbours_under_sampling, ADASYN_over_sampling, SMOTE_over_samplin... |
| `model` | `object` | 25 | 5 | XGBClassifier, GradientBoostingClassifier, BaggingClassifier, RandomForestClassi... |
| `test_f1` | `float64` | 25 | 25 | 0.5013390714180943, 0.4985423861646199, 0.4947138586710209, 0.4883928180365386, ... |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `test_f1` | 0.4491 | 0.3840 | 0.5013 |

### Table: `data_car.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `veh_value` | `float64` | 67856 | 986 | 1.06, 1.03, 3.26, 4.14, 0.72 |
| `exposure` | `float64` | 67856 | 367 | 0.303901437, 0.648870637, 0.569472964, 0.317590691, 0.854209446 |
| `clm` | `int64` | 67856 | 2 | 0, 1 |
| `numclaims` | `int64` | 67856 | 5 | 0, 1, 2, 3, 4 |
| `claimcst0` | `float64` | 67856 | 3257 | 0.0, 669.5099993, 806.6099987, 401.8054514, 1811.709997 |
| `veh_body` | `object` | 67856 | 13 | HBACK, UTE, STNWG, HDTOP, PANVN |
| `veh_age` | `int64` | 67856 | 4 | 3, 2, 4, 1 |
| `gender` | `object` | 67856 | 2 | F, M |
| `area` | `object` | 67856 | 6 | C, A, E, D, B |
| `agecat` | `int64` | 67856 | 6 | 2, 4, 6, 3, 5 |
| `X_OBSTAT_` | `object` | 67856 | 1 | 01101    0    0    0 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `veh_value` | 1.7770 | 0.0000 | 34.5600 |
| `exposure` | 0.4687 | 0.0027 | 0.9993 |
| `clm` | 0.0681 | 0.0000 | 1.0000 |
| `numclaims` | 0.0728 | 0.0000 | 4.0000 |
| `claimcst0` | 137.2702 | 0.0000 | 55922.1299 |
| `veh_age` | 2.6735 | 1.0000 | 4.0000 |
| `agecat` | 3.4855 | 1.0000 | 6.0000 |

### Table: `new_cleaned_df.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Unnamed: 0` | `int64` | 67795 | 67795 | 0, 1, 2, 3, 4 |
| `veh_value` | `int64` | 67795 | 985 | 10600, 10300, 32600, 41400, 7200 |
| `exposure` | `float64` | 67795 | 367 | 0.303901437, 0.648870637, 0.569472964, 0.317590691, 0.854209446 |
| `clm` | `int64` | 67795 | 2 | 0, 1 |
| `numclaims` | `int64` | 67795 | 5 | 0, 1, 2, 3, 4 |
| `claimcst0` | `float64` | 67795 | 3243 | 0.0, 669.5099993, 806.6099987, 401.8054514, 1811.709997 |
| `veh_body` | `object` | 67795 | 13 | HBACK, UTE, STNWG, HDTOP, PANVN |
| `veh_age` | `int64` | 67795 | 4 | 3, 2, 4, 1 |
| `gender` | `object` | 67795 | 2 | F, M |
| `area` | `object` | 67795 | 6 | C, A, E, D, B |
| `agecat` | `int64` | 67795 | 6 | 2, 4, 6, 3, 5 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Unnamed: 0` | 33926.8694 | 0.0000 | 67855.0000 |
| `veh_value` | 17781.9387 | 1800.0000 | 345600.0000 |
| `exposure` | 0.4685 | 0.0027 | 0.9993 |
| `clm` | 0.0680 | 0.0000 | 1.0000 |
| `numclaims` | 0.0726 | 0.0000 | 4.0000 |
| `claimcst0` | 132.4466 | 0.0000 | 31243.6699 |
| `veh_age` | 2.6729 | 1.0000 | 4.0000 |
| `agecat` | 3.4856 | 1.0000 | 6.0000 |

### Table: `actual_relativity_table.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Unnamed: 0` | `int64` | 47 | 47 | 0, 1, 2, 3, 4 |
| `factor` | `object` | 47 | 9 | Claim_recorded, Number_of_recorded_claims, Veh_body, Veh_age, Gender |
| `group` | `object` | 47 | 36 | 0, 1, 2, 3, 4 |
| `exposure` | `float64` | 47 | 45 | 28701.563315481, 2784.917180154, 2581.379876931, 189.032169753, 12.736481861 |
| `claims` | `int64` | 47 | 41 | 0, 4532, 4245, 267, 18 |
| `claim_cost` | `float64` | 47 | 43 | 0.0, 8081019.1783297, 7242587.3213131, 757121.5134896, 72432.383533 |
| `frequency` | `float64` | 47 | 43 | 0.0, 1.6273374419520044, 1.6444693157858177, 1.412457997751796, 1.41326311272167... |
| `severity` | `float64` | 47 | 43 | 0.0, 1783.102201749713, 1706.1454231597409, 2835.661099211985, 4024.021307388889 |
| `pure_premium` | `float64` | 47 | 43 | 0.0, 2901.7089757343647, 2805.703796654604, 4005.252198495617, 5687.000878538762 |
| `actual_claims_relativity` | `float64` | 47 | 43 | 0.0, 11.306074277545967, 10.932004481166688, 15.605865107487332, 22.158546872522... |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Unnamed: 0` | 23.0000 | 0.0000 | 46.0000 |
| `exposure` | 6029.3261 | 0.7748 | 31453.9548 |
| `claims` | 867.8298 | 0.0000 | 4532.0000 |
| `claim_cost` | 1547429.2044 | 0.0000 | 8081019.1783 |
| `frequency` | 0.4969 | 0.0000 | 5.1625 |
| `severity` | 3162.0663 | 0.0000 | 33788.7574 |
| `pure_premium` | 6069.4673 | 0.0000 | 174435.9526 |
| `actual_claims_relativity` | 23.6488 | 0.0000 | 679.6636 |

### Table: `calculation_holder.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `metric` | `object` | 5 | 3 | Severity, Pure_Premium, claims_Frequency |
| `total` | `float64` | 5 | 3 | 7647624.0, 37462095.0, 13578.41022660874 |
| `mean` | `float64` | 5 | 3 | 113.56732996732995, 556.3126670626671, 0.2016395935047333 |
| `min` | `float64` | 5 | 1 | 0.0 |
| `max` | `float64` | 5 | 3 | 36502.0, 3142976.0, 365.2499716018147 |
| `count` | `int64` | 5 | 1 | 67340 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `total` | 24009497.4820 | 13578.4102 | 37462095.0000 |
| `mean` | 356.5414 | 0.2016 | 556.3127 |
| `min` | 0.0000 | 0.0000 | 0.0000 |
| `max` | 1893159.0500 | 365.2500 | 3142976.0000 |
| `count` | 67340.0000 | 67340.0000 | 67340.0000 |

### Table: `comprehensive_group_summary.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `group_col` | `object` | 1025 | 8 | Veh_value, Veh_body, Veh_age, Gender, Area |
| `group_value` | `object` | 1025 | 1020 | 1800.0, 1900.0, 2000.0, 2100.0, 2200.0 |
| `Severity_sum` | `float64` | 1025 | 542 | 0.0, 2882.0, 200.0, 1951.0, 2073.0 |
| `Severity_mean` | `float64` | 1025 | 572 | 0.0, 64.04444444444445, 8.0, 60.96875, 2.1739130434782608 |
| `Severity_min` | `float64` | 1025 | 15 | 0.0, 633.0, 1317.0, 672.0, 383.0 |
| `Severity_max` | `float64` | 1025 | 497 | 0.0, 1458.0, 200.0, 1951.0, 1873.0 |
| `Severity_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum` | `float64` | 1025 | 579 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean` | `float64` | 1025 | 583 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min` | `float64` | 1025 | 15 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max` | `float64` | 1025 | 542 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `claims_Frequency_sum` | `float64` | 1025 | 560 | 0.0, 6.904575355368477, 1.0838278934846244, 3.652499996174007, 5.217857145559248 |
| `claims_Frequency_mean` | `float64` | 1025 | 583 | 0.0, 0.1534350078970772, 0.0433531157393849, 0.1141406248804377, 0.0567158385386... |
| `claims_Frequency_min` | `float64` | 1025 | 13 | 0.0, 1.0006849318104818, 1.03470254942265, 2.2136363630326445, 1.503086420370094 |
| `claims_Frequency_max` | `float64` | 1025 | 273 | 0.0, 2.5541958013245667, 1.0838278934846244, 3.652499996174007, 5.21785714555924... |
| `claims_Frequency_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum.1` | `float64` | 1025 | 579 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean.1` | `float64` | 1025 | 583 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min.1` | `float64` | 1025 | 15 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max.1` | `float64` | 1025 | 542 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count.1` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum.2` | `float64` | 1025 | 579 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean.2` | `float64` | 1025 | 583 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min.2` | `float64` | 1025 | 15 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max.2` | `float64` | 1025 | 542 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count.2` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Exposure_sum` | `float64` | 1025 | 935 | 2.135523615, 9.0403833, 1.237508557, 1.754962354, 27.753593429 |
| `Exposure_mean` | `float64` | 1025 | 957 | 0.266940451875, 0.6954141, 0.2475017114, 0.3509924707999999, 0.6167465206444445 |
| `Exposure_min` | `float64` | 1025 | 219 | 0.049281314, 0.314852841, 0.030116359, 0.062970568, 0.052019165 |
| `Exposure_max` | `float64` | 1025 | 268 | 0.462696783, 0.895277207, 0.459958932, 0.862422998, 0.999315537 |
| `Exposure_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Claims_cost_sum` | `float64` | 1025 | 555 | 0.0, 3586.6354535, 200.0, 1951.039997, 2072.809998 |
| `Claims_cost_mean` | `float64` | 1025 | 577 | 0.0, 79.70301007777778, 8.0, 60.96999990625, 2.1739130434782608 |
| `Claims_cost_min` | `float64` | 1025 | 15 | 0.0, 633.3499994, 1317.439999, 672.1799994, 383.3199997 |
| `Claims_cost_max` | `float64` | 1025 | 516 | 0.0, 1457.959999, 200.0, 1951.039997, 1872.809998 |
| `Claims_cost_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |
| `Number_of_recorded_claims_sum` | `int64` | 1025 | 70 | 0, 5, 1, 2, 9 |
| `Number_of_recorded_claims_mean` | `float64` | 1025 | 368 | 0.0, 0.1111111111111111, 0.04, 0.03125, 0.0108695652173913 |
| `Number_of_recorded_claims_min` | `int64` | 1025 | 2 | 0, 1 |
| `Number_of_recorded_claims_max` | `int64` | 1025 | 5 | 0, 2, 1, 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 1025 | 283 | 8, 13, 5, 45, 25 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 59688.7727 | 0.0000 | 7632803.0000 |
| `Severity_mean` | 194.9250 | 0.0000 | 33788.7500 |
| `Severity_min` | 78.1220 | 0.0000 | 32196.0000 |
| `Severity_max` | 3596.7522 | 0.0000 | 36502.0000 |
| `Severity_count` | 525.5805 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum` | 292387.0829 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean` | 988.2625 | 0.0000 | 231389.5000 |
| `Pure_Premium_min` | 167.3902 | 0.0000 | 103325.0000 |
| `Pure_Premium_max` | 76740.7717 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count` | 525.5805 | 1.0000 | 67263.0000 |
| `claims_Frequency_sum` | 105.9778 | 0.0000 | 13570.8193 |
| `claims_Frequency_mean` | 0.1946 | 0.0000 | 9.8399 |
| `claims_Frequency_min` | 0.0235 | 0.0000 | 4.3482 |
| `claims_Frequency_max` | 10.4174 | 0.0000 | 365.2500 |
| `claims_Frequency_count` | 525.5805 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum.1` | 292387.0829 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean.1` | 988.2625 | 0.0000 | 231389.5000 |
| `Pure_Premium_min.1` | 167.3902 | 0.0000 | 103325.0000 |
| `Pure_Premium_max.1` | 76740.7717 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 525.5805 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum.2` | 292387.0829 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean.2` | 988.2625 | 0.0000 | 231389.5000 |
| `Pure_Premium_min.2` | 167.3902 | 0.0000 | 103325.0000 |
| `Pure_Premium_max.2` | 76740.7717 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 525.5805 | 1.0000 | 67263.0000 |
| `Exposure_sum` | 245.7481 | 0.0027 | 31453.9548 |
| `Exposure_mean` | 0.4556 | 0.0027 | 0.9993 |
| `Exposure_min` | 0.1609 | 0.0027 | 0.9993 |
| `Exposure_max` | 0.7734 | 0.0027 | 0.9993 |
| `Exposure_count` | 525.5805 | 1.0000 | 67263.0000 |
| `Claims_cost_sum` | 63071.3692 | 0.0000 | 8066199.5083 |
| `Claims_cost_mean` | 201.1334 | 0.0000 | 33788.7574 |
| `Claims_cost_min` | 84.4682 | 0.0000 | 32195.8200 |
| `Claims_cost_max` | 3719.5303 | 0.0000 | 36502.1398 |
| `Claims_cost_count` | 525.5805 | 1.0000 | 67263.0000 |
| `Number_of_recorded_claims_sum` | 37.7834 | 0.0000 | 4838.0000 |
| `Number_of_recorded_claims_mean` | 0.0757 | 0.0000 | 1.1744 |
| `Number_of_recorded_claims_min` | 0.0146 | 0.0000 | 1.0000 |
| `Number_of_recorded_claims_max` | 0.8361 | 0.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 525.5805 | 1.0000 | 67263.0000 |

### Table: `cred_relativities.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Area` | `object` | 6 | 6 | A, B, C, D, E |
| `exposure` | `float64` | 6 | 6 | 7521.670089646, 6237.434634382, 9474.039699684, 3782.899384291, 2748.843258319 |
| `claims` | `int64` | 6 | 6 | 1065, 947, 1380, 485, 380 |
| `claim_cost` | `float64` | 6 | 6 | 1741136.7137376, 1633560.834005, 2479817.237914, 767178.3305317, 784288.3105851 |
| `frequency` | `float64` | 6 | 6 | 0.1415908950149292, 0.1518252383407667, 0.1456612008968074, 0.1282085381424702, ... |
| `severity` | `float64` | 6 | 6 | 1634.8701537442253, 1724.985041187962, 1796.9690129811595, 1581.8109907870105, 2... |
| `pure_premium` | `float64` | 6 | 6 | 231.48272830183976, 261.8962650126196, 261.7486644051864, 202.8016747464951, 285... |
| `actual_claims_relativity` | `float64` | 6 | 6 | 0.901937769099412, 1.020439558207303, 1.0198644545545912, 0.7901863410386657, 1.... |
| `Z` | `float64` | 6 | 6 | 0.974098867514661, 0.968931723371324, 0.9793261133705568, 0.9497853245329716, 0.... |
| `pp_shrunk` | `float64` | 6 | 6 | 232.13460062332132, 261.7332863736599, 261.64326436081296, 205.50567318557148, 2... |
| `rel_shrunk` | `float64` | 6 | 6 | 0.9044776919337764, 1.019804536358751, 1.019453779073174, 0.8007220658319589, 1.... |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `exposure` | 5247.7467 | 1721.5934 | 9474.0397 |
| `claims` | 755.3333 | 275.0000 | 1380.0000 |
| `claim_cost` | 1346836.5297 | 675037.7516 | 2479817.2379 |
| `frequency` | 0.1442 | 0.1282 | 0.1597 |
| `severity` | 1876.2058 | 1581.8110 | 2454.6827 |
| `pure_premium` | 272.5576 | 202.8017 | 392.1006 |
| `actual_claims_relativity` | 1.0620 | 0.7902 | 1.5278 |
| `Z` | 0.9500 | 0.8959 | 0.9793 |
| `pp_shrunk` | 270.3985 | 205.5057 | 378.0029 |
| `rel_shrunk` | 1.0536 | 0.8007 | 1.4728 |

### Table: `final_tariff_table.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `factor` | `object` | 35 | 6 | Veh_body, Gender, Area, Age_category, Veh_value_categories |
| `level` | `object` | 35 | 30 | BUS, CONVT, COUPE, HBACK, HDTOP |
| `relativity` | `float64` | 35 | 30 | 1.0, 0.980102703858801, 1.2649868809928584, 0.9768406830620808, 1.00660772050611... |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `relativity` | 0.9883 | 0.6246 | 1.3165 |

### Table: `summary_Age_category.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Age_category` | `int64` | 6 | 6 | 1, 2, 3, 4, 5 |
| `Severity_sum` | `float64` | 6 | 6 | 1123764.0, 1609460.0, 1744703.0, 1749292.0, 889124.0 |
| `Severity_mean` | `float64` | 6 | 6 | 197.2207792207792, 125.7488866317681, 111.53250655245158, 109.03771115128092, 83... |
| `Severity_min` | `float64` | 6 | 1 | 0.0 |
| `Severity_max` | `float64` | 6 | 6 | 32815.0, 36502.0, 21669.0, 32196.0, 21491.0 |
| `Severity_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Pure_Premium_sum` | `float64` | 6 | 6 | 10074752.0, 4776069.0, 9608363.0, 5065268.0, 5797539.0 |
| `Pure_Premium_mean` | `float64` | 6 | 6 | 1768.120744120744, 373.1595437143527, 614.2276417566962, 315.7307236801097, 544.... |
| `Pure_Premium_min` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 6 | 6 | 3142976.0, 476156.0, 2978066.0, 168928.0, 2523695.0 |
| `Pure_Premium_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `claims_Frequency_sum` | `float64` | 6 | 6 | 2058.374209865449, 2539.6070632536725, 3091.933676796172, 3080.06344307009, 1841... |
| `claims_Frequency_mean` | `float64` | 6 | 6 | 0.3612450350764213, 0.1984223035591587, 0.197656055538974, 0.1919879974487371, 0... |
| `claims_Frequency_min` | `float64` | 6 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 6 | 3 | 365.2499716018147, 182.62498580090733, 60.87499897273439 |
| `claims_Frequency_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Pure_Premium_sum.1` | `float64` | 6 | 6 | 10074752.0, 4776069.0, 9608363.0, 5065268.0, 5797539.0 |
| `Pure_Premium_mean.1` | `float64` | 6 | 6 | 1768.120744120744, 373.1595437143527, 614.2276417566962, 315.7307236801097, 544.... |
| `Pure_Premium_min.1` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 6 | 6 | 3142976.0, 476156.0, 2978066.0, 168928.0, 2523695.0 |
| `Pure_Premium_count.1` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Pure_Premium_sum.2` | `float64` | 6 | 6 | 10074752.0, 4776069.0, 9608363.0, 5065268.0, 5797539.0 |
| `Pure_Premium_mean.2` | `float64` | 6 | 6 | 1768.120744120744, 373.1595437143527, 614.2276417566962, 315.7307236801097, 544.... |
| `Pure_Premium_min.2` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 6 | 6 | 3142976.0, 476156.0, 2978066.0, 168928.0, 2523695.0 |
| `Pure_Premium_count.2` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Exposure_sum` | `float64` | 6 | 6 | 2589.552361654, 5846.9541416, 7330.176592014, 7529.746749434, 5119.277207846 |
| `Exposure_mean` | `float64` | 6 | 6 | 0.4544668939371709, 0.4568289820767247, 0.4685914844987534, 0.4693477996281244, ... |
| `Exposure_min` | `float64` | 6 | 1 | 0.002737851 |
| `Exposure_max` | `float64` | 6 | 1 | 0.999315537 |
| `Exposure_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Claims_cost_sum` | `float64` | 6 | 6 | 1183928.7087046, 1700495.9019402, 1857490.4622494, 1853632.0426309, 928514.25402... |
| `Claims_cost_mean` | `float64` | 6 | 6 | 207.77969615735347, 132.86162215330884, 118.7425981109378, 115.5414849236988, 87... |
| `Claims_cost_min` | `float64` | 6 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 6 | 6 | 32814.79993, 36502.13977, 21669.07996, 32195.81995, 21491.38995 |
| `Claims_cost_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |
| `Number_of_recorded_claims_sum` | `int64` | 6 | 6 | 515, 982, 1161, 1165, 637 |
| `Number_of_recorded_claims_mean` | `float64` | 6 | 6 | 0.0903825903825903, 0.0767247441206344, 0.0742185002876686, 0.072617340896341, 0... |
| `Number_of_recorded_claims_min` | `int64` | 6 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 6 | 2 | 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 6 | 6 | 5698, 12799, 15643, 16043, 10655 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Age_category` | 3.5000 | 1.0000 | 6.0000 |
| `Severity_sum` | 1274604.0000 | 531281.0000 | 1749292.0000 |
| `Severity_mean` | 118.1162 | 81.7104 | 197.2208 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 26830.6667 | 16311.0000 | 36502.0000 |
| `Severity_count` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Pure_Premium_sum` | 6243682.5000 | 2140104.0000 | 10074752.0000 |
| `Pure_Premium_mean` | 657.4164 | 315.7307 | 1768.1207 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 1626882.0000 | 168928.0000 | 3142976.0000 |
| `Pure_Premium_count` | 11223.3333 | 5698.0000 | 16043.0000 |
| `claims_Frequency_sum` | 2263.0684 | 967.0258 | 3091.9337 |
| `claims_Frequency_mean` | 0.2118 | 0.1487 | 0.3612 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 192.7708 | 60.8750 | 365.2500 |
| `claims_Frequency_count` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Pure_Premium_sum.1` | 6243682.5000 | 2140104.0000 | 10074752.0000 |
| `Pure_Premium_mean.1` | 657.4164 | 315.7307 | 1768.1207 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 1626882.0000 | 168928.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Pure_Premium_sum.2` | 6243682.5000 | 2140104.0000 | 10074752.0000 |
| `Pure_Premium_mean.2` | 657.4164 | 315.7307 | 1768.1207 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 1626882.0000 | 168928.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Exposure_sum` | 5247.7467 | 2589.5524 | 7529.7467 |
| `Exposure_mean` | 0.4670 | 0.4545 | 0.4805 |
| `Exposure_min` | 0.0027 | 0.0027 | 0.0027 |
| `Exposure_max` | 0.9993 | 0.9993 | 0.9993 |
| `Exposure_count` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Claims_cost_sum` | 1346836.5297 | 556957.8088 | 1857490.4622 |
| `Claims_cost_mean` | 124.6214 | 85.6595 | 207.7797 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 26830.6783 | 16310.8400 | 36502.1398 |
| `Claims_cost_count` | 11223.3333 | 5698.0000 | 16043.0000 |
| `Number_of_recorded_claims_sum` | 806.8333 | 381.0000 | 1165.0000 |
| `Number_of_recorded_claims_mean` | 0.0721 | 0.0586 | 0.0904 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 3.3333 | 3.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 11223.3333 | 5698.0000 | 16043.0000 |

### Table: `summary_Area.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Area` | `object` | 6 | 6 | A, B, C, D, E |
| `Severity_sum` | `float64` | 6 | 6 | 1610092.0, 1555867.0, 2376830.0, 723293.0, 748087.0 |
| `Severity_mean` | `float64` | 6 | 6 | 99.51739909759564, 117.49486482404473, 116.7287103427954, 89.11939379004436, 127... |
| `Severity_min` | `float64` | 6 | 1 | 0.0 |
| `Severity_max` | `float64` | 6 | 6 | 22340.0, 33642.0, 26507.0, 18872.0, 32196.0 |
| `Severity_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Pure_Premium_sum` | `float64` | 6 | 6 | 4618457.0, 6084878.0, 11840620.0, 7783541.0, 2981700.0 |
| `Pure_Premium_mean` | `float64` | 6 | 6 | 285.45997898510416, 459.5135175955294, 581.5057459974462, 959.0365943814688, 506... |
| `Pure_Premium_min` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 6 | 6 | 266130.0, 710046.0, 2523695.0, 3142976.0, 471471.0 |
| `Pure_Premium_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `claims_Frequency_sum` | `float64` | 6 | 6 | 2765.338975340265, 3141.461235356758, 4063.208792506872, 1647.4967783823672, 109... |
| `claims_Frequency_mean` | `float64` | 6 | 6 | 0.1709215016589569, 0.2372346500042862, 0.1995486097881776, 0.2029936888100501, ... |
| `claims_Frequency_min` | `float64` | 6 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 6 | 4 | 45.6562506192129, 182.62498580090733, 365.2499716018147, 91.3125012384258 |
| `claims_Frequency_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Pure_Premium_sum.1` | `float64` | 6 | 6 | 4618457.0, 6084878.0, 11840620.0, 7783541.0, 2981700.0 |
| `Pure_Premium_mean.1` | `float64` | 6 | 6 | 285.45997898510416, 459.5135175955294, 581.5057459974462, 959.0365943814688, 506... |
| `Pure_Premium_min.1` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 6 | 6 | 266130.0, 710046.0, 2523695.0, 3142976.0, 471471.0 |
| `Pure_Premium_count.1` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Pure_Premium_sum.2` | `float64` | 6 | 6 | 4618457.0, 6084878.0, 11840620.0, 7783541.0, 2981700.0 |
| `Pure_Premium_mean.2` | `float64` | 6 | 6 | 285.45997898510416, 459.5135175955294, 581.5057459974462, 959.0365943814688, 506... |
| `Pure_Premium_min.2` | `float64` | 6 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 6 | 6 | 266130.0, 710046.0, 2523695.0, 3142976.0, 471471.0 |
| `Pure_Premium_count.2` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Exposure_sum` | `float64` | 6 | 6 | 7521.670089646, 6237.434634382, 9474.039699684, 3782.899384291, 2748.843258319 |
| `Exposure_mean` | `float64` | 6 | 6 | 0.4649032752114469, 0.4710341817234557, 0.4652804095709655, 0.4661039162507392, ... |
| `Exposure_min` | `float64` | 6 | 1 | 0.002737851 |
| `Exposure_max` | `float64` | 6 | 1 | 0.999315537 |
| `Exposure_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Claims_cost_sum` | `float64` | 6 | 6 | 1741136.7137376, 1633560.834005, 2479817.237914, 767178.3305317, 784288.3105851 |
| `Claims_cost_mean` | `float64` | 6 | 6 | 107.61707854240684, 123.36209288664855, 121.78652577909833, 94.52665482155004, 1... |
| `Claims_cost_min` | `float64` | 6 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 6 | 6 | 22339.54999, 33642.2699, 26507.29498, 18871.62, 32195.81995 |
| `Claims_cost_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |
| `Number_of_recorded_claims_sum` | `int64` | 6 | 6 | 1160, 1002, 1460, 512, 407 |
| `Number_of_recorded_claims_mean` | `float64` | 6 | 6 | 0.0716978799678595, 0.0756683280471227, 0.071702190354582, 0.063085263676688, 0.... |
| `Number_of_recorded_claims_min` | `int64` | 6 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 6 | 2 | 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 6 | 6 | 16179, 13242, 20362, 8116, 5882 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 1274604.0000 | 633455.0000 | 2376830.0000 |
| `Severity_mean` | 121.3383 | 89.1194 | 177.9868 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 28343.1667 | 18872.0000 | 36502.0000 |
| `Severity_count` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Pure_Premium_sum` | 6243682.5000 | 2981700.0000 | 11840620.0000 |
| `Pure_Premium_mean` | 659.8846 | 285.4600 | 1166.8724 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 1503654.5000 | 266130.0000 | 3142976.0000 |
| `Pure_Premium_count` | 11223.3333 | 3559.0000 | 20362.0000 |
| `claims_Frequency_sum` | 2263.0684 | 864.4346 | 4063.2088 |
| `claims_Frequency_mean` | 0.2067 | 0.1709 | 0.2429 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 159.7969 | 45.6563 | 365.2500 |
| `claims_Frequency_count` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Pure_Premium_sum.1` | 6243682.5000 | 2981700.0000 | 11840620.0000 |
| `Pure_Premium_mean.1` | 659.8846 | 285.4600 | 1166.8724 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 1503654.5000 | 266130.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Pure_Premium_sum.2` | 6243682.5000 | 2981700.0000 | 11840620.0000 |
| `Pure_Premium_mean.2` | 659.8846 | 285.4600 | 1166.8724 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 1503654.5000 | 266130.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Exposure_sum` | 5247.7467 | 1721.5934 | 9474.0397 |
| `Exposure_mean` | 0.4697 | 0.4649 | 0.4837 |
| `Exposure_min` | 0.0027 | 0.0027 | 0.0027 |
| `Exposure_max` | 0.9993 | 0.9993 | 0.9993 |
| `Exposure_count` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Claims_cost_sum` | 1346836.5297 | 675037.7516 | 2479817.2379 |
| `Claims_cost_mean` | 128.3833 | 94.5267 | 189.6706 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 28343.1158 | 18871.6200 | 36502.1398 |
| `Claims_cost_count` | 11223.3333 | 3559.0000 | 20362.0000 |
| `Number_of_recorded_claims_sum` | 806.8333 | 300.0000 | 1460.0000 |
| `Number_of_recorded_claims_mean` | 0.0726 | 0.0631 | 0.0843 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 3.3333 | 3.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 11223.3333 | 3559.0000 | 20362.0000 |

### Table: `summary_Claims_cost_categories.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Claims_cost_categories` | `object` | 5 | 5 | Claims_cost 0, Claims_cost 1-10k, Claims_cost 10k-20k, Claims_cost 20k-30k, Clai... |
| `Severity_sum` | `float64` | 5 | 5 | 0.0, 6169468.0, 1046689.0, 296312.0, 135155.0 |
| `Severity_mean` | `float64` | 5 | 5 | 0.0, 1392.9708737864078, 12170.802325581397, 22793.23076923077, 33788.75 |
| `Severity_min` | `float64` | 5 | 5 | 0.0, 200.0, 3533.0, 20129.0, 32196.0 |
| `Severity_max` | `float64` | 5 | 5 | 0.0, 9921.0, 18872.0, 28013.0, 36502.0 |
| `Severity_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Pure_Premium_sum` | `float64` | 5 | 5 | 0.0, 23136574.0, 10622820.0, 2777143.0, 925558.0 |
| `Pure_Premium_mean` | `float64` | 5 | 5 | 0.0, 5223.882140438022, 123521.16279069768, 213626.38461538465, 231389.5 |
| `Pure_Premium_min` | `float64` | 5 | 5 | 0.0, 200.0, 11004.0, 21684.0, 103325.0 |
| `Pure_Premium_max` | `float64` | 5 | 5 | 0.0, 3142976.0, 2978066.0, 1907609.0, 476156.0 |
| `Pure_Premium_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `claims_Frequency_sum` | `float64` | 5 | 5 | 0.0, 12671.406801446785, 752.3797315478055, 127.91900843547612, 26.7046851786713... |
| `claims_Frequency_mean` | `float64` | 5 | 5 | 0.0, 2.861008534984598, 8.748601529625645, 9.839923725805855, 6.676171294667831 |
| `claims_Frequency_min` | `float64` | 5 | 3 | 0.0, 1.0006849318104818, 3.148706899598641 |
| `claims_Frequency_max` | `float64` | 5 | 5 | 0.0, 365.2499716018147, 182.62498580090733, 91.3125012384258, 13.04464286389812 |
| `claims_Frequency_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Pure_Premium_sum.1` | `float64` | 5 | 5 | 0.0, 23136574.0, 10622820.0, 2777143.0, 925558.0 |
| `Pure_Premium_mean.1` | `float64` | 5 | 5 | 0.0, 5223.882140438022, 123521.16279069768, 213626.38461538465, 231389.5 |
| `Pure_Premium_min.1` | `float64` | 5 | 5 | 0.0, 200.0, 11004.0, 21684.0, 103325.0 |
| `Pure_Premium_max.1` | `float64` | 5 | 5 | 0.0, 3142976.0, 2978066.0, 1907609.0, 476156.0 |
| `Pure_Premium_count.1` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Pure_Premium_sum.2` | `float64` | 5 | 5 | 0.0, 23136574.0, 10622820.0, 2777143.0, 925558.0 |
| `Pure_Premium_mean.2` | `float64` | 5 | 5 | 0.0, 5223.882140438022, 123521.16279069768, 213626.38461538465, 231389.5 |
| `Pure_Premium_min.2` | `float64` | 5 | 5 | 0.0, 200.0, 11004.0, 21684.0, 103325.0 |
| `Pure_Premium_max.2` | `float64` | 5 | 5 | 0.0, 3142976.0, 2978066.0, 1907609.0, 476156.0 |
| `Pure_Premium_count.2` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Exposure_sum` | `float64` | 5 | 5 | 28701.563315481, 2734.603696233, 43.91238878, 5.626283369, 0.774811772 |
| `Exposure_mean` | `float64` | 5 | 5 | 0.4569730498579957, 0.6174314057875366, 0.5106091718604652, 0.4327910283846154, ... |
| `Exposure_min` | `float64` | 5 | 4 | 0.002737851, 0.005475702, 0.010951403, 0.076659822 |
| `Exposure_max` | `float64` | 5 | 2 | 0.999315537, 0.317590691 |
| `Exposure_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Claims_cost_sum` | `float64` | 5 | 5 | 0.0, 6507047.9654497, 1142503.87894, 296312.30439, 135155.02955 |
| `Claims_cost_mean` | `float64` | 5 | 5 | 0.0, 1469.1912317565366, 13284.92882488372, 22793.254183846155, 33788.7573875 |
| `Claims_cost_min` | `float64` | 5 | 5 | 0.0, 200.0, 10037.17996, 20129.38995, 32195.81995 |
| `Claims_cost_max` | `float64` | 5 | 5 | 0.0, 9921.129944, 19847.73996, 28012.82996, 36502.13977 |
| `Claims_cost_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |
| `Number_of_recorded_claims_sum` | `int64` | 5 | 5 | 0, 4723, 101, 13, 4 |
| `Number_of_recorded_claims_mean` | `float64` | 5 | 4 | 0.0, 1.0663806728381124, 1.1744186046511629, 1.0 |
| `Number_of_recorded_claims_min` | `int64` | 5 | 2 | 0, 1 |
| `Number_of_recorded_claims_max` | `int64` | 5 | 4 | 0, 4, 3, 1 |
| `Number_of_recorded_claims_count` | `int64` | 5 | 5 | 62808, 4429, 86, 13, 4 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 1529524.8000 | 0.0000 | 6169468.0000 |
| `Severity_mean` | 14029.1508 | 0.0000 | 33788.7500 |
| `Severity_min` | 11211.6000 | 0.0000 | 32196.0000 |
| `Severity_max` | 18661.6000 | 0.0000 | 36502.0000 |
| `Severity_count` | 13468.0000 | 4.0000 | 62808.0000 |
| `Pure_Premium_sum` | 7492419.0000 | 0.0000 | 23136574.0000 |
| `Pure_Premium_mean` | 114752.1859 | 0.0000 | 231389.5000 |
| `Pure_Premium_min` | 27242.6000 | 0.0000 | 103325.0000 |
| `Pure_Premium_max` | 1700961.4000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count` | 13468.0000 | 4.0000 | 62808.0000 |
| `claims_Frequency_sum` | 2715.6820 | 0.0000 | 12671.4068 |
| `claims_Frequency_mean` | 5.6251 | 0.0000 | 9.8399 |
| `claims_Frequency_min` | 1.2302 | 0.0000 | 3.1487 |
| `claims_Frequency_max` | 130.4464 | 0.0000 | 365.2500 |
| `claims_Frequency_count` | 13468.0000 | 4.0000 | 62808.0000 |
| `Pure_Premium_sum.1` | 7492419.0000 | 0.0000 | 23136574.0000 |
| `Pure_Premium_mean.1` | 114752.1859 | 0.0000 | 231389.5000 |
| `Pure_Premium_min.1` | 27242.6000 | 0.0000 | 103325.0000 |
| `Pure_Premium_max.1` | 1700961.4000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 13468.0000 | 4.0000 | 62808.0000 |
| `Pure_Premium_sum.2` | 7492419.0000 | 0.0000 | 23136574.0000 |
| `Pure_Premium_mean.2` | 114752.1859 | 0.0000 | 231389.5000 |
| `Pure_Premium_min.2` | 27242.6000 | 0.0000 | 103325.0000 |
| `Pure_Premium_max.2` | 1700961.4000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 13468.0000 | 4.0000 | 62808.0000 |
| `Exposure_sum` | 6297.2961 | 0.7748 | 28701.5633 |
| `Exposure_mean` | 0.4423 | 0.1937 | 0.6174 |
| `Exposure_min` | 0.0197 | 0.0027 | 0.0767 |
| `Exposure_max` | 0.8630 | 0.3176 | 0.9993 |
| `Exposure_count` | 13468.0000 | 4.0000 | 62808.0000 |
| `Claims_cost_sum` | 1616203.8357 | 0.0000 | 6507047.9654 |
| `Claims_cost_mean` | 14267.2263 | 0.0000 | 33788.7574 |
| `Claims_cost_min` | 12512.4780 | 0.0000 | 32195.8200 |
| `Claims_cost_max` | 18856.7679 | 0.0000 | 36502.1398 |
| `Claims_cost_count` | 13468.0000 | 4.0000 | 62808.0000 |
| `Number_of_recorded_claims_sum` | 968.2000 | 0.0000 | 4723.0000 |
| `Number_of_recorded_claims_mean` | 0.8482 | 0.0000 | 1.1744 |
| `Number_of_recorded_claims_min` | 0.8000 | 0.0000 | 1.0000 |
| `Number_of_recorded_claims_max` | 1.8000 | 0.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 13468.0000 | 4.0000 | 62808.0000 |

### Table: `summary_Gender.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Gender` | `object` | 2 | 2 | F, M |
| `Severity_sum` | `float64` | 2 | 2 | 4126383.0, 3521241.0 |
| `Severity_mean` | `float64` | 2 | 2 | 107.74127261808404, 121.25068007300024 |
| `Severity_min` | `float64` | 2 | 1 | 0.0 |
| `Severity_max` | `float64` | 2 | 2 | 36502.0, 33642.0 |
| `Severity_count` | `int64` | 2 | 2 | 38299, 29041 |
| `Pure_Premium_sum` | `float64` | 2 | 2 | 21825479.0, 15636616.0 |
| `Pure_Premium_mean` | `float64` | 2 | 2 | 569.8707276952401, 538.4324231259254 |
| `Pure_Premium_min` | `float64` | 2 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 2 | 2 | 3142976.0, 2978066.0 |
| `Pure_Premium_count` | `int64` | 2 | 2 | 38299, 29041 |
| `claims_Frequency_sum` | `float64` | 2 | 2 | 8112.499906582375, 5465.910320026364 |
| `claims_Frequency_mean` | `float64` | 2 | 2 | 0.211820149523026, 0.1882135711589257 |
| `claims_Frequency_min` | `float64` | 2 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 2 | 2 | 365.2499716018147, 182.62498580090733 |
| `claims_Frequency_count` | `int64` | 2 | 2 | 38299, 29041 |
| `Pure_Premium_sum.1` | `float64` | 2 | 2 | 21825479.0, 15636616.0 |
| `Pure_Premium_mean.1` | `float64` | 2 | 2 | 569.8707276952401, 538.4324231259254 |
| `Pure_Premium_min.1` | `float64` | 2 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 2 | 2 | 3142976.0, 2978066.0 |
| `Pure_Premium_count.1` | `int64` | 2 | 2 | 38299, 29041 |
| `Pure_Premium_sum.2` | `float64` | 2 | 2 | 21825479.0, 15636616.0 |
| `Pure_Premium_mean.2` | `float64` | 2 | 2 | 569.8707276952401, 538.4324231259254 |
| `Pure_Premium_min.2` | `float64` | 2 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 2 | 2 | 3142976.0, 2978066.0 |
| `Pure_Premium_count.2` | `int64` | 2 | 2 | 38299, 29041 |
| `Exposure_sum` | `float64` | 2 | 2 | 17774.707736021, 13711.772759614 |
| `Exposure_mean` | `float64` | 2 | 2 | 0.4641037033870597, 0.4721522247723563 |
| `Exposure_min` | `float64` | 2 | 1 | 0.002737851 |
| `Exposure_max` | `float64` | 2 | 1 | 0.999315537 |
| `Exposure_count` | `int64` | 2 | 2 | 38299, 29041 |
| `Claims_cost_sum` | `float64` | 2 | 2 | 4359339.5751155, 3721679.6032142 |
| `Claims_cost_mean` | `float64` | 2 | 2 | 113.82384853692002, 128.1525981617093 |
| `Claims_cost_min` | `float64` | 2 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 2 | 2 | 36502.13977, 33642.2699 |
| `Claims_cost_count` | `int64` | 2 | 2 | 38299, 29041 |
| `Number_of_recorded_claims_sum` | `int64` | 2 | 2 | 2784, 2057 |
| `Number_of_recorded_claims_mean` | `float64` | 2 | 2 | 0.0726911929815399, 0.0708308942529527 |
| `Number_of_recorded_claims_min` | `int64` | 2 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 2 | 2 | 4, 3 |
| `Number_of_recorded_claims_count` | `int64` | 2 | 2 | 38299, 29041 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 3823812.0000 | 3521241.0000 | 4126383.0000 |
| `Severity_mean` | 114.4960 | 107.7413 | 121.2507 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 35072.0000 | 33642.0000 | 36502.0000 |
| `Severity_count` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Pure_Premium_sum` | 18731047.5000 | 15636616.0000 | 21825479.0000 |
| `Pure_Premium_mean` | 554.1516 | 538.4324 | 569.8707 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 3060521.0000 | 2978066.0000 | 3142976.0000 |
| `Pure_Premium_count` | 33670.0000 | 29041.0000 | 38299.0000 |
| `claims_Frequency_sum` | 6789.2051 | 5465.9103 | 8112.4999 |
| `claims_Frequency_mean` | 0.2000 | 0.1882 | 0.2118 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 273.9375 | 182.6250 | 365.2500 |
| `claims_Frequency_count` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Pure_Premium_sum.1` | 18731047.5000 | 15636616.0000 | 21825479.0000 |
| `Pure_Premium_mean.1` | 554.1516 | 538.4324 | 569.8707 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 3060521.0000 | 2978066.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Pure_Premium_sum.2` | 18731047.5000 | 15636616.0000 | 21825479.0000 |
| `Pure_Premium_mean.2` | 554.1516 | 538.4324 | 569.8707 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 3060521.0000 | 2978066.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Exposure_sum` | 15743.2402 | 13711.7728 | 17774.7077 |
| `Exposure_mean` | 0.4681 | 0.4641 | 0.4722 |
| `Exposure_min` | 0.0027 | 0.0027 | 0.0027 |
| `Exposure_max` | 0.9993 | 0.9993 | 0.9993 |
| `Exposure_count` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Claims_cost_sum` | 4040509.5892 | 3721679.6032 | 4359339.5751 |
| `Claims_cost_mean` | 120.9882 | 113.8238 | 128.1526 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 35072.2048 | 33642.2699 | 36502.1398 |
| `Claims_cost_count` | 33670.0000 | 29041.0000 | 38299.0000 |
| `Number_of_recorded_claims_sum` | 2420.5000 | 2057.0000 | 2784.0000 |
| `Number_of_recorded_claims_mean` | 0.0718 | 0.0708 | 0.0727 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 3.5000 | 3.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 33670.0000 | 29041.0000 | 38299.0000 |

### Table: `summary_Veh_age.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Veh_age` | `int64` | 4 | 4 | 1, 2, 3, 4 |
| `Severity_sum` | `float64` | 4 | 4 | 1290785.0, 2194740.0, 2379748.0, 1782351.0 |
| `Severity_mean` | `float64` | 4 | 4 | 105.94968398588196, 133.32968835429196, 119.4532677442024, 94.93720038350912 |
| `Severity_min` | `float64` | 4 | 1 | 0.0 |
| `Severity_max` | `float64` | 4 | 4 | 36502.0, 33642.0, 24718.0, 21456.0 |
| `Severity_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Pure_Premium_sum` | `float64` | 4 | 4 | 3511437.0, 13926204.0, 12757336.0, 7267118.0 |
| `Pure_Premium_mean` | `float64` | 4 | 4 | 288.2243289830091, 846.0120284308365, 640.3642204597932, 387.08415894321934 |
| `Pure_Premium_min` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 4 | 4 | 476156.0, 2523695.0, 3142976.0, 454280.0 |
| `Pure_Premium_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `claims_Frequency_sum` | `float64` | 4 | 4 | 2083.667417172997, 3901.592413882988, 4147.451810997629, 3445.6985845551235 |
| `claims_Frequency_mean` | `float64` | 4 | 4 | 0.1710307327565457, 0.2370203762762279, 0.2081845101394252, 0.183535665524402 |
| `claims_Frequency_min` | `float64` | 4 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 4 | 4 | 52.17857009429085, 182.62498580090733, 365.2499716018147, 91.3125012384258 |
| `claims_Frequency_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Pure_Premium_sum.1` | `float64` | 4 | 4 | 3511437.0, 13926204.0, 12757336.0, 7267118.0 |
| `Pure_Premium_mean.1` | `float64` | 4 | 4 | 288.2243289830091, 846.0120284308365, 640.3642204597932, 387.08415894321934 |
| `Pure_Premium_min.1` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 4 | 4 | 476156.0, 2523695.0, 3142976.0, 454280.0 |
| `Pure_Premium_count.1` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Pure_Premium_sum.2` | `float64` | 4 | 4 | 3511437.0, 13926204.0, 12757336.0, 7267118.0 |
| `Pure_Premium_mean.2` | `float64` | 4 | 4 | 288.2243289830091, 846.0120284308365, 640.3642204597932, 387.08415894321934 |
| `Pure_Premium_min.2` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 4 | 4 | 476156.0, 2523695.0, 3142976.0, 454280.0 |
| `Pure_Premium_count.2` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Exposure_sum` | `float64` | 4 | 4 | 5299.553730853, 7835.701574925, 9454.176592282, 8897.048597575 |
| `Exposure_mean` | `float64` | 4 | 4 | 0.4349957917469425, 0.4760161335839257, 0.474559612101295, 0.4739026631285288 |
| `Exposure_min` | `float64` | 4 | 1 | 0.002737851 |
| `Exposure_max` | `float64` | 4 | 1 | 0.999315537 |
| `Exposure_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Claims_cost_sum` | `float64` | 4 | 4 | 1354904.6387583, 2308581.1903013, 2505181.4785759, 1912351.8706942 |
| `Claims_cost_mean` | `float64` | 4 | 4 | 111.2127258276533, 140.2455008991738, 125.74949696696618, 101.86171677288804 |
| `Claims_cost_min` | `float64` | 4 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 4 | 4 | 36502.13977, 33642.2699, 24718.17999, 21456.26996 |
| `Claims_cost_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |
| `Number_of_recorded_claims_sum` | `int64` | 4 | 4 | 869, 1346, 1432, 1194 |
| `Number_of_recorded_claims_mean` | `float64` | 4 | 4 | 0.0713289009275219, 0.0817690298280784, 0.0718803332998695, 0.063598593799936 |
| `Number_of_recorded_claims_min` | `int64` | 4 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 4 | 2 | 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 4 | 4 | 12183, 16461, 19922, 18774 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Veh_age` | 2.5000 | 1.0000 | 4.0000 |
| `Severity_sum` | 1911906.0000 | 1290785.0000 | 2379748.0000 |
| `Severity_mean` | 113.4175 | 94.9372 | 133.3297 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 29079.5000 | 21456.0000 | 36502.0000 |
| `Severity_count` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Pure_Premium_sum` | 9365523.7500 | 3511437.0000 | 13926204.0000 |
| `Pure_Premium_mean` | 540.4212 | 288.2243 | 846.0120 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 1649276.7500 | 454280.0000 | 3142976.0000 |
| `Pure_Premium_count` | 16835.0000 | 12183.0000 | 19922.0000 |
| `claims_Frequency_sum` | 3394.6026 | 2083.6674 | 4147.4518 |
| `claims_Frequency_mean` | 0.1999 | 0.1710 | 0.2370 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 172.8415 | 52.1786 | 365.2500 |
| `claims_Frequency_count` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Pure_Premium_sum.1` | 9365523.7500 | 3511437.0000 | 13926204.0000 |
| `Pure_Premium_mean.1` | 540.4212 | 288.2243 | 846.0120 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 1649276.7500 | 454280.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Pure_Premium_sum.2` | 9365523.7500 | 3511437.0000 | 13926204.0000 |
| `Pure_Premium_mean.2` | 540.4212 | 288.2243 | 846.0120 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 1649276.7500 | 454280.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Exposure_sum` | 7871.6201 | 5299.5537 | 9454.1766 |
| `Exposure_mean` | 0.4649 | 0.4350 | 0.4760 |
| `Exposure_min` | 0.0027 | 0.0027 | 0.0027 |
| `Exposure_max` | 0.9993 | 0.9993 | 0.9993 |
| `Exposure_count` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Claims_cost_sum` | 2020254.7946 | 1354904.6388 | 2505181.4786 |
| `Claims_cost_mean` | 119.7674 | 101.8617 | 140.2455 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 29079.7149 | 21456.2700 | 36502.1398 |
| `Claims_cost_count` | 16835.0000 | 12183.0000 | 19922.0000 |
| `Number_of_recorded_claims_sum` | 1210.2500 | 869.0000 | 1432.0000 |
| `Number_of_recorded_claims_mean` | 0.0721 | 0.0636 | 0.0818 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 3.2500 | 3.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 16835.0000 | 12183.0000 | 19922.0000 |

### Table: `summary_Veh_body.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Veh_body` | `object` | 13 | 13 | BUS, CONVT, COUPE, HBACK, HDTOP |
| `Severity_sum` | `float64` | 13 | 13 | 10726.0, 6889.0, 149195.0, 2066715.0, 224048.0 |
| `Severity_mean` | `float64` | 13 | 13 | 282.2631578947368, 85.04938271604938, 191.5211810012837, 110.27184932237756, 142... |
| `Severity_min` | `float64` | 13 | 1 | 0.0 |
| `Severity_max` | `float64` | 13 | 13 | 4791.0, 6126.0, 17735.0, 18291.0, 32815.0 |
| `Severity_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Pure_Premium_sum` | `float64` | 13 | 13 | 27377.0, 14845.0, 452047.0, 7936746.0, 488327.0 |
| `Pure_Premium_mean` | `float64` | 13 | 13 | 720.4473684210526, 183.2716049382716, 580.2913992297817, 423.4738021555864, 310.... |
| `Pure_Premium_min` | `float64` | 13 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 13 | 13 | 17676.0, 13727.0, 52532.0, 710046.0, 103325.0 |
| `Pure_Premium_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `claims_Frequency_sum` | `float64` | 13 | 13 | 14.67894230553444, 5.109135489724437, 206.8743245760174, 4076.131221948116, 285.... |
| `claims_Frequency_mean` | `float64` | 13 | 13 | 0.386287955408801, 0.0630757467867214, 0.2655639596611263, 0.2174864593932406, 0... |
| `claims_Frequency_min` | `float64` | 13 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 13 | 12 | 3.689393938387741, 2.240797547531338, 18.26249991416625, 182.62498580090733, 17.... |
| `claims_Frequency_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Pure_Premium_sum.1` | `float64` | 13 | 13 | 27377.0, 14845.0, 452047.0, 7936746.0, 488327.0 |
| `Pure_Premium_mean.1` | `float64` | 13 | 13 | 720.4473684210526, 183.2716049382716, 580.2913992297817, 423.4738021555864, 310.... |
| `Pure_Premium_min.1` | `float64` | 13 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 13 | 13 | 17676.0, 13727.0, 52532.0, 710046.0, 103325.0 |
| `Pure_Premium_count.1` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Pure_Premium_sum.2` | `float64` | 13 | 13 | 27377.0, 14845.0, 452047.0, 7936746.0, 488327.0 |
| `Pure_Premium_mean.2` | `float64` | 13 | 13 | 720.4473684210526, 183.2716049382716, 580.2913992297817, 423.4738021555864, 310.... |
| `Pure_Premium_min.2` | `float64` | 13 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 13 | 13 | 17676.0, 13727.0, 52532.0, 710046.0, 103325.0 |
| `Pure_Premium_count.2` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Exposure_sum` | `float64` | 13 | 13 | 18.973305959, 32.596851476, 318.776180738, 8707.080082927, 778.751540088 |
| `Exposure_mean` | `float64` | 13 | 13 | 0.4992975252368421, 0.4024302651358024, 0.4092120420256739, 0.4645758234407747, ... |
| `Exposure_min` | `float64` | 13 | 3 | 0.024640657, 0.002737851, 0.021902806 |
| `Exposure_max` | `float64` | 13 | 3 | 0.999315537, 0.988364134, 0.980150582 |
| `Exposure_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Claims_cost_sum` | `float64` | 13 | 13 | 11839.2599886, 6888.809998, 168681.8906597, 2159403.161903, 233210.1014385 |
| `Claims_cost_mean` | `float64` | 13 | 13 | 311.5594733842105, 85.04703701234567, 216.53644500603335, 115.21732802811866, 14... |
| `Claims_cost_min` | `float64` | 13 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 13 | 13 | 4790.839996, 6125.809998, 19847.73996, 18291.46991, 32814.79993 |
| `Claims_cost_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |
| `Number_of_recorded_claims_sum` | `int64` | 13 | 12 | 8, 3, 74, 1295, 133 |
| `Number_of_recorded_claims_mean` | `float64` | 13 | 13 | 0.2105263157894736, 0.037037037037037, 0.0949935815147625, 0.0690961476896809, 0... |
| `Number_of_recorded_claims_min` | `int64` | 13 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 13 | 4 | 2, 1, 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 13 | 13 | 38, 81, 779, 18742, 1573 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 588278.7692 | 785.0000 | 2207454.0000 |
| `Severity_mean` | 125.2874 | 29.0741 | 282.2632 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 16756.0769 | 585.0000 | 36502.0000 |
| `Severity_count` | 5180.0000 | 27.0000 | 22080.0000 |
| `Pure_Premium_sum` | 2881699.6154 | 2070.0000 | 15013895.0000 |
| `Pure_Premium_mean` | 507.1749 | 76.6667 | 2034.1419 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 719000.5385 | 1858.0000 | 3142976.0000 |
| `Pure_Premium_count` | 5180.0000 | 27.0000 | 22080.0000 |
| `claims_Frequency_sum` | 1044.4931 | 4.2379 | 4693.9145 |
| `claims_Frequency_mean` | 0.2026 | 0.0631 | 0.3863 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 73.0721 | 2.2408 | 365.2500 |
| `claims_Frequency_count` | 5180.0000 | 27.0000 | 22080.0000 |
| `Pure_Premium_sum.1` | 2881699.6154 | 2070.0000 | 15013895.0000 |
| `Pure_Premium_mean.1` | 507.1749 | 76.6667 | 2034.1419 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 719000.5385 | 1858.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 5180.0000 | 27.0000 | 22080.0000 |
| `Pure_Premium_sum.2` | 2881699.6154 | 2070.0000 | 15013895.0000 |
| `Pure_Premium_mean.2` | 507.1749 | 76.6667 | 2034.1419 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 719000.5385 | 1858.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 5180.0000 | 27.0000 | 22080.0000 |
| `Exposure_sum` | 2422.0370 | 11.6687 | 10370.7844 |
| `Exposure_mean` | 0.4634 | 0.4024 | 0.5409 |
| `Exposure_min` | 0.0059 | 0.0027 | 0.0246 |
| `Exposure_max` | 0.9970 | 0.9802 | 0.9993 |
| `Exposure_count` | 5180.0000 | 27.0000 | 22080.0000 |
| `Claims_cost_sum` | 621616.8599 | 1369.4582 | 2345814.8691 |
| `Claims_cost_mean` | 135.4805 | 50.7207 | 311.5595 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 16963.5298 | 1169.4582 | 36502.1398 |
| `Claims_cost_count` | 5180.0000 | 27.0000 | 22080.0000 |
| `Number_of_recorded_claims_sum` | 372.3846 | 3.0000 | 1571.0000 |
| `Number_of_recorded_claims_mean` | 0.0890 | 0.0370 | 0.2105 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 2.4615 | 1.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 5180.0000 | 27.0000 | 22080.0000 |

### Table: `summary_Veh_value.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Veh_value` | `float64` | 985 | 985 | 1800.0, 1900.0, 2000.0, 2100.0, 2200.0 |
| `Severity_sum` | `float64` | 985 | 505 | 0.0, 2882.0, 200.0, 1951.0, 2073.0 |
| `Severity_mean` | `float64` | 985 | 535 | 0.0, 64.04444444444445, 8.0, 60.96875, 2.1739130434782608 |
| `Severity_min` | `float64` | 985 | 12 | 0.0, 633.0, 1317.0, 672.0, 383.0 |
| `Severity_max` | `float64` | 985 | 493 | 0.0, 1458.0, 200.0, 1951.0, 1873.0 |
| `Severity_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum` | `float64` | 985 | 542 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean` | `float64` | 985 | 546 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min` | `float64` | 985 | 12 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max` | `float64` | 985 | 538 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `claims_Frequency_sum` | `float64` | 985 | 523 | 0.0, 6.904575355368477, 1.0838278934846244, 3.652499996174007, 5.217857145559248 |
| `claims_Frequency_mean` | `float64` | 985 | 546 | 0.0, 0.1534350078970772, 0.0433531157393849, 0.1141406248804377, 0.0567158385386... |
| `claims_Frequency_min` | `float64` | 985 | 12 | 0.0, 1.0006849318104818, 1.03470254942265, 2.2136363630326445, 1.503086420370094 |
| `claims_Frequency_max` | `float64` | 985 | 272 | 0.0, 2.5541958013245667, 1.0838278934846244, 3.652499996174007, 5.21785714555924... |
| `claims_Frequency_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum.1` | `float64` | 985 | 542 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean.1` | `float64` | 985 | 546 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min.1` | `float64` | 985 | 12 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max.1` | `float64` | 985 | 538 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count.1` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Pure_Premium_sum.2` | `float64` | 985 | 542 | 0.0, 4288.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_mean.2` | `float64` | 985 | 546 | 0.0, 95.28888888888888, 8.68, 222.6875, 11.347826086956522 |
| `Pure_Premium_min.2` | `float64` | 985 | 12 | 0.0, 633.0, 1363.0, 1488.0, 576.0 |
| `Pure_Premium_max.2` | `float64` | 985 | 538 | 0.0, 1528.0, 217.0, 7126.0, 1044.0 |
| `Pure_Premium_count.2` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Exposure_sum` | `float64` | 985 | 896 | 2.135523615, 9.0403833, 1.237508557, 1.754962354, 27.753593429 |
| `Exposure_mean` | `float64` | 985 | 918 | 0.266940451875, 0.6954141, 0.2475017114, 0.3509924707999999, 0.6167465206444445 |
| `Exposure_min` | `float64` | 985 | 219 | 0.049281314, 0.314852841, 0.030116359, 0.062970568, 0.052019165 |
| `Exposure_max` | `float64` | 985 | 268 | 0.462696783, 0.895277207, 0.459958932, 0.862422998, 0.999315537 |
| `Exposure_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Claims_cost_sum` | `float64` | 985 | 518 | 0.0, 3586.6354535, 200.0, 1951.039997, 2072.809998 |
| `Claims_cost_mean` | `float64` | 985 | 540 | 0.0, 79.70301007777778, 8.0, 60.96999990625, 2.1739130434782608 |
| `Claims_cost_min` | `float64` | 985 | 12 | 0.0, 633.3499994, 1317.439999, 672.1799994, 383.3199997 |
| `Claims_cost_max` | `float64` | 985 | 512 | 0.0, 1457.959999, 200.0, 1951.039997, 1872.809998 |
| `Claims_cost_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |
| `Number_of_recorded_claims_sum` | `int64` | 985 | 41 | 0, 5, 1, 2, 9 |
| `Number_of_recorded_claims_mean` | `float64` | 985 | 336 | 0.0, 0.1111111111111111, 0.04, 0.03125, 0.0108695652173913 |
| `Number_of_recorded_claims_min` | `int64` | 985 | 2 | 0, 1 |
| `Number_of_recorded_claims_max` | `int64` | 985 | 5 | 0, 2, 1, 3, 4 |
| `Number_of_recorded_claims_count` | `int64` | 985 | 252 | 8, 13, 5, 45, 25 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Veh_value` | 46195.3574 | 1800.0000 | 345600.0000 |
| `Severity_sum` | 7764.0853 | 0.0000 | 91950.0000 |
| `Severity_mean` | 127.4914 | 0.0000 | 10424.0000 |
| `Severity_min` | 24.3827 | 0.0000 | 10424.0000 |
| `Severity_max` | 2853.9117 | 0.0000 | 36502.0000 |
| `Severity_count` | 68.3655 | 1.0000 | 543.0000 |
| `Pure_Premium_sum` | 38032.5838 | 0.0000 | 3302060.0000 |
| `Pure_Premium_mean` | 426.9278 | 0.0000 | 37972.4557 |
| `Pure_Premium_min` | 35.9005 | 0.0000 | 11004.0000 |
| `Pure_Premium_max` | 26550.3848 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count` | 68.3655 | 1.0000 | 543.0000 |
| `claims_Frequency_sum` | 13.7852 | 0.0000 | 457.7356 |
| `claims_Frequency_mean` | 0.1671 | 0.0000 | 4.3482 |
| `claims_Frequency_min` | 0.0182 | 0.0000 | 4.3482 |
| `claims_Frequency_max` | 5.4329 | 0.0000 | 365.2500 |
| `claims_Frequency_count` | 68.3655 | 1.0000 | 543.0000 |
| `Pure_Premium_sum.1` | 38032.5838 | 0.0000 | 3302060.0000 |
| `Pure_Premium_mean.1` | 426.9278 | 0.0000 | 37972.4557 |
| `Pure_Premium_min.1` | 35.9005 | 0.0000 | 11004.0000 |
| `Pure_Premium_max.1` | 26550.3848 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 68.3655 | 1.0000 | 543.0000 |
| `Pure_Premium_sum.2` | 38032.5838 | 0.0000 | 3302060.0000 |
| `Pure_Premium_mean.2` | 426.9278 | 0.0000 | 37972.4557 |
| `Pure_Premium_min.2` | 35.9005 | 0.0000 | 11004.0000 |
| `Pure_Premium_max.2` | 26550.3848 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 68.3655 | 1.0000 | 543.0000 |
| `Exposure_sum` | 31.9660 | 0.0027 | 261.5606 |
| `Exposure_mean` | 0.4551 | 0.0027 | 0.9993 |
| `Exposure_min` | 0.1663 | 0.0027 | 0.9993 |
| `Exposure_max` | 0.7653 | 0.0027 | 0.9993 |
| `Exposure_count` | 68.3655 | 1.0000 | 543.0000 |
| `Claims_cost_sum` | 8204.0804 | 0.0000 | 95821.7199 |
| `Claims_cost_mean` | 132.4808 | 0.0000 | 10423.5300 |
| `Claims_cost_min` | 24.3833 | 0.0000 | 10423.5300 |
| `Claims_cost_max` | 2977.9464 | 0.0000 | 36502.1398 |
| `Claims_cost_count` | 68.3655 | 1.0000 | 543.0000 |
| `Number_of_recorded_claims_sum` | 4.9147 | 0.0000 | 51.0000 |
| `Number_of_recorded_claims_mean` | 0.0718 | 0.0000 | 1.0000 |
| `Number_of_recorded_claims_min` | 0.0112 | 0.0000 | 1.0000 |
| `Number_of_recorded_claims_max` | 0.7624 | 0.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 68.3655 | 1.0000 | 543.0000 |

### Table: `summary_Veh_value_categories.csv`

| Column | Inferred Type | Non-null Count | Unique | Sample Values |
|---|---:|---:|---:|---|
| `Veh_value_categories` | `object` | 4 | 4 | Veh_value between 100k and 200k, Veh_value between 200k and 300k, Veh_value betw... |
| `Severity_sum` | `float64` | 4 | 3 | 14821.0, 0.0, 7632803.0 |
| `Severity_mean` | `float64` | 4 | 3 | 211.72857142857143, 0.0, 113.47699329497644 |
| `Severity_min` | `float64` | 4 | 1 | 0.0 |
| `Severity_max` | `float64` | 4 | 3 | 10424.0, 0.0, 36502.0 |
| `Severity_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Pure_Premium_sum` | `float64` | 4 | 3 | 25239.0, 0.0, 37436856.0 |
| `Pure_Premium_mean` | `float64` | 4 | 3 | 360.5571428571429, 0.0, 556.5742830382231 |
| `Pure_Premium_min` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max` | `float64` | 4 | 3 | 11004.0, 0.0, 3142976.0 |
| `Pure_Premium_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `claims_Frequency_sum` | `float64` | 4 | 3 | 7.590975877164455, 0.0, 13570.819250731573 |
| `claims_Frequency_mean` | `float64` | 4 | 3 | 0.1084425125309207, 0.0, 0.2017575673212847 |
| `claims_Frequency_min` | `float64` | 4 | 1 | 0.0 |
| `claims_Frequency_max` | `float64` | 4 | 3 | 4.34821428796604, 0.0, 365.2499716018147 |
| `claims_Frequency_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Pure_Premium_sum.1` | `float64` | 4 | 3 | 25239.0, 0.0, 37436856.0 |
| `Pure_Premium_mean.1` | `float64` | 4 | 3 | 360.5571428571429, 0.0, 556.5742830382231 |
| `Pure_Premium_min.1` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max.1` | `float64` | 4 | 3 | 11004.0, 0.0, 3142976.0 |
| `Pure_Premium_count.1` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Pure_Premium_sum.2` | `float64` | 4 | 3 | 25239.0, 0.0, 37436856.0 |
| `Pure_Premium_mean.2` | `float64` | 4 | 3 | 360.5571428571429, 0.0, 556.5742830382231 |
| `Pure_Premium_min.2` | `float64` | 4 | 1 | 0.0 |
| `Pure_Premium_max.2` | `float64` | 4 | 3 | 11004.0, 0.0, 3142976.0 |
| `Pure_Premium_count.2` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Exposure_sum` | `float64` | 4 | 4 | 29.544147846, 2.168377823, 0.813141684, 31453.954828282 |
| `Exposure_mean` | `float64` | 4 | 4 | 0.4220592549428572, 0.3613963038333334, 0.813141684, 0.4676264042383182 |
| `Exposure_min` | `float64` | 4 | 3 | 0.002737851, 0.101300479, 0.813141684 |
| `Exposure_max` | `float64` | 4 | 3 | 0.999315537, 0.810403833, 0.813141684 |
| `Exposure_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Claims_cost_sum` | `float64` | 4 | 3 | 14819.669991, 0.0, 8066199.5083387 |
| `Claims_cost_mean` | `float64` | 4 | 3 | 211.7095713, 0.0, 119.92030549245052 |
| `Claims_cost_min` | `float64` | 4 | 1 | 0.0 |
| `Claims_cost_max` | `float64` | 4 | 3 | 10423.53, 0.0, 36502.13977 |
| `Claims_cost_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |
| `Number_of_recorded_claims_sum` | `int64` | 4 | 3 | 3, 0, 4838 |
| `Number_of_recorded_claims_mean` | `float64` | 4 | 3 | 0.0428571428571428, 0.0, 0.0719266164161574 |
| `Number_of_recorded_claims_min` | `int64` | 4 | 1 | 0 |
| `Number_of_recorded_claims_max` | `int64` | 4 | 3 | 1, 0, 4 |
| `Number_of_recorded_claims_count` | `int64` | 4 | 4 | 70, 6, 1, 67263 |

**Numeric columns summary (mean/min/max)**

| Column | Mean | Min | Max |
|---|---:|---:|---:|
| `Severity_sum` | 1911906.0000 | 0.0000 | 7632803.0000 |
| `Severity_mean` | 81.3014 | 0.0000 | 211.7286 |
| `Severity_min` | 0.0000 | 0.0000 | 0.0000 |
| `Severity_max` | 11731.5000 | 0.0000 | 36502.0000 |
| `Severity_count` | 16835.0000 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum` | 9365523.7500 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean` | 229.2829 | 0.0000 | 556.5743 |
| `Pure_Premium_min` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max` | 788495.0000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count` | 16835.0000 | 1.0000 | 67263.0000 |
| `claims_Frequency_sum` | 3394.6026 | 0.0000 | 13570.8193 |
| `claims_Frequency_mean` | 0.0776 | 0.0000 | 0.2018 |
| `claims_Frequency_min` | 0.0000 | 0.0000 | 0.0000 |
| `claims_Frequency_max` | 92.3995 | 0.0000 | 365.2500 |
| `claims_Frequency_count` | 16835.0000 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum.1` | 9365523.7500 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean.1` | 229.2829 | 0.0000 | 556.5743 |
| `Pure_Premium_min.1` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.1` | 788495.0000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.1` | 16835.0000 | 1.0000 | 67263.0000 |
| `Pure_Premium_sum.2` | 9365523.7500 | 0.0000 | 37436856.0000 |
| `Pure_Premium_mean.2` | 229.2829 | 0.0000 | 556.5743 |
| `Pure_Premium_min.2` | 0.0000 | 0.0000 | 0.0000 |
| `Pure_Premium_max.2` | 788495.0000 | 0.0000 | 3142976.0000 |
| `Pure_Premium_count.2` | 16835.0000 | 1.0000 | 67263.0000 |
| `Exposure_sum` | 7871.6201 | 0.8131 | 31453.9548 |
| `Exposure_mean` | 0.5161 | 0.3614 | 0.8131 |
| `Exposure_min` | 0.2300 | 0.0027 | 0.8131 |
| `Exposure_max` | 0.9055 | 0.8104 | 0.9993 |
| `Exposure_count` | 16835.0000 | 1.0000 | 67263.0000 |
| `Claims_cost_sum` | 2020254.7946 | 0.0000 | 8066199.5083 |
| `Claims_cost_mean` | 82.9075 | 0.0000 | 211.7096 |
| `Claims_cost_min` | 0.0000 | 0.0000 | 0.0000 |
| `Claims_cost_max` | 11731.4174 | 0.0000 | 36502.1398 |
| `Claims_cost_count` | 16835.0000 | 1.0000 | 67263.0000 |
| `Number_of_recorded_claims_sum` | 1210.2500 | 0.0000 | 4838.0000 |
| `Number_of_recorded_claims_mean` | 0.0287 | 0.0000 | 0.0719 |
| `Number_of_recorded_claims_min` | 0.0000 | 0.0000 | 0.0000 |
| `Number_of_recorded_claims_max` | 1.2500 | 0.0000 | 4.0000 |
| `Number_of_recorded_claims_count` | 16835.0000 | 1.0000 | 67263.0000 |


## Measures (Detected / Suggested)

The script detected the following measure-like columns in dataset files:

- `Pure_Premium`
- `Pure_Premium_count`
- `Pure_Premium_count.1`
- `Pure_Premium_count.2`
- `Pure_Premium_max`
- `Pure_Premium_max.1`
- `Pure_Premium_max.2`
- `Pure_Premium_mean`
- `Pure_Premium_mean.1`
- `Pure_Premium_mean.2`
- `Pure_Premium_min`
- `Pure_Premium_min.1`
- `Pure_Premium_min.2`
- `Pure_Premium_sum`
- `Pure_Premium_sum.1`
- `Pure_Premium_sum.2`
- `Severity`
- `Severity_count`
- `Severity_max`
- `Severity_mean`
- `Severity_min`
- `Severity_sum`
- `actual_claims_relativity`
- `claims_Frequency`
- `claims_Frequency_count`
- `claims_Frequency_max`
- `claims_Frequency_mean`
- `claims_Frequency_min`
- `claims_Frequency_sum`
- `pure_premium`
- `severity`

### Suggested DAX formulas
These DAX expressions are suggested based on the project's existing calculations (also present in the project notebook).
Adjust field names to match your model when creating measures in Power BI:

**Severity**:

```dax
Severity = IF([Number_of_recorded_claims] <> 0, [Claims_cost] / [Number_of_recorded_claims], 0)
```

**Claims Frequency**:

```dax
Claims_Frequency = DIVIDE([Number_of_recorded_claims], [Exposure], 0)
```

**Pure Premium**:

```dax
Pure_Premium = [Severity] * [Claims_Frequency]
```

**Overall Pure Premium**:

```dax
Overall_Pure_Premium = DIVIDE(SUM([Claims_cost]), SUM([Exposure]), 0)
```

**Actual Claims Relativity**:

```dax
Actual_Claims_Relativity = DIVIDE([Pure_Premium], [Overall_Pure_Premium], 0)
```

## Recommended documentation to add (manual)


- Business descriptions for each table and column (what the field means, units, cardinality).
- Grain of the table (row-level meaning, e.g., policy-period, transaction-level).
- Data source and refresh schedule.
- Keys and relationships (primary/foreign keys) between tables.
- Any transformations applied in Power Query or ETL steps.
- Calculation logic and validation notes for measures.
- Data quality notes and known issues.
- Owner/Contact for each table/measure.
