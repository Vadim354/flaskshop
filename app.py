from flask import Flask, render_template

app = Flask("Магазин подарков", template_folder="", static_folder="")

@app.route('/')
def index():
    return render_template("index.html")



app.run()
