# Sample script to run ns-3 5G simulation
import os

print("Starting 5G Network Simulation...")
os.system("./waf --run 'lte-simple'")
print("Simulation completed.")
