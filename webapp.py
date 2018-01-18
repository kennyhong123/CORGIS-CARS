from flask import Flask, Markup, render_template, request, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/largestCars")
def render_largestCars():
    with open('cars.json') as cars_data:
        cars = json.load(cars_data)
    longestData = get_longest_car(cars)
    tallestData = get_tallest_car(cars)
    return render_template('largest-cars.html',longest = longestData[0], length = longestData[1], tallest = tallestData[0], height = tallestData[1])
 
def get_car_options(cars):
    names = []
    options = ""
    for c in cars:
        if c["Identification"]["Make"] not in cars:
            names.append(c["Identification"]["ID"])
        options += Markup("<option value=\"" + c["Identification"]["Make"] + "\">" + c["Identification"]["Make"] + "</option>")
    return options

def get_longest_car(cars):
    length = 0
    longestCar = ""
    for c in cars:
        if c["Dimensions"]["Length"] > length:
            length = c["Dimensions"]["Length"]
            longestCar = c["Identification"]["ID"]
    return [longestCar, length]
      
def get_tallest_car(cars):
    height = 0
    tallestCar = ""
    for c in cars:
        if c["Dimensions"]["Height"] > height:
            height = c["Dimensions"]["Height"]
            tallestCar = c["Identification"]["ID"]
    return [tallestCar, height]
    
@app.route("/mpgPerCars")
def render_mpg_per_cars():
    return render_template('mpg-per-car.html')

@app.route("/horsepowerPerCars")
def render_horsepower_per_cars():
    return render_template('horsepower-per-car.html')


if __name__=="__main__":
    app.run(debug=False, port=54321)
