from flask import Flask, render_template, request
from stock_engine import get_stock_data
from alert_engine import check_alert

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    stock_data = None
    price = None
    alert = None
    symbol = None
    error = None

    if request.method == "POST":

        symbol = request.form.get("symbol")
        threshold_input = request.form.get("threshold")

        if not symbol or not threshold_input:
            error = "Please enter both symbol and threshold."
        else:
            try:
                threshold = float(threshold_input)
                result = get_stock_data(symbol)

                if result:
                    df, price = result
                    alert = check_alert(price, threshold)
                    stock_data = df.to_html(classes="table", index=False)
                else:
                    error = "Invalid stock symbol or data not available."

            except ValueError:
                error = "Threshold must be a number."

    return render_template(
        "index.html",
        stock_data=stock_data,
        price=price,
        alert=alert,
        symbol=symbol,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)