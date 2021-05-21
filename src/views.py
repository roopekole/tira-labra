from flask import render_template, request
from src import app
from src.forms import MapForm
from src.utilities import movingai_parser, unzip_file
import numpy as np
import pandas as pd


@app.route("/", methods=["GET"])
def index():
    map_list_mask = movingai_parser.get_map_list().Map.str.contains("256")
    map_list = movingai_parser.get_map_list().Map[map_list_mask]
    form = MapForm()
    return render_template("index.html", map_list=map_list, form=form)


@app.route("/select", methods=["POST"])
def process_selected_map():
    form = MapForm(request.form)

    x_start = form.start_x.data
    y_start = form.start_y.data

    x_end = form.end_x.data
    y_end = form.end_y.data

    map_id = request.form["map_select"]

    unzip_file.download_and_unzip(map_id)
    path = "example/" + map_id
    with open(path, "r") as map:
        data = map.read().splitlines()

    ida, jps = "", ""

    #Jump point search
    if form.jps.data:
        jps = "JPS"

    if form.ida.data:
        ida = "IDA*"

    print(ida)
    print(jps)

    algorithms = ida + " " + jps

    return render_template("select.html", map_id=map_id, map=data, algorithms=algorithms)


@app.route("/select/<map_id>", methods=["GET"])
def select_parameters(map_id):
    return render_template("select.html", map_id = map_id)