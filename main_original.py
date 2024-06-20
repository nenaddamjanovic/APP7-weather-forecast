import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, input, slide, selectbox and subheader
st.title("Weather forecast for next days")
place = st.text_input("Place: ", value="Pancevo")
days = st.slider("Forecast days",
                 min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.header(f"{option} for the next {days} days in {place.title()}")

if place:
    # Get the temp/sky data
    filtered_data = get_data(place, days)

    # Create temperature plot
    if option == "Temperature":
        temperature = [int(dict["main"]["feels_like"]) - 273.15 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C"})
        st.plotly_chart(figure, theme="streamlit")

    # Create Sky plot
    elif option == "Sky":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        dates = [dict["dt_txt"] for dict in filtered_data]
        st.image(image_paths, width=88, caption=dates)


