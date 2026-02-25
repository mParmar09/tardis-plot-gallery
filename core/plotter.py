from pathlib import Path
import matplotlib.pyplot as plt

from tardis.visualization.tools.sdec_plot import SDECPlotter
from tardis.visualization.tools.liv_plot import LIVPlotter


def save_spectrum(simulation, output_dir: Path, name: str):
    """
    Save synthetic spectrum as PNG and CSV.
    """

    spectrum = simulation.spectrum_solver.spectrum_integrated

    wavelength = spectrum.wavelength.value
    luminosity = spectrum.luminosity_density_lambda.value

    # ----- Save PNG -----
    plt.figure(figsize=(8, 5))
    plt.plot(wavelength, luminosity)
    plt.xlabel("Wavelength (Angstrom)")
    plt.ylabel("Luminosity Density")
    plt.title("Synthetic Spectrum")
    plt.grid(True)

    png_path = output_dir / f"{name}_spectrum.png"
    plt.savefig(png_path)
    plt.close()

    print(f"Spectrum PNG saved to {png_path}")

    # ----- Save CSV -----
    csv_path = output_dir / f"{name}_spectrum.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        f.write("wavelength,luminosity_density\n")
        for w, l in zip(wavelength, luminosity):
            f.write(f"{float(w)},{float(l)}\n")

    print(f"Spectrum CSV saved to {csv_path}")


def save_sdec(simulation, output_dir: Path, name: str):
    """
    Save SDEC plot as PNG.
    """

    sdec_plotter = SDECPlotter.from_simulation(simulation)
    ax = sdec_plotter.generate_plot_mpl(packets_mode="real")

    fig = ax.get_figure()

    path = output_dir / f"{name}_sdec.png"
    fig.savefig(path)
    plt.close(fig)

    print(f"SDEC plot saved to {path}")


def save_liv(simulation, output_dir: Path, name: str):
    """
    Save LIV plot as PNG.
    """

    liv_plotter = LIVPlotter.from_simulation(simulation)
    ax = liv_plotter.generate_plot_mpl()

    fig = ax.get_figure()

    path = output_dir / f"{name}_liv.png"
    fig.savefig(path)
    plt.close(fig)

    print(f"LIV plot saved to {path}")