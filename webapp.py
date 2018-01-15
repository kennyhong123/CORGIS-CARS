from flask import Flask, Markup, render_template, request, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/largestCars")
def render_largest_cars():
    return render_template('largest-cars.html')
 

if __name__=="__main__":
    app.run(debug=False, port=54321)
