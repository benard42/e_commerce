from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from e_shopping.models import Post_product

product = Blueprint('product', __name__, url_prefix= '/product')

@product.route('/')
def hello():
    return 'you have reached the hello page'

@product.route('/')
def index():
    if current_user.is_authenticated:
        user_product = Post_product.get_product_by_user_id(current_user.id)
        return render_template('index.html',product=user_product)
    else:
        return redirect(url_for('users.login'))


@product.route('/create',methods=['POST'])
@login_required
def create():
    prod = request.form.get('prod')
    new_product = Post_product(prod = prod, created_by=current_user.id)
    new_product.save()
    flash('Product created successfully')
    return redirect(url_for('product.index'))

@product.route('/<int:product_id>/delete', methods = ['POST'])
@login_required
def delete(product_id):
    prod = Post_product.get_by_id(product_id)
    if prod and prod.created_by == current_user.id:
        prod.delete_instance
        flash('product deleted successfully')
    else:
        flash('product not found')

    return redirect(url_for('products.index'))