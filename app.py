import os
import joblib
import steamlit as st

# Debugging code
file_path = 'preprocessor.pkl'
if not os.path.exists(file_path):
    st.error(f"File not found: {os.path.abspath(file_path)}")
else:
    try:
        p = joblib.load(file_path)
        st.success("Preprocessor loaded successfully!")
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
