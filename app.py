from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder='images')

# Sample furniture data
furniture_data = [
    {"name": "Sofa", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Dining Table", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Bed", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door1", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan1", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair1", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door2", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan2", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair2", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door3", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan3", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair3", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door4", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan4", "price": "$700", "size": "Queen", "color": "White"},
    {"name": "Chair4", "price": "$500", "size": "3-seater", "color": "Gray"},
    {"name": "Door5", "price": "$300", "size": "6-person", "color": "Brown"},
    {"name": "Devan5", "price": "$700", "size": "Queen", "color": "White"}
]

@app.route('/')
def index():
    return render_template('index.html', furniture=furniture_data)

@app.route('/cart')
def cart():
 
    return render_template('cart.html' )

if __name__ == "__main__":
    app.run(debug=True)
