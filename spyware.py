import os
import time
import subprocess

# Simulate file drop
with open("dropped_file.txt", "w") as f:
    f.write("This file was dropped by the malware.")

# Simulate execution of another process
subprocess.Popen(["notepad.exe"])  # On Linux, replace with a harmless command

# Simulate delay
time.sleep(3)

# Simulate registry change (Windows only)
try:
    import winreg
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\FakeMalware")
    winreg.SetValueEx(key, "Key", 0, winreg.REG_SZ, "SuspiciousValue")
    winreg.CloseKey(key)
except ImportError:
    pass  # Not on Windows
