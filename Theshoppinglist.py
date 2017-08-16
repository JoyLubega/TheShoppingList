

from flask import Flask, render_template, request, redirect, url_for, session, flash
from classes.app import App
#import App from app

from classes.user import User
from classes.shoppinglists import SList
from classes.items import Item

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_items = []
current_user = None
Shop = App()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
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
    password = request.form['password2']
    # create user
    global current_user
    current_user = User(email, password, name)
    session['id'] = Shop.sign_up(current_user)
    # start session
    if session['id']:
        return redirect(url_for('homepage'))
    else:
        return render_template('index.html', error='Email already exists')



@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    """
    Signs in user to their account
    """
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

            return redirect(url_for('homepage'))
        return render_template('index.html',
                               error='Invalid username or password')
    else:
        return render_template('index.html')



@app.route('/signOut')
def sign_out():
    """
    Signs out user
    """
    session.pop('id', None)
    return redirect(url_for('sign_in'))


@app.route('/homepage')
def homepage():
    """
    Returns lists
    """

    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user # if the user exists then go the homepage
    return render_template('homepage.html',
                           lst=current_user.get_lists())



@app.route('/createList', methods=["POST"])
def createList():
    """
    Creates a new Shopping list
    """

    # Check user is signed in
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    # Pick form values
    list_name = request.form['list-name']

    # create List
    new_List = SList(list_name, session['id'])
    global current_user
    if current_user.create_bucket(new_List):
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
    new_list_name = request.form['list-name']

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
    thelist = current_user.get_single_bucket(list_name)
    return render_template('items.html',
                           list_name=list_name,
                           list_items=thelist.items )

@app.route('/del_list/<string:list_name>')
def del_list(list_name):
    """
    Deletes a list from the shopping list
    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    current_user.delete_list(list_name)
    return redirect(url_for('homepage'))


@app.route('/create_item/<string:list_name>', methods=['POST'])
def create_item(list_name):
    """

    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    #picking item name and item price from the user
    item_name = request.form['item-name']
    item_price= request.form['priceitem']
    new_item = Item(item_name, item_price)
    global current_user
    current_user.add_item(list_name, new_item) #adding the new created item
    return redirect(url_for('single_list',
                            list_name=list_name))


app.route('/edit_item/<string:list_name>/'
           '<item_name>', methods=['POST', 'GET'])
def edit_item(item_name, list_name):
    """
    Edits an item in a given bucket
    :param item_name:
    :param list_name:
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    if request.method == 'POST':
        new_item_name = request.form['item-name']
        status = False
        if 'status' in request.form:
            status = request.form['status']
        global current_user
        current_user.edit_item(list_name, item_name,
                               new_item_name, status)
        return redirect(url_for('single_list',
                                bucket_name=list_name))
    else:
        item = current_user.get_single_item(list_name, item_name)
        return render_template('homepage.html',
                               item_name=list_name,
                               activity_name=item_name,
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
                            bucket_name=list_name))







if __name__ == '__main__':
    app.run()