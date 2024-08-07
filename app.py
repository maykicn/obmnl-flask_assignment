# Import libraries
# TASK LINK:  https://labs.cognitiveclass.ai/v2/tools/cloud-ide?ulid=ulid-d2ade1717bf72595f7653f7ccddff552dbd361c9
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': 200},
    {'id': 3, 'date': '2023-06-03', 'amount': 250},
    {'id': 4, 'date': '2023-06-03', 'amount': 275},
    {'id': 5, 'date': '2023-06-03', 'amount': 285},
    {'id': 6, 'date': '2023-06-03', 'amount': 300},
    {'id': 7, 'date': '2023-06-03', 'amount': 500}
]


# Read operation
@app.route('/', methods=['GET'])
def get_transactions():
    total_balance = sum(transaction['amount'] for transaction in transactions)
    return render_template('transactions.html', transactions=transactions, total_balance=total_balance)


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

# Search Transactions
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == 'POST':
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = [transaction for transaction in transactions if
                                 min_amount < transaction['amount'] < max_amount]
        return render_template('transactions.html', transactions=filtered_transactions)
    return render_template('search.html')

# Total Balance
@app.route('/balance')
def total_balance():
    balance = sum(transaction['amount'] for transaction in transactions)
    return f"Total Balance: {balance}"


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
