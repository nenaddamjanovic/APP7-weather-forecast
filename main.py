import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")

# Add title, input, slide, selectbox and subheader
st.title("Weather forecast for next days")
place = st.text_input("Place: ", value="Pancevo")
days = st.slider("Forecast days",
                 min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Pressure", "Humidity", "Windspeed", "Sky", "Sky-detailed" ))
st.header(f"{option} for the next {days} days in {place.title()}")

if place:
    # Get the temp/sky data
    filtered_data = get_data(place, days)

    # Create temperature plot
    if option == "Temperature":
        temperature = [int(dict["main"]["feels_like"]) - 273.15 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure, theme="streamlit")

    # Create Pressure plot
    if option == "Pressure":
        pressure = [int(dict["main"]["pressure"]) for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=pressure, labels={"x": "Date", "y": "Pressure (Millibar)"})
        st.plotly_chart(figure, theme="streamlit")

    # Create Humidity plot
    if option == "Humidity":
        humidity = [int(dict["main"]["humidity"]) for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=humidity, labels={"x": "Date", "y": "Humidity (%)"})
        st.plotly_chart(figure, theme="streamlit")

    # Create Windspeed plot
    if option == "Windspeed":
        wind = [int(dict["wind"]["speed"]) for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=wind, labels={"x": "Date", "y": "Windspeed (kmh)"})
        st.plotly_chart(figure, theme="streamlit")

    # Create Sky plot
    elif option == "Sky":
        images = {"Clear": "images/clear_sky.png",
                  "Clouds": "images/few_clouds.png",
                  "Rain": "images/moderate_rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        dates = [dict["dt_txt"] for dict in filtered_data]
        st.image(image_paths, width=88, caption=dates)

    # Create Sky-detailed plot
    elif option == "Sky-detailed":
        images = {"clear sky": "images/clear_sky.png",
                  "few clouds": "images/few_clouds.png",
                  "scattered clouds": "images/scattered_clouds.png",
                  "broken clouds": "images/broken_clouds.png",
                  "overcast clouds": "images/overcast_clouds.png",
                  "light rain": "images/light_rain.png",
                  "moderate rain": "images/moderate_rain.png",
                  "heavy intensity rain": "images/heavy_intensity_rain.png",
                  "light snow": "images/light_snow.png",
                  "snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["description"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create captions by combining sky conditions and dates
        captions = [f"{condition}\n{date}" for condition, date in
                    zip(sky_conditions, dates)]
        st.image(image_paths, width=88, caption=captions)

