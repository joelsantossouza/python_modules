if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    try:
        print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            pass
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as file:
            pass
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            print("SUCCESS: Archive recovered - ``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
