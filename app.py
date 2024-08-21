import subprocess
import sys
import streamlit as st

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        st.success(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to install {package}: {e}")

# Example package list
packages = ['numpy==2.2.0', 'pandas==2.3.0']

for package in packages:
    install(package)
