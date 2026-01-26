file = "ancient_fragment.txt"

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file}")
    try:
        fd = open(file, 'r')
        content = fd.read()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
    except Exception:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        fd.close()
        print("\nData recovery complete. Storage unit disconnected.")
