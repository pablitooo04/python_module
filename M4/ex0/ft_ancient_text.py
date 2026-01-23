file = "ancient_fragment.txt"

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault {file}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    fd = open(file, 'r')
    content = fd.read()
    print(content)
    fd.close()
    print("Data recovery complete. Storage unit disconnected.")
