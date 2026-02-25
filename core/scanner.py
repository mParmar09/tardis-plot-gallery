
from pathlib import Path


def scan_models(models_dir: Path):
    """
    Scan directory for .yml configuration files.
    Returns list of file paths.
    """
    if not models_dir.exists():
        raise FileNotFoundError(f"{models_dir} does not exist.")

    return list(models_dir.glob("*.yml"))


if __name__ == "__main__":
    # Resolve project root dynamically
    project_root = Path(__file__).resolve().parent.parent
    models_path = project_root / "models"

    files = scan_models(models_path)

    print("Found model files:")
    for f in files:
        print(f)