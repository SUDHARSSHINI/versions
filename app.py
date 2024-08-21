import streamlit as st
import subprocess

def get_versions():
    try:
        result = subprocess.run(['python', 'check_versions.py'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"

st.title("Package Versions Check")
versions_output = get_versions()
st.code(versions_output)
