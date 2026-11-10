#AI-assisted section: ChatGPT (GPT-6)
#interface layout and navigation

import streamlit as st

st.set_page_config(
    page_title="MechWar-X",
    layout="wide",
)
st.title("MechWar-X")
st.write("Robo-Rental Management System") #Ask if they like this name lol

tab1, tab2, tab3, tab4 = st.tabs(["Mech Registration", "Client Dashboard", 
"Rental Scheduling", "Maintenance"])

with tab1:
    st.header("Mech Registration")
    st.write("Register new combat mechs here.")

with tab2:
    st.header("Client Dashboard")
    st.write("View, search, and manage client information and records here.")

with tab3:
    st.header("Rental Scheduling")
    st.write("Schedule and manage mech rentals here.")

with tab4:
    st.header("Maintenance")
    st.write("Manage and track mech maintenance schedules and records here.")


