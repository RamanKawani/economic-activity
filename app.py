from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example data: You can replace this with real economic data or a database later
cities_data = {
    'Baghdad': {'gdp': 3000, 'industry': 'Services', 'population': 8000000},
    'Erbil': {'gdp': 1500, 'industry': 'Oil', 'population': 1500000},
    'Basra': {'gdp': 2000, 'industry': 'Oil', 'population': 2500000},
    'Sulaymaniyah': {'gdp': 1200, 'industry': 'Agriculture', 'population': 600000},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cities')
def get_cities():
    return jsonify(cities_data)

@app.route('/api/city/<name>')
def get_city(name):
    city_info = cities_data.get(name)
    if city_info:
        return jsonify(city_info)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
