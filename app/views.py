# from flask import Flask, render_template, request, redirect, url_for, session, flash
# import sys
# import os
"""
sys.path.append(os.path.abspath('../classes'))
#import App from classes.app import App 
#import App from app
import App

import classes.user
import classes.shoppinglists
import classes.items
"""
from app.classes.auth import App
from app.classes.user import User
from app.classes.items import Item
from app.classes.shoppinglists import SList
from app import app, render_template, request, redirect, url_for, session, flash


# app = Flask(__name__)
# app.secret_key = b's\x83I\xc7\xd6\xae<\xf1\x8f\\b\xff\x9e\x82::'
# all_items = []
# current_user = None
Shop = App()



@app.route('/', methods=['GET'])
def index():
    """This show the first page which is the index page"""
    return render_template('signup.html')


@app.route('/sn', methods=['POST'])
def sn():
    """This show the first page which is the index page"""
    return render_template('index.html')

@app.route('/signUp', methods=['POST'])
def sign_up():
    """
    Signs up user to the app
    """
    # here the details of the user are picked using the variables
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # create user
    global current_user
    current_user = User(email, password, name)
    session['id'] = Shop.sign_up(current_user)
    # start session
    if session['id']:
        return redirect(url_for('homepage'))
    else:
        return render_template('index.html', error='Email already exists')

"""
@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    
    #Signs in user to their account
    
    if request.method == 'POST':
        # Pick form values
        email = request.form['email']
        password = request.form['password']
        user = User(email, password)
        # start session
        session['id'] = Shop.sign_in(user)

        if session['id']:
            global current_user
            user = [user for user in Shop.all_users
                    if user.id == session['id']]
            current_user = user[0]

            return redirect(url_for('index'))
        return render_template('homepage.html',
                               error='Invalid username or password')
    else:
        return render_template('homepage.html')
"""        


"""
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    error = None
    if request.method == 'POST':
        if request.form['email'] != app.config['EMAIL']:
            error = 'Invalid User'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session[id] = True
            flash('You were logged in')
            return redirect(url_for('homepage'))
    return render_template('index.html', error=error)
"""











@app.route('/signIn', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        return redirect(url_for('homepage'))
    else:
        return render_template('index.html')






@app.route('/signOut')
def sign_out():
    """
    Signs out user
    """
    session.pop('id', None)
    return redirect(url_for('sign_in'))


@app.route('/homepage', methods=['POST'])
def homepage():
    """
    Returns lists
    """

    #if 'id' not in session:
     #   return redirect(url_for('sign_in'))
    #global current_user # if the user exists then go the homepage
    return render_template('homepage.html')



@app.route('/createList', methods=['POST'])
def createList():
    """
    Creates a new Shopping list
    """

    # Check user is signed in
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    # Pick form values
    list_name = request.form['addlist']

    # create List
    new_List = SList(list_name, session['id'])
    global current_user
    if current_user.create_list(new_List):
        return redirect(url_for('homepage'))
    flash('Shopping List name already exists')
    return redirect(url_for('HomePage'))


@app.route('/edit_list/<list_name>', methods=['POST'])
def edit_list(list_name):
    """
    Edits attributes of a list
    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    new_list_name = request.form['addlistarea']

    global current_user
    current_user.edit_list(list_name,
                             new_list_name)
    return redirect(url_for('single_list',
                            list_name=new_list_name))


@app.route('/homepage/<string:list_name>')
def single_list(list_name):
    """
    Returns a single list with a given name
    :param list_name:
    """
    # checking if the user has logged in
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    thelist = current_user.get_single_list(list_name)
    return render_template('items.html',
                           list_name=list_name,
                           list_items=thelist.items )

@app.route('/del_list/<string:delist_name>')
def del_list(list_name):
    """
    Deletes a list from the shopping list
    :param list_name:
    """
    delist_name=request.form['deletelist']
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    current_user.delete_list(delist_name)
    return redirect(url_for('homepage'))


@app.route('/create_item/<string:list_name>', methods=['POST'])
def create_item(list_name):
    """

    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    #picking item name and item price from the user
    item_name = request.form['additem']
    item_price= request.form['addprice']
    new_item = Item(additem, addprice)
    global current_user
    current_user.add_item(list_name, new_item) #adding the new created item
    return redirect(url_for('single_list',
                            list_name=list_name))


app.route('/edit_item/<string:list_name>/'
           '<item_name>', methods=['POST', 'GET'])
def edit_item(list_name,item_name):
    """
    Edits an item in a given list
    :param item_name:
    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    if request.method == 'POST':
        new_item_name = request.form['edititem']
        status = False
        if 'status' in request.form:
            status = request.form['status']
        global current_user
        current_user.edit_item(list_name, item_name,
                               new_item_name, status)
        return redirect(url_for('single_list',
                                list_name=list_name))
    else:
        item = current_user.get_single_item(list_name, item_name)
        return render_template('homepage.html',
                               list_name=list_name,
                               item_name=item_name,
                               status=item.status)


@app.route('/del_item/<string:list_name>/'
           '<string:item_name>')
def del_item(item_name, list_name):
    """
    Deletes an item from a shopping List
    :param item_name:
    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    current_user.delete_item(list_name, item_name)
    return redirect(url_for('single_list',
                            list_name=list_name))
