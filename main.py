import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for next days")
place = st.text_input("Place: ")

days = st.slider("Forecast days",
                 min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.header(f"{option} for the next {days} days in {place.title()}")


d, t = get_data(f_place, f_days, f_option)


figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (C"})
st.plotly_chart(figure)

