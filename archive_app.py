
import streamlit as st
import pandas as pd

# Load project list
df = pd.read_csv("projects_simple.csv")

st.set_page_config(page_title="Matt's Project Archive", layout="centered")
st.title("📁 Matt's Project Archive")

# Dropdown menu
project_names = df['Project Name'].tolist()
selected = st.selectbox("Select a project", ["-- Select --"] + project_names)

if selected != "-- Select --":
    project = df[df['Project Name'] == selected].iloc[0]
    st.subheader(f"📂 {project['Project Name']}")

    link = project["Google Drive Folder Link"]
    if isinstance(link, str) and link.strip():
        st.markdown(f"[🔗 Open Project Folder]({link})", unsafe_allow_html=True)
    else:
        st.info("🔒 No folder link available yet.")
