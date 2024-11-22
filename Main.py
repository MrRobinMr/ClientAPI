from flask import Flask, request, jsonify
import os
import subprocess
import socket

app = Flask(__name__)

#gering basic data about computer
@app.route("/get-info")
def get_user():
    computer_info = {
        "user" : os.getlogin(),
        "host_name" : socket.gethostname(),
        "ip" : socket.gethostbyname(socket.gethostname())
    }
    return jsonify(computer_info), 200

"""
#commands response for computers
@app.route("/send-shell", methods=["POST"])
def send_shell():
    data = request.get_json()
    if 'command' in data:
        command = data['command']
        response = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = {
            "stdout": response.stdout.strip(),
            "stderr": response.stderr.strip(),
            "return_code": response.returncode
        }
        return jsonify(result), 201
    else:
        return "Invalid data", 400
"""



if __name__ == "__main__":
    app.run(debug=True)