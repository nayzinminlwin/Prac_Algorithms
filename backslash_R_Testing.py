import time

for i in range(10):
    print(f"\rCounting: {i}", end="", flush=True)  # Overwrite the same line
    time.sleep(0.5)

print("\nDone!")  # Move to the next line after finishing
