if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print("\nAccessing Storage Vault: ancient\\_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print("Connection established...")
            print("\nRECOVERED DATA:")
            print(file.read())
            print("\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found")
