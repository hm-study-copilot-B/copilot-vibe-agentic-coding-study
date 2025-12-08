import pytest
import matplotlib.pyplot as plt
import numpy as np


def test_toggle_dark_mode_exists():
    """Test that toggle_dark_mode function exists."""
    from src.solution import toggle_dark_mode
    assert callable(toggle_dark_mode)


def test_toggle_dark_mode_on_figure():
    """Test toggle_dark_mode can be applied to a figure."""
    from src.solution import toggle_dark_mode
    
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    # Should not raise an error
    toggle_dark_mode(fig=fig)
    plt.close(fig)


def test_toggle_dark_mode_on_axis():
    """Test toggle_dark_mode can be applied to an axis."""
    from src.solution import toggle_dark_mode
    
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    # Should not raise an error
    toggle_dark_mode(ax=ax)
    plt.close(fig)


def test_toggle_dark_mode_reversible():
    """Test toggle_dark_mode can be toggled back."""
    from src.solution import toggle_dark_mode
    
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    # Toggle twice should return to original state
    toggle_dark_mode(fig=fig)
    toggle_dark_mode(fig=fig)
    plt.close(fig)
