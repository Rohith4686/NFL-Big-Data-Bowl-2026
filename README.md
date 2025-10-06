# NFL Big Data Bowl 2026
### Measuring Individual Defender Skill During Pass Coverage

**Competition:** [NFL Big Data Bowl 2026 — University Track](https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-analytics)  
**Track:** University Track  
**Season:** 2023 NFL Season (Weeks 1–18)

---

## Overview

When a quarterback throws the ball, two things happen simultaneously: the receiver tries to get to the landing spot, and defenders try to stop them. Standard stats like pass breakups and tackles don't capture *how well* a defender actually moved to contest the throw.

This project builds a framework to quantify individual defensive back skill during the time the ball is in the air, using NFL Next Gen Stats player tracking data.

### Pipeline

```
Raw Tracking Data
       │
       ▼
Feature Engineering (15+ features)
       │
       ▼
XGBoost Catch Probability Model
       │
       ▼
RFCDE Ghost Defender (league-average baseline)
       │
       ▼
Mixed-Effects Defender Metric (skill vs. noise)
       │
       ▼
2023 Defender Rankings
```

---

## Results

> *(To be updated as project progresses)*

| Metric | Value |
|--------|-------|
| Catch Probability Model Brier Score | TBD |
| Coverage Plays Analyzed | TBD |
| Defenders Ranked | TBD |

---

## Repository Structure

```
nfl-big-data-bowl-2026/
│
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
│
├── writeup/
│   └── writeup.md              # Final Kaggle writeup (≤2000 words)
│
├── data/
│   ├── raw/                    # NOT committed — download from Kaggle
│   └── processed/              # Lightweight processed outputs
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_catch_probability_model.ipynb
│   ├── 04_rfcde_ghost_defender.ipynb
│   └── 05_mixed_effects_metric.ipynb
│
├── src/
│   ├── features.py             # Feature engineering
│   ├── models.py               # Model training/inference
│   ├── rfcde.py                # Ghost defender
│   ├── mixed_effects.py        # Defender scoring metric
│   └── viz.py                  # Plotting utilities
│
└── results/
    ├── figures/                # All saved plots
    └── tables/                 # Model outputs, defender rankings
```

---

## How to Reproduce

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/nfl-big-data-bowl-2026.git
cd nfl-big-data-bowl-2026
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the data
Download from the [Kaggle competition page](https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-analytics/data) and place files in `data/raw/`.

```
data/raw/
├── train/
│   ├── input_2023_w01.csv
│   ├── output_2023_w01.csv
│   └── ... (weeks 01–18)
└── supplementary.csv
```

### 4. Run notebooks in order
```
01_eda.ipynb → 02_feature_engineering.ipynb → 03_catch_probability_model.ipynb → ...
```

---

## Methods

### Catch Probability Model
XGBoost classifier trained on 15+ engineered tracking features. Evaluated via Brier score and leave-one-week-out cross-validation to prevent data leakage.

### Ghost Defender (RFCDE)
Random Forest Conditional Density Estimation model that generates a distribution of where a *league-average* defender would position given the same play context. The gap between actual and ghost behavior isolates individual skill.

### Mixed-Effects Defender Metric
A mixed-effects framework that treats each defender as a random effect, separating true skill from play context, scheme, and sample size noise (via shrinkage/partial pooling).

---

## Citation

```
Michael Lopez, Tom Bliss, Ally Blake, and Addison Howard.
NFL Big Data Bowl 2026 - Analytics.
https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-analytics, 2025. Kaggle.
```

---

*Last updated: October 2025*
