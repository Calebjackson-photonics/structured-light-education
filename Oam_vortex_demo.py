import argparse

import numpy as np
import matplotlib.pyplot as plt


def generate_oam_field(l=1, grid_size=512, extent=10.0):
    """
    Generate a simple optical vortex (OAM) field on a 2D grid.

    Parameters
    ----------
    l : int
        Topological charge (OAM index). Positive / negative values
        correspond to opposite helicities.
    grid_size : int
        Number of points along x and y.
    extent : float
        Physical size of the grid in arbitrary units.

    Returns
    -------
    x, y : 1D arrays
        Coordinate axes.
    phase : 2D array
        Phase profile of the field.
    intensity : 2D array
        Intensity profile |E|^2.
    """
    # Coordinate grid
    x = np.linspace(-extent, extent, grid_size)
    y = np.linspace(-extent, extent, grid_size)
    X, Y = np.meshgrid(x, y)

    # Polar coordinates
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    # Simple vortex-like amplitude envelope:
    # radial factor * Gaussian
    w0 = extent / 2.5
    A = (R / w0) ** abs(l) * np.exp(-(R / w0) ** 2)

    # Complex field with OAM phase term exp(i l theta)
    E = A * np.exp(1j * l * Theta)

    phase = np.angle(E)
    intensity = np.abs(E) ** 2

    return x, y, phase, intensity


def plot_oam(x, y, phase, intensity, l):
    """Plot phase and intensity side by side."""
    extent = [x.min(), x.max(), y.min(), y.max()]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    im0 = axes[0].imshow(
        phase,
        extent=extent,
        origin="lower",
    )
    axes[0].set_title(f"Phase, l = {l}")
    axes[0].set_xlabel("x (arb. units)")
    axes[0].set_ylabel("y (arb. units)")
    fig.colorbar(im0, ax=axes[0], shrink=0.8, label="phase [rad]")

    im1 = axes[1].imshow(
        intensity,
        extent=extent,
        origin="lower",
    )
    axes[1].set_title(f"Intensity, l = {l}")
    axes[1].set_xlabel("x (arb. units)")
    axes[1].set_ylabel("y (arb. units)")
    fig.colorbar(im1, ax=axes[1], shrink=0.8, label="normalized intensity")

    fig.suptitle("Simple Optical Vortex (Textbook OAM Demo)", fontsize=14)
    fig.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Educational demo: optical vortex / OAM beam."
    )
    parser.add_argument(
        "-l",
        "--charge",
        type=int,
        default=1,
        help="Topological charge (OAM index), e.g. -3, -1, 1, 2, ...",
    )
    parser.add_argument(
        "--grid",
        type=int,
        default=512,
        help="Grid size (number of points along each axis).",
    )
    parser.add_argument(
        "--extent",
        type=float,
        default=10.0,
        help="Half-size of the simulation window (arb. units).",
    )

    args = parser.parse_args()

    x, y, phase, intensity = generate_oam_field(
        l=args.charge, grid_size=args.grid, extent=args.extent
    )
    plot_oam(x, y, phase, intensity, l=args.charge)


if __name__ == "__main__":
    main()
