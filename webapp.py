from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/laregstCar")
def render_largest_car():
    with open('cars.json') as cars_data:
        cars = json.load(cars_data)
    longestData = get_longest_car(cars)
    tallestData = get_tallest_car(cars)
    return render_template('horsepower.html',longest = longestData[0], length = longestData[1], tallest = tallestData[0], height = tallestData[1])
 
def get_longest_car(cars)
    length = 0
    longestCar = ""
    for c in cars:
        if c["Dimensions"]["Length"] > length:
            length = c["Dimensions"]["Length"]
            longestCar = c["Identification"]["Make"]
    return [longestCar, length]
      
def gget_tallest_car(cars):
    height = 0
    tallestCar = ""
    for c in cars:
        if c["Dimensions"]["Height"] > height:
            height = c["Dimensions"]["Height"]
            tallestCar = c["Identification"]["Make"]
    return [tallestCar, height]

if __name__=="__main__":
    app.run(debug=False, port=54321)
