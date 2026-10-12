"""Smoke checks for the installed package."""

from importlib.metadata import distribution

import scan_to_swarm


def test_installed_package() -> None:
    """The source package is importable and has installed distribution metadata."""
    assert scan_to_swarm.__name__ == "scan_to_swarm"
    metadata = distribution("scan-to-swarm").metadata
    assert metadata["Name"] == "scan-to-swarm"
    assert metadata["Version"]
