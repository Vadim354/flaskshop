from flask import Flask, render_template, session

app = Flask("Магазин подарков", template_folder="", static_folder="")
app.secret_key = '1234'

products = {
    1:{
        'name':
        'price':
        'image:
    },
    2:{
        'name':
        'price':
        'image:
    }
}
@app.route('/')
def index():
    return render_template("index.html", products=products)
@app.route('/cart')
def cart():
    return render_template("cart.html")
@app.route('/o_nas')
def o_nas():
    return render_template("o_nas.html")


app.run()
