from flask import Flask, Markup, render_template, request, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('cars.json') as cars_data:
		cars = json.load(cars_data)

def get_car_options():
	options = ""
	for c in cars:
		if c["Identification"]["ID"] not in cars:
			options += Markup("<option value=\"" + c["Identification"]["ID"] + "\">" + c["Identification"]["ID"] + "</option>")
	return options

def get_highmpg(model):
	fact = ""
	for c in cars:
		if c["Identification"]["ID"] == model:
			fact += Markup("<p>"+ "Highway MPG: "+str(c["Fuel Information"]["Highway mpg"]) + "</p>")
			fact += Markup("<p>"+ "City MPH: "+str(c["Fuel Information"]["City mph"]) + "</p>")
			fact += Markup("<p>"+ "Fuel Type: "+c["Fuel Information"]["Fuel Type"] + "</p>")
	return fact
	
def get_horsepower(power):
	yo = ""
	for c in cars:
		if c["Identification"]["ID"] == power:
			yo += Markup("<p>"+ "Transmission: "+c["Engine Information"]["Transmission"] + "</p>")
			yo += Markup("<p>"+ "Engine Type: "+c["Engine Information"]["Engine Type"] + "</p>")
			yo += Markup("<p>"+ "Horsepower: "+str(c["Engine Information"]["Engine Statistics"]["Horsepower"]) + "</p>")
			yo += Markup("<p>"+ "Hybrid: "+str(c["Engine Information"]["Hybrid"]) + "</p>")
			yo += Markup("<p>"+ "Number of Forward Gears: "+str(c["Engine Information"]["Number of Forward Gears"]) + "</p>")
			yo += Markup("<p>"+ "Driveline: "+str(c["Engine Information"]["Driveline"]) + "</p>")
	return yo

@app.route("/horsepowerPerCar")
def render_horsepower():
    power = request.args['car']
    return render_template('horsepower-per-car.html',options=get_car_options(),yo=get_horsepower(power))
	
@app.route("/mpgPerCar")
def render_highmpg():
	model = request.args['car']
	return render_template('mpg-per-car.html',options=get_car_options(),fact=get_highmpg(model))
	
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
    
@app.route("/mpgPerCars")
def render_mpg_per_cars():
    return render_template('mpg-per-car.html',options=get_car_options())

@app.route("/horsepowerPerCars")
def render_horsepower_per_cars():
    return render_template('horsepower-per-car.html', options=get_car_options())


if __name__=="__main__":
    app.run(debug=True, port=54321)
