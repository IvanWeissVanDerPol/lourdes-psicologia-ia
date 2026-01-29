import os

start_dir = r"c:\Users\Alejandro\Documents\Ivan\LourdesBusiness\06-DATOS"

print(f"Scanning {start_dir}...")
for root, dirs, files in os.walk(start_dir):
    print(f"Root: {root}")
    for d in dirs:
        print(f"  Dir: {d}")
    for f in files:
        print(f"  File: {f}")
