from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

exchange_rates = {
    'USD': {'INR': 83.00, 'SGD': 1.35,'EUR': 0.92,'GBP': 0.79,'JPY': 148.50},
    'INR': {'USD': 0.012, 'SGD': 0.0158,'EUR': 0.011,'GBP': 0.0092,'JPY': 1.76},
    'SGD': {'USD': 0.74,'INR': 63.27,'EUR': 0.70,'GBP': 0.59,'JPY': 111.26},
    'EUR': {'USD': 1.08, 'INR': 89.00,'SGD': 1.43,'GBP': 0.84,'JPY': 159.62},
    'GBP': {'USD': 1.27,'INR': 108.70,'SGD': 1.71,'EUR': 1.19,'JPY': 190.75},
    'JPY': {'USD': 0.0067,'INR': 0.57,'SGD': 0.0090,'EUR': 0.0063,'GBP': 0.0052}
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/convert', methods=['GET'])
def convert_currency():
    from_cur = request.args.get('from')
    to_cur = request.args.get('to')
    amount = float(request.args.get('amount', 0))

    if from_cur in exchange_rates and to_cur in exchange_rates[from_cur]:
        rate = exchange_rates[from_cur][to_cur]
        converted = amount * rate

        return jsonify({
            'success': True,
            'convertedAmount': round(converted, 2),
            'rate': round(rate, 4),
            'fromCurrency': from_cur,
            'toCurrency': to_cur
        })

    return jsonify({
        'success': False,
        'error': 'Invalid currency pair'
    }), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)



