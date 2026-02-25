from pathlib import Path


def create_gallery(output_dir: Path):
    """
    Create structured HTML gallery grouped by model.
    """

    png_files = sorted(output_dir.glob("*.png"))
    csv_files = sorted(output_dir.glob("*.csv"))

    models = {}

    # Organize files by model name
    for file in png_files:
        name = file.stem.split("_")[0]
        models.setdefault(name, {})
        models[name][file.stem.replace(name + "_", "")] = file.name

    for file in csv_files:
        name = file.stem.split("_")[0]
        models.setdefault(name, {})
        models[name]["csv"] = file.name

    html = """
    <html>
    <head>
        <title>TARDIS Spectrum Gallery</title>
        <style>
            body { font-family: Arial; background: #f4f4f4; padding: 20px; }
            h1 { text-align: center; }
            .model { background: white; padding: 20px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            img { width: 100%; max-width: 900px; margin-bottom: 20px; }
            a { display: inline-block; margin-top: 10px; }
        </style>
    </head>
    <body>
        <h1>TARDIS Simulation Gallery</h1>
    """

    for model_name, files in models.items():
        html += f"<div class='model'>"
        html += f"<h2>{model_name}</h2>"

        if "spectrum" in files:
            html += f"<h3>Spectrum</h3>"
            html += f"<img src='{files['spectrum']}'><br>"

        if "sdec" in files:
            html += f"<h3>SDEC Plot</h3>"
            html += f"<img src='{files['sdec']}'><br>"

        if "liv" in files:
            html += f"<h3>LIV Plot</h3>"
            html += f"<img src='{files['liv']}'><br>"

        if "csv" in files:
            html += f"<a href='{files['csv']}' download>Download CSV Data</a>"

        html += "</div>"

    html += "</body></html>"

    gallery_path = output_dir / "gallery.html"

    with open(gallery_path, "w") as f:
        f.write(html)

    print(f"Gallery updated at {gallery_path}")