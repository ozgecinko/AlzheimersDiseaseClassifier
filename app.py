from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
from keras.preprocessing import image
from keras.metrics import AUC
from PIL import Image
import numpy as np
import pyrebase
from config import firebase_config

app = Flask(__name__)
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

dependencies = {"auc_roc": AUC}
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}

verbose_name = {
    0: "Non Demented",
    1: "Very Mild Demented",
    2: "Mild Demented",
    3: "Moderate Demented",
}

# Select model
model = load_model("alzheimer_cnn_model.h5", compile=False)

model.make_predict_function()


def predict_label(img_path):
    test_image = Image.open(img_path).convert("L")
    test_image = image.img_to_array(test_image) / 255.0
    test_image = test_image.reshape(-1, 128, 128, 1)

    predict_x = model.predict(test_image)
    classes_x = np.argmax(predict_x, axis=1)

    return verbose_name[classes_x[0]]


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("register.html")


@app.route("/", methods=["GET", "POST"])
def main():
    if person["is_logged_in"]:
        return render_template("index.html", person=person)
    return render_template("login.html")


@app.route("/submit", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        img = request.files["my_image"]

        img_path = "static/tests/" + img.filename
        img.save(img_path)

        predict_result = predict_label(img_path)

    if person["is_logged_in"]:
        data = {
            "user_name": person["name"],
            "result": predict_result,
            "created_at": datetime.now(),
        }
        db.child("alzheimer_results").child(person["uid"]).set(data)

    return render_template(
        "index.html", prediction=predict_result, img_path=img_path, person=person
    )


@app.route("/previous-results", methods=["GET", "POST"])
def previous_results():
    # Todo: create new previous list template
    return render_template("index.html")


@app.route("/auth/token", methods=["POST", "GET"])
def token():
    if request.method == "POST":
        result = request.form
        email, password = result["email"], result["password"]
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]

            data = db.child("users").get()
            person["name"] = data.val()[person["uid"]]["name"]
            return redirect(url_for("main"))
        except:
            return redirect(url_for("login"))
    else:
        if person["is_logged_in"]:
            return redirect(url_for("main"))
        else:
            return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        result = request.form
        email, password, name = result["email"], result["password"], result["name"]
        try:
            auth.create_user_with_email_and_password(email, password)
            user = auth.sign_in_with_email_and_password(email, password)

            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            person["name"] = name

            data = {"name": name, "email": email}
            db.child("users").child(person["uid"]).set(data)

            return redirect(url_for("main"))
        except:
            return redirect(url_for("signup"))
    else:
        if person["is_logged_in"]:
            return redirect(url_for("main"))
        else:
            return redirect(url_for("signup"))


if __name__ == "__main__":
    app.run(debug=True)
