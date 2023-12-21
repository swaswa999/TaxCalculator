from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        tax_rate = float(request.form['tax_rate'])
        amount = float(request.form['amount'])
        total_amount = amount + (amount * tax_rate / 100)
        return render_template('result.html', amount=amount, tax_rate=tax_rate, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
