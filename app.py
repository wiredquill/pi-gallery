from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # simulate database access or other operations
        raise ValueError("Simulated error for testing")
        return jsonify({"message": "Hello World"})
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

