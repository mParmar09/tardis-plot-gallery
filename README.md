# TARDIS Plot Generation and Gallery Prototype

This project is a prototype implementation of the
"TARDIS Setups Generated Plots and Gallery" **GSoC idea**.

## Features

- Run TARDIS simulations from YAML configuration files
- Generate synthetic spectrum plots
- Generate SDEC (Spectral Element Decomposition) plots
- Generate LIV (Line Interaction Visualization) plots
- Automatically process multiple models
- Automatically generate an HTML gallery of outputs

## Usage

Run all models in the models folder:

    python -m core.runner

Run models from a custom folder:

    python -m core.runner path_to_models_folder

## Notebook Demonstration

The notebook `notebooks/visualization_demo.ipynb`
demonstrates how to:

- Run a simulation
- Visualize spectrum
- Generate SDEC and LIV plots
