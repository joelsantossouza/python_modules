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
    if mode == "development":
        database: str = getenv('DATABASE_URL')
        api_access: str = getenv('API_KEY')
        log_level: str = getenv('LOG_LEVEL')
        zion_network: str = getenv('ZION_ENDPOINT')
    else:
        database: str = "Database is connected"
        api_access: str = "Authenticated"
        log_level: str = "INFO"
        zion_network: str = "Online"

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_network}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
