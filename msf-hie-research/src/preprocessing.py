"""Data preprocessing utilities for the MSF HIE research workflow."""

from __future__ import annotations

from typing import Iterable


def load_data(path: str):
    """Load a dataset from disk."""
    raise NotImplementedError("Implement dataset loading logic for the target source.")


def clean_data(data):
    """Standardize column names and handle missing values."""
    raise NotImplementedError("Implement cleaning and validation logic here.")


def validate_schema(data, required_columns: Iterable[str]):
    """Ensure the required schema is present before modeling."""
    missing = [col for col in required_columns if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return True
