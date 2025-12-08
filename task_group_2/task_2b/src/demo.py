"""
Demo script for dark mode toggle in Matplotlib.
Run this to see the dark mode in action.
"""

from solution import toggle_dark_mode
import matplotlib.pyplot as plt
import numpy as np


def demo_dark_mode():
    """Demo: Toggle dark mode on a simple plot."""
    # Create a sample plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label='sin(x)')
    ax.set_title('Dark Mode Toggle Demo')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.legend()
    ax.grid(True)
    
    print("Showing light mode...")
    plt.show(block=False)
    plt.pause(2)
    
    # Toggle to dark mode
    print("Toggling to dark mode...")
    toggle_dark_mode(fig=fig)
    plt.draw()
    plt.pause(2)
    
    # Toggle back to light mode
    print("Toggling back to light mode...")
    toggle_dark_mode(fig=fig)
    plt.draw()
    plt.pause(2)
    
    plt.close()
    print("Demo complete!")


if __name__ == "__main__":
    print("Dark Mode Toggle Demo")
    print("=" * 40)
    demo_dark_mode()
