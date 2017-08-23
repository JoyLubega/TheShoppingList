from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
import os


app = Flask(__name__)
from app import views