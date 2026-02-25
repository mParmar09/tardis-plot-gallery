🚀 **TARDIS Plot Generation and Gallery Prototype**

This project is a prototype implementation of the "TARDIS Setups Generated Plots and Gallery" GSoC idea.

It automates the generation of synthetic spectrum plots, SDEC plots, LIV plots, and creates an HTML gallery from multiple TARDIS YAML configuration files.

📌 **Overview**

The TARDIS setups repository contains many YAML configuration files for running simulations. However, it is not straightforward for users to preview the inputs and outputs for each model.

This project provides:

A script to automatically run TARDIS simulations from YAML files

Automatic generation of:

  Synthetic Spectrum plots
  
  SDEC (Spectral Element Decomposition) plots
  
  LIV (Line Interaction Visualization) plots
  
  CSV export of spectral data
  
  Automatic HTML gallery generation for easy browsing
  
  A Jupyter notebook demonstration of the full workflow

✨ **  Features**

  Run TARDIS simulations from YAML configuration files
  
  Generate synthetic spectrum plots (PNG + CSV)
  
  Generate SDEC plots
  
  Generate LIV plots
  
  Automatically process multiple models
  
  Automatically generate an HTML gallery of outputs
  
  Jupyter notebook demonstration of visualization workflow

 
  📂 **Project Structure**

      core/
        runner.py       - Main execution script
        plotter.py      - Spectrum, SDEC, and LIV plot generation
        gallery.py      - HTML gallery builder
        scanner.py      - Scans YAML model files
    
    models/
        YAML configuration files
    
    notebooks/
        visualization_demo.ipynb - Demonstration notebook
    
    outputs/
        Generated plots and gallery (ignored in git)

🛠 **Installation**

Create and activate a Python environment, then install required dependencies:
         
    pip install tardis-sn matplotlib pandas

**if using conda:**

    conda create -n tardis_env python=3.13
    conda activate tardis_env
    pip install tardis-sn matplotlib pandas

▶️ **Usage**

Run all models inside the models/ folder:

    python -m core.runner

**Run models from a custom folder:**

    python -m core.runner path_to_models_folder
    
📓 **After execution:**

Spectrum PNG and CSV files are saved in outputs/

SDEC plots are saved in outputs/

LIV plots are saved in outputs/

An HTML gallery is generated at:   

    outputs/gallery.html

Open gallery.html in your browser to view results


🎯 **Notebook Demonstration**

The notebook notebooks/visualization_demo.ipynb demonstrates:

Running a TARDIS simulation

Generating synthetic spectrum

Generating SDEC plot

Generating LIV plot

Visualization workflow in JupyterLab


📄 **Expected Outcome (GSoC Context)**

This prototype demonstrates:

Automated visualization of TARDIS YAML setups

Multi-model batch processing

Structured plot generation

Basic HTML gallery creation

This aligns with the objective of building a preview and visualization pipeline for TARDIS setup configurations.
    

📄 **License**

MIT License
    
    
