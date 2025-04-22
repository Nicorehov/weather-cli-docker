# Weather CLI App ☁️🌦️

A simple command-line weather application built with Python and Docker.

## Features
- Get current weather by city name
- Uses OpenWeatherMap API
- CLI interface
- Dockerized for easy usage

## Technologies
- Python 3
- `requests` library
- Docker

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/weather-cli-app.git
cd weather-cli-app

Run with Docker:

```bash
docker build -t weather-cli .
docker run --rm weather-cli "London"

API Key
Set your OpenWeatherMap API key as an environment variable:

```bash
set OPENWEATHER_API_KEY=your_api_key_here

Author
Mykyta Oriekhov


This project was created as part of a portfolio.
