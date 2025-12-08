import pytest
import numpy as np


def test_smooth_transition_exists():
    """Test that smooth_transition function exists."""
    from src.solution import smooth_transition
    assert callable(smooth_transition)


def test_transition_plot_state_exists():
    """Test that transition_plot_state function exists."""
    from src.solution import transition_plot_state
    assert callable(transition_plot_state)


def test_easing_functions_exist():
    """Test that easing functions exist."""
    from src.solution import ease_linear, ease_in, ease_out, ease_in_out
    assert callable(ease_linear)
    assert callable(ease_in)
    assert callable(ease_out)
    assert callable(ease_in_out)


def test_smooth_transition_returns_animation():
    """Test that smooth_transition returns an animation object."""
    from src.solution import smooth_transition
    from_data = np.array([1, 2, 3, 4, 5])
    to_data = np.array([5, 4, 3, 2, 1])
    result = smooth_transition(from_data, to_data)
    # Should return an animation or similar object
    assert result is not None
