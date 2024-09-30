import os
from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

#################################################
# Flask Setup
#################################################

os.chdir(os.path.dirname(os.path.realpath(__file__)))
app = Flask(__name__)
modelHelper = ModelHelper()

#################################################
# Flask Routes
#################################################

# HTML ROUTES
@app.route("/")
def index():
    return render_template("home.html")


# Notes: Live serving model deployment. This listens for requests of user-provided info from an
# html form. Big Idea: user inputs sent to backend and then you need a function (modelHelper)
# and you'll see modelHelper takes in user inputs and makes the prediction
@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    sex_flag = content["sex_flag"]
    age = float(content["age"])
    fare = float(content["fare"])
    familySize = int(content["familySize"])
    p_class = int(content["p_class"])
    embarked = content["embarked"]
    has_cabin = bool(int(content["has_cabin"]))

    preds = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked, has_cabin)
    return(jsonify({"ok": True, "prediction": str(preds)}))


@app.route("/dashboard1")
def dashboard():
    return render_template("tableau_1.html")

@app.route("/dashboard2")
def dashboard():
    return render_template("tableau_2.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/work_cited")
def work_cited():
    return render_template("workcited.html")


# Run the App
if __name__ == '__main__':
    app.run(debug=True)