"""
data_loader.py
--------------
Utilities for loading and merging the Big Data Bowl 2026 CSVs.

Usage:
    from src.data_loader import load_week, load_all_weeks, load_supplementary

Data lives in data/raw/train/ — never committed to git.
"""

import os
import glob
import pandas as pd
from tqdm import tqdm

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
TRAIN_DIR = os.path.join(RAW_DIR, "train")
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")


def load_week(week: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load input and output CSVs for a single week.

    Returns
    -------
    input_df : pd.DataFrame
        Tracking data BEFORE the pass is thrown.
    output_df : pd.DataFrame
        Tracking data AFTER the pass is thrown.
    """
    week_str = str(week).zfill(2)
    input_path = os.path.join(TRAIN_DIR, f"input_2023_w{week_str}.csv")
    output_path = os.path.join(TRAIN_DIR, f"output_2023_w{week_str}.csv")

    input_df = pd.read_csv(input_path)
    output_df = pd.read_csv(output_path)

    # Tag with week number for CV splits later
    input_df["week"] = week
    output_df["week"] = week

    return input_df, output_df


def load_all_weeks(weeks: list[int] = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load and concatenate input/output data across all (or specified) weeks.

    Parameters
    ----------
    weeks : list of int, optional
        Weeks to load. Defaults to 1–18.

    Returns
    -------
    all_input, all_output : pd.DataFrame
    """
    if weeks is None:
        weeks = list(range(1, 19))

    inputs, outputs = [], []
    for week in tqdm(weeks, desc="Loading weeks"):
        try:
            inp, out = load_week(week)
            inputs.append(inp)
            outputs.append(out)
        except FileNotFoundError:
            print(f"  [WARNING] Week {week} file not found, skipping.")

    return pd.concat(inputs, ignore_index=True), pd.concat(outputs, ignore_index=True)


def load_supplementary() -> pd.DataFrame:
    """Load the supplementary contextual data."""
    path = os.path.join(RAW_DIR, "supplementary.csv")
    return pd.read_csv(path)


def merge_all(input_df: pd.DataFrame,
              output_df: pd.DataFrame,
              supplementary_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge input, output, and supplementary on game_id + play_id.

    Note: output_df is aggregated to play level before merging
    (last frame position per player as endpoint).
    """
    # Supplementary is at play level — merge onto input
    merged = input_df.merge(
        supplementary_df,
        on=["game_id", "play_id"],
        how="left"
    )

    return merged


if __name__ == "__main__":
    # Quick smoke test
    print("Loading week 1...")
    inp, out = load_week(1)
    print(f"  Input shape:  {inp.shape}")
    print(f"  Output shape: {out.shape}")

    sup = load_supplementary()
    print(f"  Supplementary shape: {sup.shape}")
    print("Done.")
