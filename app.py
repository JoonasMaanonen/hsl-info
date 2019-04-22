from flask import Flask, render_template
import json
import requests

app = Flask(__name__)




@app.route('/')
def index():
    with open('config.json', 'r') as f:
        data = json.load(f)


    return render_template('index.html', bike_stations = data['bikeRentalStations'])

if __name__ == '__main__':
    app.run(debug=True)
