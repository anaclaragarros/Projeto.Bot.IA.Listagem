
from flask import Flask, jsonify
from scraper import get_lenovo_laptops

app = Flask(__name__)

@app.route('/lenovo-laptops', methods=['GET'])
def lenovo_laptops():
    laptops = get_lenovo_laptops()
    return jsonify(laptops)

if __name__ == '__main__':
    app.run(debug=True)
