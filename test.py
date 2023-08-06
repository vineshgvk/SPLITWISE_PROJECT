# # ---------------------------------------------------------------------------------------
# import pandas as pd
# import json
# import numpy as np

# def convert_json_to_matrix(data):
#     # data = [
#     # {
#     #     "amount": "10",
#     #     "name_owes": "f",
#     #     "to_name": "e"
#     # },
#     # {
#     #     "amount": "10",
#     #     "name_owes": "f",
#     #     "to_name": "d"
#     # },
#     # {
#     #     "amount": "50",
#     #     "name_owes": "d",
#     #     "to_name": "e"
#     # }
#     # ]

#     # Create a DataFrame from the data
#     df = pd.DataFrame(data)
#     df['amount'] = pd.to_numeric(df['amount'])
#     # Convert the DataFrame to a matrix (2D NumPy array)
#     matrix = df.to_numpy()

#     # print(matrix)

#     matrix=matrix

#     # Extract unique variable cells and create a mapping to indices
#     unique_vars = np.unique(matrix[:, 1:])
#     var_to_index = {var: idx for idx, var in enumerate(unique_vars)}

#     # Create a new matrix of zeroes with integer data type
#     new_matrix = np.zeros((len(unique_vars), len(unique_vars)), dtype=int)

#     # Populate the new matrix based on the mapping and rules
#     for row in matrix:
#         value = row[0]
#         from_var = row[1]
#         to_var = row[2]
        
#         from_idx = var_to_index[from_var]
#         to_idx = var_to_index[to_var]
        
#         new_matrix[to_idx, from_idx] = value

#     # Convert the NumPy matrix to a 2D list
#     new_matrix_list = new_matrix.tolist()

#     # print("Original Matrix:\n", matrix)
#     # print("\nUnique Variables:", unique_vars)
#     # print("\nVariable to Index Mapping:", var_to_index)
#     # print("\nNew Matrix (as 2D list):\n", new_matrix_list)
#     return new_matrix_list


import json
from flask import jsonify
import pandas as pd
import numpy as np
# data = [
#     {
#         "amount": "10",
#         "name_owes": "f",
#         "to_name": "e"
#     },
#     {
#         "amount": "10",
#         "name_owes": "f",
#         "to_name": "d"
#     },
#     {
#         "amount": "50",
#         "name_owes": "d",
#         "to_name": "e"
#     }
#     ]

data=[{'name_owes': 'a', 'to_name': 'b', 'amount': '10'}, {'name_owes': 'b', 'to_name': 'c', 'amount': '20'}]

# df = pd.DataFrame(data)
# df['amount'] = pd.to_numeric(df['amount'])
# # Convert the DataFrame to a matrix (2D NumPy array)
# matrix = df.to_numpy()

# print(matrix)

import numpy as np

# def convert_matrix(data):
#     df = pd.DataFrame(data)
#     df['amount'] = pd.to_numeric(df['amount'])
#     # Convert the DataFrame to a matrix (2D NumPy array)
#     matrix = df.to_numpy()
#     # Convert the input matrix to a NumPy array
#     original_matrix = np.array(matrix)

#     # Extract unique variable cells and create a mapping to indices
#     unique_vars = np.unique(original_matrix[:, :2])
#     var_to_index = {var: idx for idx, var in enumerate(unique_vars)}
#     print(var_to_index)

#     # Create a new matrix of zeroes with integer data type
#     new_matrix = np.zeros((len(unique_vars), len(unique_vars)), dtype=int)

#     # Populate the new matrix based on the mapping and rules
#     for row in original_matrix:
#         from_var = row[0]
#         to_var = row[1]
#         value = int(row[2])
        
#         from_idx = var_to_index[from_var]
#         to_idx = var_to_index[to_var]
        
#         new_matrix[to_idx, from_idx] = value

#     # Convert the NumPy matrix to a 2D list
#     new_matrix_list = new_matrix.tolist()

#     return new_matrix_list


# def convert_json_to_matrix(data):
#     # data = [
#     # {
#     #     "amount": "10",
#     #     "name_owes": "f",
#     #     "to_name": "e"
#     # },
#     # {
#     #     "amount": "10",
#     #     "name_owes": "f",
#     #     "to_name": "d"
#     # },
#     # {
#     #     "amount": "50",
#     #     "name_owes": "d",
#     #     "to_name": "e"
#     # }
#     # ]

#     # Create a DataFrame from the data
#     df = pd.DataFrame(data)
#     df['amount'] = pd.to_numeric(df['amount'])
#     # Convert the DataFrame to a matrix (2D NumPy array)
#     matrix = df.to_numpy()

#     # print(matrix)
#     # Extract unique variable cells and create a mapping to indices
#     unique_vars = np.unique(matrix[:, 1:])
#     var_to_index = {var: idx for idx, var in enumerate(unique_vars)}

#     # Create a new matrix of zeroes with integer data type
#     new_matrix = np.zeros((len(unique_vars), len(unique_vars)), dtype=int)

#     # Populate the new matrix based on the mapping and rules
#     for row in matrix:
#         # value = row[0]
#         # from_var = row[1]
#         # to_var = row[2]
#         value = row[2]
#         from_var = row[0]
#         to_var = row[1]
        
#         from_idx = var_to_index[from_var]
#         to_idx = var_to_index[to_var]
        
#         new_matrix[to_idx, from_idx] = value

#     # Convert the NumPy matrix to a 2D list
#     new_matrix_list = new_matrix.tolist()

#     # print("Original Matrix:\n", matrix)
#     # print("\nUnique Variables:", unique_vars)
#     # print("\nVariable to Index Mapping:", var_to_index)
#     # print("\nNew Matrix (as 2D list):\n", new_matrix_list)
#     return new_matrix_list



# def convert_to_json(matrix):
#     data = []
#     for row in matrix:
#         name_owes,to_name, amount = row
#         # data.append({
#         #     "amount": str(amount),
#         #     "name_owes": name_owes,
#         #     "to_name": to_name
#         # })
#         data.append({
#             "name_owes": name_owes,
#             "to_name": to_name,
#             "amount": amount
#         })
#     # Convert the data list to JSON format
#     json_data = json.dumps(data, indent=2)
#     return (json_data)



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
    print(var_to_index)

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

    return new_matrix_list

x=convert_json_to_matrix(data)
print(x)