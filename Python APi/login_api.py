from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# A dictionary to store the users in memory
users = {
    "john": generate_password_hash("123456"),
    "mary": generate_password_hash("abcdef"),
}

@app.route("/login", methods=["POST"])
def login():
    # Get the request data
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    # Check if the user exists in the database
    if username in users:
        # Check if the password is correct
        if check_password_hash(users[username], password):
            return jsonify({"message": "Success"})
        else:
            return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "Invalid username"}), 401

if __name__ == "__main__":
    app.run()

