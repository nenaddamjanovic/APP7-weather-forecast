import requests
import streamlit as st
import sqlite3

# Access API key from secrets
api_key = st.secrets["default"]["API_KEY"]


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    np_values = 8 * days
    filtered_data = filtered_data[:np_values]
    return filtered_data

# Function to create the database and table
def create_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            place TEXT,
            dt TEXT,
            temp REAL,
            pressure INTEGER,
            humidity INTEGER,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Function to insert data into the database
def insert_data(data, place):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()

    for entry in data:
        dt = entry["dt_txt"]
        temp = int(entry["main"]["feels_like"]) - 273.15
        pressure = entry["main"]["pressure"]
        humidity = entry["main"]["humidity"]
        description = entry["weather"][0]["description"]

        c.execute('''
            INSERT INTO weather (place, dt, temp, pressure, humidity, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (place, dt, temp, pressure, humidity, description))

    conn.commit()
    conn.close()


#  Da probamo dal radi funkcija
if __name__ == "__main__":
    filtered_data = get_data(place="Tokyo", days=3)
    print(filtered_data)
    # Create the database and table
    create_db()
    # Insert the data into the database
    insert_data(filtered_data)