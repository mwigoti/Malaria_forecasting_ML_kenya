"""Feature engineering utilities for forecasting and epidemiological analysis."""

from __future__ import annotations


def make_lag_features(data, lag_steps: int = 3):
    """Create temporal lag features for model training."""
    raise NotImplementedError("Implement lag feature engineering here.")


def build_spatial_features(data, geometry_column: str = "geometry"):
    """Construct spatial features for adjacent-location or cluster-based analysis."""
    raise NotImplementedError("Implement spatial feature creation here.")
