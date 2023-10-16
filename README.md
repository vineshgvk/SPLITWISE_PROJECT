
## Cash Flow Optimization App

This is a simple Flask web app that optimizes cash flow between entities by minimizing the total amount of money transferred.

## Functionality

- The main `index.html` page has a form to input a graph matrix representing money owed between entities 
- On submitting the form, a POST request is sent to the `/optimize` route
- The optimization logic uses a recursive algorithm to calculate the minimum cash transfers
- The result is returned as JSON containing info about payer, payee and transfer amount for each step
- The frontend displays the optimized cash flow steps
- A sample output looks like below upon accessing the localhost.
  
<img width="872" alt="Transaction_Inputs" src="https://github.com/vineshgvk/SPLITWISE_PROJECT/assets/67590588/bed77d06-bd65-4f0f-a23f-1c6daa3478ac">

## Usage

- Clone the repo and cd into the directory
- Create a virtualenv and activate it
- Install dependencies: `pip install -r requirements.txt` 
- Run the app: `python app.py`
- Access the app at http://localhost:5000
- Enter values in the graph matrix form and submit
- Optimized cash flow steps will be displayed below the form

## Implementation 

- `app.py` contains the Flask app and routing
- `getMin()`, `getMax()` helpers get min/max indexed values in an array
- `minOf2()` returns minimum of two values 
- `minCashFlowRec()` implements recursive optimized cash flow algorithm
- `printCashFlow()` prints each step's payer, payee and amount  
- `index.html` has the web form and result display

## Technologies

**Frontend:**

- HTML - To create the web form 
- CSS - For basic styling
- JavaScript - Form validation and handling request/response

**Backend:**

- Python - For the server logic 
- Flask - Python web microframework
- JSON - For sending data between frontend and backend

**Libraries:**

- Flask - For building the web app
- jsonify - For converting to the JSON format  

**Tools & Platforms:**

- Git/GitHub - For version control and source code management
- Visual Studio Code - As IDE for development
- Postman - For testing API endpoints

## Further Improvements

- Validate graph matrix input
- Add more informative result display
- Improve UI/UX
- Containerize app with Docker

## Contact Information
Feel free to contact me at gande.vi@northeastern.edu for any questions or improvements related to this project.
