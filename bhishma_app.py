import streamlit as st
import subprocess

st.title("🛡️ BHISHMA - Memory Dump Analyzer")

if st.button("Run Volatility (Sample)"):
    plugins = ["pslist", "dlllist"]
    for plugin in plugins:
        st.subheader(f"Plugin: {plugin}")
        result = subprocess.getoutput(f"volatility -f memdump.raw --profile=Win7SP1x64 {plugin}")
        st.code(result)