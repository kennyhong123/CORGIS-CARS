from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('cars.json') as car_data:
        data = json.load(car_data)

def get_car_names():
	options = ""
	
	for car in data:
		options += Markup("<option value=" +'"'+ car["Identification"] +'">'+ car["Identification"] + "</option>")
    
	return options

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/identifications")
def render_identifications():
    return render_template('identifications.html')

@app.route("/horsepower")
def render_horsepower():
    return render_template('horsepower.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
