TARDIS Setups Plot Gallery
An automated visualization pipeline developed for the **GSoC 2026 project idea**: "TARDIS Setups Generated Plots and Gallery". This tool streamlines the process of running supernova simulations and comparing results through an automatically generated web dashboard.

🚀 Overview
This project automates the workflow for researchers using TARDIS. Instead of manually running simulations and plotting results one by one, this tool scans a directory of models, executes the simulations, and compiles a comprehensive visual gallery.

✨ Features
Automated Batch Processing: Scans the models/ directory for .yml configuration files and runs them in sequence.

Comprehensive Visualization: Automatically generates three types of plots for every model:

Standard Spectrum: Visualizes luminosity density across wavelengths.

SDec (Spectral element DEComposition): Identifies chemical element contributions to the spectrum.

LIV (Line Interaction Visualization): Shows photon-line interactions.

Data Export: Saves raw simulation data into .csv files for deep-dive scientific analysis.

Web Dashboard: Automatically generates a responsive gallery.html to view and compare all results in a single browser view.

Modular Architecture: Organized into core/ (logic), models/ (inputs), and outputs/ for professional software maintainability.

🛠️ Project Structure
Plaintext
tardis-plot-gallery/
├── core/
│   ├── scanner.py   # Scans for model files
│   ├── runner.py    # Main simulation execution logic
│   └── plotter.py   # Custom plotting functions (Matplotlib/TARDIS)
├── models/          # Input .yml configuration files
├── outputs/         # Generated PNGs, CSVs, and HTML gallery
└── main.py          # Entry point for the pipeline
⚙️ Installation & Usage
Prerequisites
Python 3.13 (Recommended for TARDIS stability)

Conda / Miniconda

Setup
Clone the repository:

Bash
git clone https://github.com/mParmar09/tardis-plot-gallery.git
cd tardis-plot-gallery
Create and activate the environment:

Bash
conda create -n tardis_env python=3.10
conda activate tardis_env
conda install -c tardis-sn tardis
Running the Pipeline
Place your .yml files in the models/ folder and run:

Bash
python -m core.runner
Once finished, open outputs/gallery.html in your browser to view the results.

📈 Future Roadmap
[ ] Integration with the official tardis-setups repository.

[ ] Support for interactive Plotly widgets in the HTML gallery.

[ ] Metadata extraction (Temperature, Velocity) to display alongside plots.

[ ] GitHub Actions pipeline for automated gallery updates on new submissions.
