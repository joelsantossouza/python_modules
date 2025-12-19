if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print("\nAccessing Storage Vault: ancient\\_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print(file.read())
    except Exception as e:
        print(f"[ERROR] {e}")
