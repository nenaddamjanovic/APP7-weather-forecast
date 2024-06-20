import requests
import streamlit as st

# Access API key from secrets
api_key = st.secrets["default"]["API_KEY"]

def get_data(place, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    np_values = 8 * days
    filtered_data = filtered_data[:np_values]
    return filtered_data

    # if option == "Sky":
    #    filtered_data = [(dict["weather"][0]["main"], dict["weather"][0]["description"]) for dict in filtered_data]


#  Da probamo dal radi funkcija
if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, option="Sky"))
