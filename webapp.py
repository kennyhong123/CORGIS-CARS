from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('cars.json') as car_data:
        data = json.load(car_data)
	
def get_car_names():
	options = ""
	
	for food in data:
		options += Markup("<option value=" +'"'+ car["Description"] +'">'+ car["Description"] + "</option>")
    
	return options

def get_identi_info(name):
	info = ""
	for car in data:
		if name == car["Descriptions"]:
			fact += Markup("<p><b>"+ car["Description"] + "</b></p>")
			info += Markup("<p>"+"Make: " + str(car["Data"]["Identification"]["Make"]) +"</p>")
			info += Markup("<p>"+"Model Year: " + str(car["Data"]["Identification"]["Model Year"])+"</p>")
			info += Markup("<p>"+ "ID: " + str(car["Data"]["Identification"]["ID"]) + "</p>")
			info += Markup("<p>"+"Classification: " + str(car["Data"]["Identification"]["Classification"])+"</p>")
			info += Markup("<p>"+"Year: " + str(car["Data"]["Identification"]["Year"])+"</p>")
	return info

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/identifications")
def render_identifications():
    return render_template('identifications.html', Identifications = get_car_names())

@app.route("/horsepower")
def render_horsepower():
    return render_template('horsepower.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
