from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/horsepower")
def render_horsepower():
    with open('cars.json') as cars_data:
        cars = json.load(cars_data)
    longestData = get_longest_dam(cars)
    return render_template('horsepower.html', length = longestData[1])

def get_longest_dam(cars):
    length = 0
    for d in cars:
        if d["Engine Statistics"]["Horsepower"] > length:
            length = d["Engine Statistics"]["Horsepower"]
    return length

if __name__=="__main__":
    app.run(debug=False, port=54321)
