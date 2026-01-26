content="""\
[CLASSIFIED] New security protocols archived
Vault automatically sealed upon completion
"""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access..")
    with open("classified_data.txt", 'r') as f:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        print(f.read())
    with open("classified_data_write.txt", 'w') as f:
        print("\nSECURE PRESERVATION:")
        f.write(content.strip())
        print(content.strip())
    print("\nAll vault operations completed with maximum security.")
