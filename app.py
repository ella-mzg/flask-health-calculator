from flask import Flask, request, jsonify, render_template
from utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    """
    Endpoint to calculate BMI.
    Accepts JSON data with 'height' (in meters) and 'weight' (in kilograms).
    Returns the calculated BMI.
    """
    data = request.json
    try:
        height = float(data.get('height'))  # Height in meters
        weight = float(data.get('weight'))  # Weight in kilograms
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        bmi_value = calculate_bmi(height, weight)
        return jsonify({"bmi": round(bmi_value, 2)}), 200
    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Invalid input or missing fields. Provide 'height' and 'weight' in JSON format."}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    """
    Endpoint to calculate BMR.
    Accepts JSON data with 'height' (in cm), 'weight' (in kg), 'age', and 'gender'.
    Returns the calculated BMR.
    """
    data = request.json
    try:
        height = float(data.get('height'))  # Height in cm
        weight = float(data.get('weight'))  # Weight in kilograms
        age = int(data.get('age'))  # Age in years
        gender = data.get('gender').lower()  # Gender ('male' or 'female')
        if height <= 0 or weight <= 0 or age <= 0:
            raise ValueError("Height, weight, and age must be positive numbers.")
        if gender not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'.")
        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": round(bmr_value, 2)}), 200
    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Invalid input or missing fields. Provide 'height', 'weight', 'age', and 'gender' in JSON format."}), 400

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

