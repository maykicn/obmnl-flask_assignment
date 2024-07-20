# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route('/', methods=['GET'])
def get_transactions():
    return render_template('transactions.html', transactions=transactions)


# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        id = len(transactions) + 1
        date = request.form['date']
        amount = float(request.form['amount'])
        transactions.append({'id': id, 'date': date, 'amount': amount})
        return redirect(url_for('get_transactions'))
    return render_template('form.html')


# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = next((transaction for transaction in transactions if transaction['id'] == transaction_id), None)
    if request.method == 'POST':
        transaction['date'] = request.form['date']
        transaction['amount'] = float(request.form['amount'])
        return redirect(url_for('get_transactions'))
    return render_template('edit.html', transaction=transaction)


# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    transaction = next((transaction for transaction in transactions if transaction['id'] == transaction_id), None)
    transactions.remove(transaction)
    return redirect(url_for('get_transactions'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
