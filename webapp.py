from flask import Flask, Markup, render_template, request, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/largestCars")
def render_largest_cars():
   with open('hydropower.json') as dams_data:
        dams = json.load(dams_data)
        longestData = get_longest_dam(dams)
        tallestData = get_tallest_dam(dams)
    return render_template('largest-dams.html', longest = longestData[0], length = longestData[1], tallest = tallestData[0], height = tallestData[1])
 
def get_car_options(cars):
    names = []
    options = ""
    for c in cars:
        if c["Identification"]["Make"] not in cars:
            names.append(c["Identification"]["Make"])
        options += Markup("<option value=\"" + c["Identification"]["Make"] + "\">" + c["Identification"]["Make"] + "</option>")
        
def get_longest_car(cars)
    length = 0
    longestCar = ""
    for c in cars:
        if c["Dimensions"]["Length"] > length:
            length = c["Dimensions"]["Length"]
            longestCar = c["Identification"]["Make"]
    return [longestCar, length]
      
def get_tallest_car(cars):
    height = 0
    tallestCar = ""
    for c in cars:
        if c["Dimensions"]["Height"] > height:
            height = c["Dimensions"]["Height"]
            tallestCar = c["Identification"]["Make"]
    return [tallestCar, height]
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
