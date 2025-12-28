import importlib

URL_42 = "https://www.42porto.com/pt/"

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")

    # Trying to import pandas at runtime...
    print("\nChecking dependencies:")
    try:
        pandas = importlib.import_module("pandas")
        DataFrame = pandas.DataFrame
        print(
            f"[OK] pandas {pandas.__version__} - Data manipulation ready"
        )
        requests = importlib.import_module("requests")
        Response = requests.models.Response
        print(
            f"[OK] requests {requests.__version__} - Network access ready"
        )
        matplot = importlib.import_module("matplotlib")
        print(
            f"[OK] matplotlib {matplot.__version__} - Visualization ready"
        )
    except (ModuleNotFoundError, ImportError) as e:
        print(f"[KO] {e}")
        exit(1)

    print("\nAnalyzing Matrix data...")
    year_profit: dict = {
        "month": range(1, 13),
        "profit": range(12, 0, -1)
    }
    data_frame: DataFrame = DataFrame(year_profit)
    print(data_frame)

    print("\nDoing a request...")
    response: Response = requests.get(URL_42)
    print(f"Response Status: {response.status_code}")
    if response.status_code == 200:
        print(response.text)

    print("\n")
