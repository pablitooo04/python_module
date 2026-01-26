if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", 'r') as f:
            pass
    except (FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
    except (PermissionError):
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as f:
            pass
    except (FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
    except (PermissionError):
        print("RESPONSE: Security protocols deny access")
    
    print("STATUS: Crisis handled, security maintained")
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", 'r') as f:
            print(f"SUCCESS: Archive recovered - ``{f.read()}``")
    except (FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
    except (PermissionError):
        print("RESPONSE: Security protocols deny access")
    
    print("All crisis scenarios handled successfully. Archives secure.")