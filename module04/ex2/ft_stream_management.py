import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    try:
        id: str = input("\nInput Stream active. Enter archivist ID: ")
        stats: str = input("Input Stream active. Enter status report: ")
    except KeyboardInterrupt:
        print("\nAn error occured, try again", file=sys.stderr)
    else:
        print(f"\n{{[}}STANDARD{{]}} Archive status from {id}: {stats}")
        print(
            "{[}ALERT{]} System diagnostic: Communication channels verified",
            file=sys.stderr
        )
        print("{[}STANDARD{]} Data transmission complete")

        print("\nThree-channel communication test successful.")
