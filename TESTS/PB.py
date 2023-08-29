from tqdm import tqdm
import time

total_phases = 4

progress_bar = tqdm(total=total_phases, desc="Server Boot Phases", unit="phase")

phases = ["Initializing", "Loading Modules", "Configuring", "Finalizing"]

for phase in phases:
    # Update the description to show the current phase
    progress_bar.set_description(f"Server Boot: {phase}")
    progress_bar.update(1)

progress_bar.close()

print("Server boot completed!")

def n()
    progress_bar.update(1)
