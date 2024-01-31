from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Mock user data
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "Email": "John.doe@example.com"
    }

    # Checking for extra query parameter
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200
@app.route("/creat-user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    return jsonify(user_data), 201

if __name__ == "__main__":
    app.run(debug=True)
