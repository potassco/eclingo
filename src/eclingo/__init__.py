"""
This package contains tools for solving epistemic logic programs
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("eclingo")
    if __version__ is None:
        __version__ = "0.0.0"
except Exception:
    __version__ = "0.0.0"
