from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "29075347victor"  # Substitua pela sua chave de API

@app.route('/data', methods=['GET'])
def get_data():
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    pollution_data = {
        "temperature": {
            "value": 26.3,
            "unit": "C"
        },
        "dissolved_oxygen": {
            "value": 6.4,
            "unit": "mg/L"
        },
        "salinity": {
            "value": 35.1,
            "unit": "ppt"
        },
        "turbidity": {
            "value": 3.5,
            "unit": "NTU"
        },
        "microplastics": {
            "value": 150,
            "unit": "particles/m^3"
        }
    }

    return jsonify(pollution_data)

if __name__ == '__main__':
    app.run(debug=True)
