import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List the packages you want to install or update
packages = ['numpy==2.2.0', 'pandas==2.3.0']

for package in packages:
    install(package)
