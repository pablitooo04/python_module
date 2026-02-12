import os

print("\nLOADING STATUS: Loading programs...\n")

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    print("Error: Could not import importlib module !")
    exit(1)


def main() -> None:
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/" \
        "summary/all_day.geojson"

    print("Analyzing Matrix data...")
    data = requests.get(url).json()
    features = data["features"]
    subset = features[:10]

    print("Processing 1000 data points...")
    df = pd.json_normalize(subset)
    magnitudes = df["properties.mag"]
    magnitudes = np.array(magnitudes)

    places = df["properties.place"]

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(range(len(magnitudes)), magnitudes, color="red")
    ax.set_xticks(range(len(places)))
    ax.set_xticklabels(places, rotation=20, ha="right", fontsize=5)
    ax.set_ylabel("Magnitude")
    ax.set_title("Magnitudes of the last 10 earthquakes (USGS - last day)")

    os.makedirs("matrix", exist_ok=True)
    fig.savefig("matrix/data.png", dpi=200)

    print()

    print("Analysis complete!")
    print("Results saved to: matrix/data.png")


if __name__ == "__main__":
    import_status = True
    print("Checking dependencies:")

    try:
        import numpy as np
    except ImportError:
        print("[\033[91mKO\033[0m] numpy not found !")
        import_status = False
    else:
        try:
            v = getattr("numpy", "__version__", version("numpy"))
        except PackageNotFoundError:
            v = "unknown"
        print(
            f"[\033[92mOK\033[0m] numpy ({v}) - Scientific manipulation ready")

    try:
        import pandas as pd
    except ImportError:
        print("[\033[91mKO\033[0m] pandas not found !")
        import_status = False
    else:
        try:
            v = getattr("pandas", "__version__", version("pandas"))
        except PackageNotFoundError:
            v = "unknown"
        print(f"[\033[92mOK\033[0m] pandas ({v}) - Data manipulation ready")

    try:
        import requests
    except ImportError:
        print("[\033[91mKO\033[0m] requests not found !")
        import_status = False
    else:
        try:
            v = getattr("requests", "__version__", version("requests"))
        except PackageNotFoundError:
            v = "unknown"
        print(f"[\033[92mOK\033[0m] requests ({v}) - Network access ready")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("[\033[91mKO\033[0m] matplotlib not found !")
        import_status = False
    else:
        try:
            v = getattr("matplotlib", "__version__", version("matplotlib"))
        except PackageNotFoundError:
            v = "unknown"
        print(f"[\033[92mOK\033[0m] matplotlib ({v}) - Visualization ready")

    print()

    if not import_status:
        print("Error: Missing dependencies !", end="")
        print("Please install the required packages\n")
        print(">>> pip install -r requirements.txt")
        print(">>> poetry install; poetry run python loading.py")
        exit(1)

    main()
