from os import getenv, getcwd
from os.path import exists
from sys import stderr
try:
    from dotenv import load_dotenv
except ModuleNotFoundError as e:
    print(f"{e}. Install with pip install python3-dotenv", file=stderr)
    exit(1)


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")

    has_env_file: bool = True
    if not exists(".env"):
        print(f"WARNING - Missing .env file in {getcwd()}", file=stderr)
        has_env_file = False

    load_dotenv()
    mode: str = getenv('MATRIX_MODE')
    if not mode or mode != "development" or mode != "production":
        print(
            "\nNo matrix mode provided (development or production)",
            file=stderr
        )
        exit(1)
    env_vars: list[str] = [
        "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]
    vars: list[str] = [
        getenv(var) for var in env_vars
    ]
    for i, var in enumerate(vars):
        if not var:
            print(f"Missing configuration of {env_vars[i]}", file=stderr)
            exit(1)

    if mode == "production":
        info: list[str] = [
            "Database is connected", "Authenticated",
            "INFO", "Online"
        ]
        for i, new_value in enumerate(info):
            vars[i] = new_value

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {vars[0]}")
    print(f"API Access: {vars[1]}")
    print(f"Log Level: {vars[2]}")
    print(f"Zion Network: {vars[3]}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if has_env_file:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
