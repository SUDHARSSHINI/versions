import pandas as pd
import numpy as np
import sklearn
import responsibleai
import aif360
import streamlit as st

def get_versions():
    versions = {
        'pandas': pd.__version__,
        'numpy': np.__version__,
        'scikit-learn': sklearn.__version__,
        'responsibleai': responsibleai.__version__,
        'aif360': aif360.__version__,
        'streamlit': st.__version__
    }
    return versions

st.title("Package Versions Check")
versions = get_versions()
st.write("Installed package versions:")
for package, version in versions.items():
    st.write(f"{package} version: {version}")
