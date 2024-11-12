from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/payment", methods=["POST"])
def make_payment():
    return jsonify({"status": "success", "transaction_id": "txn_12345"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
