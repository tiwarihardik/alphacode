import os
import fnmatch
from os import system, name
from colorama import init, Fore, Back, Style
from tqdm import tqdm
import time
import pandas as pd

# Initialize colorama
init()

#Function to clear the cli screen
def clear():
    system("cls" if name == "nt" else "clear")

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            return os.path.join(root, filename)
    return None

# Example usage
codefile = input("Code program to run: ")
directory = './'
pattern = f'{codefile}.code'  # Change this to your desired file pattern

file_path = find_files(directory, pattern)
if file_path:
    clear()
    print(Fore.GREEN + "Valid Program" + Fore.RESET)
    
    # Simulate loading with a progress bar
    for i in tqdm(range(100)):
        time.sleep(0.05)  # Simulate a task
    
    # Execute the code file
    execute(file_path)
else:
    print(Fore.RED + "File not found" + Fore.RESET)
