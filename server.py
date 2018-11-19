#!/usr/bin/env python3

from flask import Flask
import tasks

app = Flask(__name__)

@app.route('/pronouncounts', methods=['GET'])
def PronounCounts():
    results = tasks.counts.apply_async()
    pronounCounts = results.get()
    return(pronounCounts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
