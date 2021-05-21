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
    path = "maps/" + map_id
    with open(path, "r") as map:
        data = map.read().splitlines()

    ida, jps = "", ""

    #Jump point search
    if form.jps.data:
        jps = "JPS"

    if form.ida.data:
        ida = "IDA*"


    algorithms = ida + " " + jps

    canvas_map = "background:url(https://movingai.com/benchmarks/street/" + map_id.replace(".map", ".png") + ")"
    test_route = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [15, 16], [15, 17], [15, 18],
                  [15, 19], [15, 20], [15, 21], [15, 22], [15, 23], [15, 24], [16, 24], [17, 24], [18, 24],
                  [19, 24], [20, 24], [21, 24], [22, 24], [23, 24], [24, 24],[24,25], [24, 26], [24,27], [24,28], [24,29],
                  [24,30], [24,31], [24,32], [24,33], [24,34], [24,35], [24,36], [24,37], [24,38], [24,39], [24,40], [24,41],
                  [24,42], [24,43], [24,44], [24,45], [24,46], [24,47], [24,48], [24,49], [24,50], [24,51], [24,52], [24,53],
                  [24,54]]

    return render_template("results.html", route=test_route, canvas_map=canvas_map, map=data,
                           algorithms=algorithms, x_start = x_start, y_start = y_start, x_end = x_end,
                           y_end = y_end)


@app.route("/select/<map_id>", methods=["GET"])
def select_parameters(map_id):
    return render_template("results.html", map_id = map_id)