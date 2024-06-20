import requests

API_KEY = "339a12e2986c2973874900f6012d781c"


def get_data(f_place, f_days=None, f_option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={f_place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    print(f"Complete filtered data:\n{filtered_data}")
    np_values = 8 * f_days
    filtered_data = filtered_data[:np_values]
    print(f"Complete filtered data for number of days:\n{filtered_data}")

    if f_option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        print(f"Temp filtered_data is:\n{filtered_data}")
    if f_option == "Sky":
        # filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        # Dodajemo i objašnjenje vrste vremena
        filtered_data = [(dict["weather"][0]["main"], dict["weather"][0]["description"]) for dict in filtered_data]
        print(f"Sky filtered_data is:\n{filtered_data}")
    return filtered_data


#  Da probamo dal radi funkcija
if __name__ == "__main__":
    print(get_data(f_place="Tokyo", f_days=3, f_option="Sky"))
