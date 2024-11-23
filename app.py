from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

url = "http://hackapi.rhosigma.tech/api/completion"
api_key = "9a343879-6b43-4d4b-8501-6d506a33a57f"

headers = {
    "X-API-Key": api_key
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')  # Get user input from form

        payload = {
            "system": "Remove stop words from input text. For remaining words, append a context category after each word, separated by '_'. Categories: 'everyday', 'finance_and_banking', 'legal', 'numbers', 'states_and_cities', 'technical', 'health', 'retail', 'travel', 'food', 'living', 'entertainment', 'social', 'proper_noun', 'geography'. Example: Input: 'I am not feeling good in Paris' → Output: 'feeling_health, good_health, Paris_proper_noun'.",
            "user": user_input
        }

        # Send POST request to API
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Will raise an error for bad responses
            result = response.json()  # Get JSON data from the API response
        except requests.exceptions.RequestException as e:
            error_message = f"Error: {str(e)}"

    return render_template('index.html', result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
