from flask import Flask, Markup, render_template, request, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('car.json') as car_data:
    data = json.load(car_data)

def get_car_names():
    options = ""
    for car in data:
        options += Markup("option value=" + '""' + car["Identification"]["ID"] + '">' + car["Identification"]["ID"] + "</option>")
    return options

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/largestCars")
def render_largestCars():
    return render_template('largest-cars.html')
    
@app.route("/mpgPerCars")
def render_mpg_per_cars():
    return render_template('mpg-per-car.html')

def get_mpg_per_car(cars):
    


if __name__=="__main__":
    app.run(debug=False, port=54321)
