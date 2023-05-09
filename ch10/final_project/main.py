import random
from src.f1API import ErgastAPI
from src.weatherAPI import WeatherstackAPI

def main():
    # Create instances of the API proxy classes
    ergast_api = ErgastAPI()
    weatherstack_api = WeatherstackAPI()

    # Get the race schedule for the current season (2023)
    season = random.randint(1950, 2023)
    race_schedule = ergast_api.get_race_schedule(season)
    
    # Select a random race from the schedule
    races = race_schedule["MRData"]["RaceTable"]["Races"]
    random_race = random.choice(races)
    race_location = random_race["Circuit"]["Location"]
    location = f"{race_location['lat']},{race_location['long']}"

    # Get the current weather for the race location
    current_weather = weatherstack_api.get_current_weather(location)

    # Process and print the results
    print(f"Random race: {random_race['raceName']}")
    print(f"Race location: {random_race['Circuit']['circuitName']}")
    print(f"Weather conditions: {current_weather['current']['weather_descriptions'][0]}")
    print(f"Temperature: {current_weather['current']['temperature']}°C")

if __name__ == "__main__":
    main()
