if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURIY SYSTEM ===")

    print("\nInitiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols")

            print("\nSECURE EXTRACTION:")
            print(file.read())

        with open("new_classified_data.txt", "w") as file:
            print("\nSECURE PRESERVATION:")
            text: str = "{[}CLASSIFIED{]} New security protocols archived"
            file.write(text)
            print(text)

        print("Vault automatically sealed upon completion")

        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(f"ERROR: {e}")
