from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from static.Products.product_reader import product_reader
# -*- coding: utf-8 -*-

app = Flask(__name__)
app.config.secret_key = "xxxxxxxxxx"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Productsdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

products = product_reader('static/Products/productos.csv')

store = {
    'store_name': 'Albye',
    'slogan': 'El caviar de la Sal',
    'titular': 'Alberto LastName',
    'titular_mail': 'titualmail@gmail.com',
    'titular_phone': '555987654',
    'Facebook': 'facebook_account',
    'Instagram': 'instagram_account'
}

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articulo = db.Column(db.String(50),index=True)
    sabor = db.Column(db.String(50),index=True)
    gramos = db.Column(db.Integer,index=True)

@app.route('/')
def index():
    route = 'static/Products/product_images/'
    return render_template('base.html',products=products,store=store,route=route)

if __name__=='__main__':
    app.run(debug=True)