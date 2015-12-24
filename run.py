#!/usr/bin/env python
from flask import Flask, request
from engine import get_similarity
import requests

app = Flask(__name__)



@app.route('/data', methods = ['POST'])
def handleData():
    # get web addresses for two images to compare
    img1 = request.form['img1']
    img2 = request.form['img2']
    # get the address to post result to
    addr = request.form['addr']
    if img1 and img2 and addr:
        # run your engine
        score = get_similarity(img1, img2)
        print addr, score
        # post similarity score
        return requests.post(addr, data={'score': score})



# run app locally on default port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0')