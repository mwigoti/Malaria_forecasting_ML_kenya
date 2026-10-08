"""Evaluation utilities for forecasting and model comparison."""

from __future__ import annotations


def evaluate_model(model, X_test, y_test):
    """Compute evaluation metrics for a fitted model."""
    raise NotImplementedError("Implement train/test evaluation logic here.")


def summarize_metrics(metrics):
    """Return a compact summary dictionary of model metrics."""
    raise NotImplementedError("Implement metrics summarization here.")
