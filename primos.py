import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    ate=100
    a=1
    b=1
    n=3
    primo = "2,"
    
    while b < ate:
        num_primo = 1
        for i in range(2, n):
            if n % i == 0:
                num_primo = 0
            break
        if (num_primo):
            primo = primo + str(n) +","
            b += 1
        n += 1
        return primos
        

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
