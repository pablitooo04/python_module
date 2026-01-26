content = """\
[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        f = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        print(content, end="\n\n")
        f.write(content)
    except Exception:
        print("Error creating the archive!")
    else:
        f.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
