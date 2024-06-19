import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for happiness")

option_x = st.selectbox("Select data for x axis",
                        ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select data for y axis",
                        ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match option_x:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

match option_y:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]


st.subheader(f"{option_x} and {option_y}")


figure1 = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)

st.write("---")

df2 = pd.read_csv("happy.csv")
df2["happiness"] = df2["happiness"] / 10  # Scale the happiness column

st.subheader("Country Happiness Indicators")

# Dropdown for country selection
country = st.selectbox('Select a country: ', df2['country'].unique())

# Filter data for the selected country
country_data = df2[df2['country'] == country].iloc[0]

# Prepare data for plotting
indicators = ['happiness', 'gdp', 'social_support', 'life_expectancy',
              'freedom_to_make_life_choices', 'generosity', 'corruption']
values = [country_data[i] for i in indicators]

# Create a dataframe for Plotly
plot_data = pd.DataFrame({
    'Indicator': indicators,
    'Value': values})

# Plot using Plotly
figure2 = px.bar(plot_data, x='Indicator', y='Value', title=f'Indicators for {country}')
st.plotly_chart(figure2)