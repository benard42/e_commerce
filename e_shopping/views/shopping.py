from flask import Blueprint, request, redirect, render_template
from e_shopping.models import Post_product

views = Blueprint('views', __name__)

@views.route('/products', methods = ['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        Product_quality = request.form['Product_quality']
        price = request.form['price']
        Total = request.form['Total']
        product = Post_product(product_name=product_name,product_type= product_type,Product_quality=Product_quality,price = price, Total= Total)
        product.save()
        return redirect('/products')

    products = Post_product.get_all()
    return render_template('products.html',products=products)

