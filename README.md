# Week 02 - Morning Briefing App

A command-line app that fetches live weather and news and displays a clean morning briefing in the terminal.

## What it does
- Fetches real-time weather for any city using OpenweatherMap API
- Fetches live news headlines by topic using NewsAPI
- Displays a clean formatted briefing in the terminal

## What I learned
- Classes and object-Oriented Programming in Python
- Making HTTP requests to external APIs using requests library
- Parsing JSON responses and extracting relevant data
- Protecting API keys using .env files
- Reading and diagnosing real API errors (401, SSL, empty responses)
- Default parameters and enumerate() in Python

## APIs Used
- OpenWeatherMap API(free tier)
- NewsAPI(free tier)

## How to run
1. Clone the repo
2. Create a virtual environment and activate it
3. pip install requests python-dotenv
4. Create a .env file with your API keys
5. python main.py
