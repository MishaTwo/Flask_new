from flask import Flask, render_template, request
from dotenv import load_dotenv
import  os

load_dotenv()

app = Flask(__name__)
app.config['KEY'] = os.getenv("KEY")

import  routes