from flask import Flask, request, jsonify
import ipaddress

app = Flask(__name__)

ALLOWED_NET = ipaddress.ip_network("192.168.1.0/24")
@app.before_request
def restrict_network():
    client_ip = request.remote_addr

    # Deny if not inside office network
    if ipaddress.ip_address(client_ip) not in ALLOWED_NET:
        return jsonify({
            "client_ip": client_ip,
            "error": "Access denied"
        }), 403


@app.route("/")
def home():
    return {"message": "done"}