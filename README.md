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

## Run with Docker

1. Build the image:

```bash
docker build -t weather-cli-app .
Run the container:

bash
Копировать
Редактировать
docker run --rm weather-cli-app "Vienna"
