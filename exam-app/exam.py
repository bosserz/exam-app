from lib2to3.pytree import convert
from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)
application = app

# create a dictionary of test questions from a csv
question_list = convert_to_dict("test.csv")

# first rout

@app.route("/")
def index():
    return render_template('index.html', page_title="Digital SAT Mockup Test")

# second route
@app.route("/exam/<num>")
def exam(num):
    return
