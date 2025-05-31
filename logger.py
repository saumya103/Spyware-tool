import os
import time

print("Monitoring for changes...")

before = set(os.listdir())

time.sleep(5)  # Wait for malware to act

after = set(os.listdir())
new_files = after - before

if new_files:
    print("[+] New files created:")
    for file in new_files:
        print("   -", file)
else:
    print("[-] No new files detected.")
