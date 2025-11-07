import requests

# ✅ Use your free API key here
API_KEY = "62bff59ce1d46efb6ea19a220f5f1767"

def get_weather_forecast(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["description"]
        }
        return forecast
    else:
        print("❌ Failed to fetch weather data")
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        return {"error": "Failed to fetch weather data"}

# ✅ Test block
if __name__ == "__main__":
    forecast = get_weather_forecast("Kolhapur")  # Change city as needed
    print("🌤️ Current Weather:")
    for key, value in forecast.items():
        print(f"{key}: {value}")
