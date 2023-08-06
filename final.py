import json
import pandas as pd
import numpy as np

def getMin(arr,N):
    minInd = 0
    for i in range(1, N):
        if (arr[i] < arr[minInd]):
            minInd = i
    return minInd
 
def getMax(arr,N):
    maxInd = 0
    for i in range(1, N):
        if (arr[i] > arr[maxInd]):
            maxInd = i
    return maxInd

def minOf2(x, y):
    return x if x < y else y

def minCashFlowRec(amount,N, l):
    mxCredit = getMax(amount,N)
    mxDebit = getMin(amount,N)

    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0

    min_amt = minOf2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min_amt
    amount[mxDebit] += min_amt
    l.append("Person " + str(mxDebit) + " receives " + str(min_amt)
        + " from " + "Person " + str(mxCredit))

    # print("Person ", mxDebit, " receives ", min_amt,
        # " from ", "Person ", mxCredit)

    minCashFlowRec(amount,N, l)

def minCashFlow(graph):
    N=len(graph)
    amount = [0 for i in range(N)]
    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])

    l = []
    minCashFlowRec(amount,N, l)
    return l


def convert_to_matrix(data):
    matrix = []
    for item in data:
        parts = item.split()
        row = [int(parts[1]), int(parts[6]), int(parts[3])]
        matrix.append(row)
    return matrix

def convert_to_json(matrix):
    data = []
    for row in matrix:
        name_owes,to_name, amount = row
        # data.append({
        #     "amount": str(amount),
        #     "name_owes": name_owes,
        #     "to_name": to_name
        # })
        data.append({
            "name_owes": name_owes,
            "to_name": to_name,
            "amount": str(amount)
        })
    # Convert the data list to JSON format
    json_data = json.dumps(data, indent=2)
    return (json_data)

def convert_json_to_matrix(data):
    df = pd.DataFrame(data)
    df['amount'] = pd.to_numeric(df['amount'])
    # Convert the DataFrame to a matrix (2D NumPy array)
    matrix = df.to_numpy()
    # Convert the input matrix to a NumPy array
    original_matrix = np.array(matrix)

    # Extract unique variable cells and create a mapping to indices
    unique_vars = np.unique(original_matrix[:, :2])
    var_to_index = {var: idx for idx, var in enumerate(unique_vars)}

    # Create a new matrix of zeroes with integer data type
    new_matrix = np.zeros((len(unique_vars), len(unique_vars)), dtype=int)

    # Populate the new matrix based on the mapping and rules
    for row in original_matrix:
        from_var = row[0]
        to_var = row[1]
        value = int(row[2])
        
        from_idx = var_to_index[from_var]
        to_idx = var_to_index[to_var]
        
        new_matrix[to_idx, from_idx] = value

    # Convert the NumPy matrix to a 2D list
    new_matrix_list = new_matrix.tolist()

    return new_matrix_list,var_to_index



def replace_values_with_keys(matrix, dictionary):
    # Create a new matrix with the same shape as the input matrix
    new_matrix = [[0] * len(row) for row in matrix]

    # Create a reversed dictionary where the keys are the values and the values are the keys
    reversed_dictionary = {value: key for key, value in dictionary.items()}

    # Iterate over the rows and columns of the input matrix
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            # Replace the value in the new matrix with the corresponding key from the reversed dictionary
            new_matrix[i][j] = reversed_dictionary.get(value, value)

    return new_matrix

def calculate_cash_flow(data):
    graph,var_index = convert_json_to_matrix(data)
    # N=len(graph)
    transactions_string_form=minCashFlow(graph)
    # print(transactions_string_form)
    cash_flow_matrix = convert_to_matrix(transactions_string_form)
    cash_flow_matrix_names_map=replace_values_with_keys(cash_flow_matrix,var_index)

    json_converted_op=convert_to_json(cash_flow_matrix_names_map)
    return json_converted_op