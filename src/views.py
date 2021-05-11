from flask import render_template, session
from src import app
from src.utilities import movingai_parser
import requests

@app.route("/")
def index():
    map_list_mask = movingai_parser.get_map_list().Map.str.contains("256")
    map_list = movingai_parser.get_map_list().Map[map_list_mask]
    return render_template("index.html", map_list = map_list)

