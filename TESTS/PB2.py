# simple_progress_bar_module.py

import time
import sys

class CSPB:
    def __init__(self, total_iterations, width=40, char="#"):
        self.total_iterations = total_iterations
        self.width = width
        self.char = char

    def update(self, iteration):
        progress = iteration / self.total_iterations
        bar_width = int(self.width * progress)
        bar = self.char * bar_width + " " * (self.width - bar_width)
        sys.stdout.write(f"\r[{bar}] {int(progress * 100)}%")
        sys.stdout.flush()

def SPB(total_iterations):
    progress_bar = SimpleProgressBar(total_iterations)
    for i in range(total_iterations):
        progress_bar.update(i + 1)
        time.sleep(0.01)  # Simulating some work
    sys.stdout.write("\n")
    sys.stdout.flush()

# Example usage
if __name__ == "__main__":
    SPB(1000)
