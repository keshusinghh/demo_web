import streamlit as  st

name = st.text_input("Enter Your Name")
fname = st.text_input("Enter Your Father's Name")
adr = st.text_area("Enter Your Text")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6,))

button = st.button("Done")
if button:
    st.success(f"Your Name is {name}")
    st.success(f"Your Father's Name is {fname}")
    st.success(f"Your Text is {adr}")
    st.success(f"Your Class is {classdata}")