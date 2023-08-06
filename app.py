from flask import Flask, request, jsonify
from flask_cors import CORS
import final

app = Flask(__name__)
data = []
CORS(app)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/add_data', methods=['POST'])
def add_data():
    data.clear()
    rows = request.get_json()
    for row in rows:
        row_data = {
            'name_owes': row['name_owes'],
            'to_name': row['to_name'],
            'amount': row['amount']
        }
        # print(f"Adding row: {row_data}")
        # print(type(row_data))
        data.append(row_data)
    return '', 204


@app.route('/get_data')
def get_data():
    return jsonify(data)

@app.route('/calculate_cash_flow')
def calculate_cash_flow():
    cash_flow_matrix = final.calculate_cash_flow(data)
    return (cash_flow_matrix)

if __name__ == '__main__':
    app.run(debug=True)
