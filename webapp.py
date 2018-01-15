from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
@app.route("/horsepower")
def render_largest_dams():
    with open('cars.json') as cars_data:
        cars = json.load(cars_data)
    longestData = get_longest_dam(cars)
    return render_template('horsepower.html', longest = longestData[0], length = longestData[1])
@app.route("/dataByDam")
def render_data_by_dam():
    with open('hydropower.json') as dams_data:
        dams = json.load(dams_data)
    if 'dam' in request.args:
        d = get_dam_data(dams, request.args['dam'])
        return render_template('data-by-dam.html', options = get_dam_options(dams), name = d["Identity"]["Name"], year = d["Identity"]["Project"]["Year"], state = d["Location"]["State"], length = d["Dimensions"]["Crest Length"], height = d["Dimensions"]["Structural Height"])
    return render_template('data-by-dam.html', options = get_dam_options(dams))

@app.route("/damsPerState")
def render_dams_per_state():
    with open('hydropower.json') as dams_data:
        dams = json.load(dams_data)
    if 'state' in request.args:
        return render_template('dams-per-state.html', options = get_state_options(dams), numDams = get_dams_per_state(dams, request.args['state']), state = request.args['state'])
    return render_template('dams-per-state.html', options = get_state_options(dams))

def get_dam_options(dams):
    names = []
    options = ""
    for d in dams:
        if d["Identity"]["Name"] not in dams:
            names.append(d["Identity"]["Name"])
            options += Markup("<option value=\"" + d["Identity"]["Name"] + "\">" + d["Identity"]["Name"] + "</option>")
    return options

def get_state_options(dams):
    states = []
    options = ""
    for d in dams:
        if d["Location"]["State"] not in states:
            states.append(d["Location"]["State"])
            options += Markup("<option value=\"" + d["Location"]["State"] + "\">" + d["Location"]["State"] + "</option>")
    return options

def get_dam_data(dams, selected_dam):
    for d in dams:
        if d["Identity"]["Name"] == selected_dam:
            return d

def get_dams_per_state(dams, selected_state):
    numDams = 0
    for d in dams:
        if d["Location"]["State"] == selected_state:
            numDams += 1
    return numDams

def get_longest_dam(cars):
    length = 0
    for d in cars:
        if d["Engine Information"]["Engine Statistics"]["Horsepower"] > length:
            length = d["Engine Information"]["Engine Statistics"]["Horsepower"]
    return length

if __name__=="__main__":
    app.run(debug=False, port=54321)
