"""Spatial analysis tooling for hotspot and accessibility workflows."""

from __future__ import annotations


def compute_hotspots(data, target_column: str = "case_count"):
    """Identify hotspot regions or clusters based on incidence intensity."""
    raise NotImplementedError("Implement hotspot detection logic here.")


def compute_accessibility(data):
    """Estimate access or travel-time-related estimates for populations."""
    raise NotImplementedError("Implement healthcare-accessibility logic here.")
