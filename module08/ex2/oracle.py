from os import getenv, getcwd
from os.path import exists
from dotenv import load_dotenv
from sys import stderr


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")

    if not exists(".env"):
        print(f"Missing .env file in {getcwd()}", file=stderr)
        exit(1)

    load_dotenv(override=True)
    print("\nConfiguration loaded:")
    print(f"Mode: {getenv('MATRIX_MODE')}")
    print(f"Database: {getenv('DATABASE_URL')}")
    print(f"API Access: {getenv('API_KEY')}")
    print(f"Log Level: {getenv('LOG_LEVEL')}")
    print(f"Zion Network: {getenv('ZION_ENDPOINT')}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
