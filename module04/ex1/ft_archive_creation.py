if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\nInitializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "w") as file:
            print("Storage unit created successfully...")

            print("\nInscribing preservation data...")
            text: str = \
                "{[}ENTRY 001{]} New quantum algorithm discovered\n" \
                "{[}ENTRY 002{]} Efficiency increased by 347%\n" \
                "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
            file.write(text)
            print(text)

            print("Data inscription complete. Storage unit sealed.")
            print(
                "Archive 'new_discovery.txt' ready for long-term preservation."
            )
    except Exception:
        print("ERROR: Could not create storage vault")
