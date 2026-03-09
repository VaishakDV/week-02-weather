from weather import WeatherService
from news import NewsService

def display_briefing(weather, headlines):
    print("\n" + "="*50)
    print("          YOUR MORNING BRIEFING")
    print("="*50)

    print(f"\n {weather['city']}")
    print(f" Temperature : {weather['temperature']}°C")
    print(f" Feels like : {weather['feels_like']}°C")
    print(f" Condition : {weather['condition'].title()}")
    print(f" Humidity : {weather['humidity']}%")

    print("\n"+"-"*50)
    print("   TOP HEADLINES")
    print("-"*50)

    for i, article in enumerate(headlines, start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   -{article['source']}")

    print("\n"+"="*50+"\n")

def main():
    print("\nFetching your morning briefing...")

    weather_service = WeatherService()
    news_service = NewsService()

    weather = weather_service.get_weather("Bengaluru")
    headlines = news_service.get_headlines()

    display_briefing(weather, headlines)

if __name__ == "__main__":
    main()