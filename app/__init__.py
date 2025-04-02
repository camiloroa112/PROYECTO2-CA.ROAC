# 3rd Party Libraries
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

# 1st Party Libraries
from app.models.settings import user, password
from app.controllers.controlador import obtener_productos

# Connection to MySQL
app = Flask(__name__, template_folder = 'templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@localhost:3306/heladeria'
db = SQLAlchemy(app)

# Class to create the Ingredientes Model
class ingredientes(db.Model):
    # ID Ingredient
    id = db.Column(db.Integer, primary_key = True)
    # Ingredient Name
    nombre = db.Column(db.String(50), nullable = False)
    # Ingredient Price
    precio = db.Column(db.Float, nullable = False)
    # Ingredient Calories
    calorias = db.Column(db.Integer, nullable = False)
    # Ingredient Inventory
    inventario = db.Column(db.Integer, nullable = False)
    # Ingredient Boolean Value if its Vegetarian or not
    es_vegetariano = db.Column(db.Boolean, nullable = False)
    # Flavour
    sabor = db.Column(db.String(10), nullable = True)

# Class to create the Productos Model
class productos(db.Model):
    # ID Product
    id = db.Column(db.Integer, primary_key = True) 
    # Product Name
    nombre = db.Column(db.String(50), nullable = False)
    # Volume of the product
    volumen = db.Column(db.String(8), nullable = True)
    # Ingredient ID #1
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient ID #2
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient ID #3
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = False)
    # Ingredient #1
    ingrediente1 = db.relationship('ingredientes', foreign_keys = [ingrediente1_id])
    # Ingredient #2
    ingrediente2 = db.relationship('ingredientes', foreign_keys = [ingrediente2_id])
    # Ingredient #3
    ingrediente3 = db.relationship('ingredientes', foreign_keys = [ingrediente3_id])
    # Public Price
    precio_publico = db.Column(db.Float, nullable = False)
    # Glass type
    tipo_vaso = db.Column(db.String(8), nullable = True)

@app.route('/')
def index():
    
    # Trayendo resultados del controlador
    productos_ingredientes = obtener_productos(productos, ingredientes, db)
    
    # Displaying results in index.html
    return render_template('index.html', heladeria = productos_ingredientes)