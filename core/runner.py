from pathlib import Path
import sys

from tardis import run_tardis

from core.plotter import save_spectrum, save_sdec, save_liv
from core.gallery import create_gallery


def run_simulation(config_path: Path, output_dir: Path):
    """
    Run a TARDIS simulation for a given YAML configuration file
    and save spectrum, SDEC, and LIV plots.
    """

    print(f"\nRunning simulation for: {config_path}")

    simulation = run_tardis(config_path, show_progress_bars=False)

    # Save plots
    save_spectrum(simulation, output_dir, config_path.stem)
    save_sdec(simulation, output_dir, config_path.stem)
    save_liv(simulation, output_dir, config_path.stem)

    print(f"Finished processing: {config_path.stem}")


if __name__ == "__main__":

    # If user provides models folder path
    if len(sys.argv) > 1:
        models_dir = Path(sys.argv[1])
    else:
        models_dir = Path("models")

    if not models_dir.exists():
        print(f"Models folder not found: {models_dir}")
        sys.exit(1)

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    config_files = list(models_dir.glob("*.yml"))

    if not config_files:
        print("No YAML configuration files found.")
        sys.exit(1)

    for config_file in config_files:
        run_simulation(config_file, output_dir)

    create_gallery(output_dir)

    print("\nAll models processed successfully.")