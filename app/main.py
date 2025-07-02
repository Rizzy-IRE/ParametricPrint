import streamlit as st
from prompts import generate_script
import os

st.title("🛠️ ParametricPrint")
st.subheader("Generate OpenSCAD scripts with AI")

desc = st.text_area("📝 Describe your part (e.g., 'a customizable electronics box with vents')")

if st.button("Generate CAD Script"):
    with st.spinner("Generating..."):
        script = generate_script(desc)
        with open("output/output.scad", "w") as f:
            f.write(script)
        st.code(script, language="scad")
        st.download_button("📥 Download .scad", script, file_name="parametric_model.scad")
