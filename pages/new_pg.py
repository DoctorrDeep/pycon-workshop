import streamlit as st
import pandas as pd
import plotly.express as px

from utils.platform.header import same_old


same_old()


st.title("Now we're cooking!")


left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

st.divider()

left1, middle1, right1 = st.columns(3)
if left1.button("Plain button", use_container_width=True, key="left1"):
    left1.markdown("You clicked the plain button.")
else:
    left1.markdown("Oh no, you no click on the plain old left")
if middle1.button("Emoji button", icon="😃", use_container_width=True, key="middle1"):
    middle1.markdown("You clicked the emoji button.")
else:
    middle1.markdown("Oh no, you no click middle me emoji")
if right1.button("Material button", icon=":material/mood:", use_container_width=True, key="right1"):
    right1.markdown("You clicked the Material button.")
else:
    right1.markdown("Oh no, you no click rightly materials")

st.divider()

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.divider()

if st.button("Aloha", type="secondary"):
    st.write("Ciao")
st.write("Why no Ciao?")

st.divider()

st.badge("Hi")
st.badge("Gas", color="green")
st.badge("#not-a-chef", color="red")

st.divider()

my_code = """
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.platform.header import same_old
same_old()
"""
st.code(my_code, language="javascript")
st.write("Done!!")
