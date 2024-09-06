# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    data = request.get_json()
    # Input initial marks from the user
    initial_marks = data['initialMarks']

    # Input credits from the user
    credits = [3, 4, 3, 3, 3, 1, 2, 3]

    final_marks = []

    # Calculate final marks
    num_of_subjects = 8 # total number of subjects in 6th sem
    for i in range(num_of_subjects):
        if initial_marks[i] < 100:
            single_marks = (initial_marks[i] // 10) + 1
            final_marks.append(single_marks)
        elif initial_marks[i] == 100:
            single_marks = (initial_marks[i] // 10)
            final_marks.append(single_marks)

    # Calculate credit marks
    credit_marks = [num1 * num2 for num1, num2 in zip(final_marks, credits)]

    # Calculate SGPA
    sgpa = sum(credit_marks) / sum(credits)

    # Round the SGPA to two decimal places
    sgpa_rounded = round(sgpa, 2)

    return jsonify({'sgpa': sgpa_rounded})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
