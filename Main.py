from flask import Flask, request, jsonify
import Info

app = Flask(__name__)

#get basic data about computer
@app.route("/get-info")
def get_user():
    try:
        computer_info = Info.Info()
        return jsonify(computer_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#get basic data about gpu
@app.route("/get-info/gpu")
def get_gpu():
    try:
        gpu_info = Info.Gpu_Info()
        return jsonify(gpu_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#get basic data about cpu
@app.route("/get-info/cpu")
def get_cpu():
    try:
        cpu_info = Info.Cpu_Info()
        return jsonify(cpu_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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