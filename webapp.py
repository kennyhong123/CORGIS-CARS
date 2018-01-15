from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/horsepower")
def render_highest_horsepower():
    with open('cars.json') as car_data:
        cars = json.load(car_data)
    highestHorsepower = get_highest_horsepower(cars)
    return render_template('largest-dams.html', highest = highestHorsepower[0], length = highestHorsepower[1])

def get_highest_horsepower(cars):
	length = 0
	highestHorsepower = ""
	for c in cars:
		c['Engine Information']['Engine Statistics']['Horsepower'] > length:
		length = c['Engine Information']['Engine Statistics']['Horsepower']
	return [highestHorsepower,length]

if __name__=="__main__":
    app.run(debug=False, port=54321)
