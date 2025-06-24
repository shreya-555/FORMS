from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend calls

@app.route("/api/submit", methods=["POST"])
def submit_form():
    data = request.json
    print("Received data:", data)
    # You can now save this to a database
    return jsonify({"message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
# This is a simple Flask application that listens for POST requests on the /api/submit endpoint.