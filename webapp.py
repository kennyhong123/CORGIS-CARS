from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/identifications")
def render_identifications():
    return render_template('identifications.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
