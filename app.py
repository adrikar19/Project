import streamlit as st
    
# page info
st.set_page_config(
    page_title="AI Interview Panel",page_icon="🤖",layout="wide"
)
st.title(":blue[Welcome to] :orange[AI ] :blue[Interview Panel]")
st.text("\n")
st.text("\n")
st.text("\n")
st.subheader(":gray[Topics]")
st.text("\n")
# Topics
col1, col2, Col3 = st.columns(3)
with col1:
    st.page_link("pages/hr.py", label=":rainbow[HR]", icon="✔")
    st.page_link("pages/java.py", label=":rainbow[JAVA]", icon="✔")
with col2:
    st.page_link("pages/dotnet.py", label=":rainbow[.NET]", icon="✔")
    st.page_link("pages/python.py", label=":rainbow[Python]", icon="✔")
with Col3:
    #st.page_link("pages/css.py", label=":rainbow[CSS]", icon="✔")
    st.page_link("pages/english.py", label=":rainbow[ENGLISH]", icon="✔")
    st.page_link("pages/html.py", label=":rainbow[HTML]", icon="✔")

st.caption("Choose any one of the above to proceed")

st.sidebar.title("LogIn")
st.sidebar.text_input("UserId")
st.sidebar.text_input("Password")
st.sidebar.button("submit")
