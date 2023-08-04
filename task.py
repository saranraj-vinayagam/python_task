import json

def get_weather_data(file_path):
    try:
        with open('jsonfile\sample.json', 'r') as file:
            return json.load(file)['list']
    except FileNotFoundError:
        print("Failed to open weather data file.")
        return None

def get_weather_by_date(weather_data, date):
    for forecast in weather_data:
        if date in forecast['dt_txt']:
            return forecast['weather'][0]['description']
    return None

def get_wind_speed_by_date(weather_data, date):
    for forecast in weather_data:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for forecast in weather_data:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None

def main():
    file_path = 'weather_data.json'
    weather_data = get_weather_data(file_path)

    if weather_data is None:
        print("Exiting program due to data loading error.")
        return

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            weather = get_weather_by_date(weather_data, date)
            if weather is not None:
                print(f"Weather on {date}: {weather}")
            else:
                print("Weather data not found for the given date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Wind speed data not found for the given date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Pressure data not found for the given date.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
