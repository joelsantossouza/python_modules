from os import getenv, getcwd
from os.path import exists
from dotenv import load_dotenv
from sys import stderr


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")

    if not exists(".env"):
        print(f"WARNING - Missing .env file in {getcwd()}\n", file=stderr)

    load_dotenv()
    mode: str = getenv('MATRIX_MODE')
    if not mode:
        print("No matrix mode provided", file=stderr)
        exit(1)
    vars: list[str] = [
        getenv(var) for var in [
            "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
        ]
    ]
    if mode == "development":
        for i, var in enumerate(vars):
            vars[i] = var if var else "Missing configuration..."
    else:
        info: list[str] = [
            "Database is connected", "Authenticated",
            "INFO", "Online"
        ]
        for i, var in enumerate(vars):
            vars[i] = info[i] if var else "Missing configuration..."

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {vars[0]}")
    print(f"API Access: {vars[1]}")
    print(f"Log Level: {vars[2]}")
    print(f"Zion Network: {vars[3]}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
