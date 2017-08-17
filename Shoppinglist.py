

from flask import Flask, render_template, request, redirect, url_for, session, flash
from user import User
from shoppinglists import SList
from item import Item
from  app import App

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_items = []
current_user = None
bucketApp = App()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
