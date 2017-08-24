from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
import os


app = Flask(__name__)
app.secret_key = b's\x83I\xc7\xd6\xae<\xf1\x8f\\b\xff\x9e\x82::'
all_items = []
current_user = None
from app import views