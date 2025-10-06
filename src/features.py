"""
features.py
-----------
Feature engineering for the catch probability model and defender metric.

All functions take a merged DataFrame and return a DataFrame with new columns.
Run this after data_loader.py.
"""

import numpy as np
import pandas as pd


# ── Placeholder: fill in during Week 3–4 ──────────────────────────────────────

def compute_distance_to_landing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute Euclidean distance from each player to the ball landing spot.
    Uses ball_land_x, ball_land_y from input data.
    """
    df = df.copy()
    df["dist_to_landing"] = np.sqrt(
        (df["x"] - df["ball_land_x"]) ** 2 +
        (df["y"] - df["ball_land_y"]) ** 2
    )
    return df


def compute_closing_speed(df: pd.DataFrame) -> pd.DataFrame:
    """
    Project player velocity onto the vector pointing toward ball landing spot.
    Positive = moving toward landing spot, negative = moving away.
    """
    # TODO: implement in Week 4
    raise NotImplementedError


def compute_separation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Distance between targeted receiver and nearest defender at time of throw.
    """
    # TODO: implement in Week 4
    raise NotImplementedError


def build_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Master function: apply all feature transforms and return model-ready DataFrame.
    """
    df = compute_distance_to_landing(df)
    # Add more transforms here as implemented
    return df
