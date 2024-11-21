from flask import Flask, request, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/get-info")
def get_user():
    computer_info = {
        "user" : os.getlogin(),
        "host_name" : socket.gethostname(),
        "ip" : socket.gethostbyname(socket.gethostname())
    }
    return jsonify(computer_info), 200

if __name__ == "__main__":
    app.run(debug=True)