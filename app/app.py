#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    output_text = '<h1>Python Operations with Flask Routing and Views</h1>'
    
    # Capture the output for the console
    print(output_text)
    
    return output_text

@app.route('/print/<parameter>')
def print_parameter(parameter):
    # Capture the output for the console
    print(parameter)
    
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter)) + '\n'
    
    # Capture the output for the console
    print(result)
    
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    # Capture the output for the console
    print(result)
    
    return str(result)

if __name__ == '__main__':
    app.run()


 