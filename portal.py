from flask import Flask

app = Flask(__name__)


def calculate_fee(amount):
    return round(amount * 0.02, 2)


@app.route("/")
def home():
    amount = 1000
    fee = calculate_fee(amount)
    return (
        "Finance Service Portal<br>"
        "--------------------------<br>"
        f"Transaction Amount: {amount}<br>"
        f"Processing Fee: {fee}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
