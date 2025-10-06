"""
viz.py
------
Visualization utilities: field plots, calibration curves, rankings charts.

All figures saved to results/figures/ via save_fig().

Implemented incrementally throughout the project.
"""

import os
import matplotlib.pyplot as plt

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "figures")


def save_fig(name: str, dpi: int = 150) -> None:
    """Save current matplotlib figure to results/figures/."""
    os.makedirs(FIGURES_DIR, exist_ok=True)
    path = os.path.join(FIGURES_DIR, f"{name}.png")
    plt.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Saved: {path}")


def plot_field(ax=None):
    """
    Draw a basic NFL field outline on a matplotlib axis.
    Field: x = 0–120 yards, y = 0–53.3 yards.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 5.33))

    # Field background
    ax.set_facecolor("#4a7c59")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 53.3)

    # Yard lines every 10 yards
    for x in range(10, 111, 10):
        ax.axvline(x, color="white", linewidth=0.5, alpha=0.6)

    # End zones
    ax.axvspan(0, 10, color="#2d5a3d", alpha=0.8)
    ax.axvspan(110, 120, color="#2d5a3d", alpha=0.8)

    ax.set_xlabel("Yards (x)")
    ax.set_ylabel("Width (y)")

    return ax


# TODO: add calibration_curve(), player_heatmap(), defender_rankings_bar() in later weeks
