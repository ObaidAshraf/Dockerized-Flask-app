import os
from flask import Flask, request
from getWeather import getCityWeather

app = Flask(__name__)
PORT=5000

@app.route("/")
def index():
    return "Invalid format."

@app.route("/weather")
def login():
    city = request.args.get('city', '')
    if (city != ""):
        try:
            return getCityWeather(city)
        except:
            return "Unexpected error."
    return "Invalid format."

if (os.environ and os.environ.get("PORT")):
	PORT = int( os.environ.get("PORT") )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
