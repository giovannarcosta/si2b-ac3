import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    maxim=100
    a=1
    b=1
    num=3
    primos='2,'
    while b<maxim:
        num_primo=1
        for i in range(2, num):
            if num % i == 0:
                num_primo = 0
                break
        if (num_primo):
            primos = primos + str(num) + ','
            b += 1
        num+=1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
