#!/usr/bin/python3
from flask import render_template, request, flash
from src import app
from src.forms import MapForm
from src.utilities import movingai_parser, process_map_file
from src.algorithms import a_star, jps


@app.route("/", methods=["GET"])
def index(error=None):
    """

    Args:
        error: Error message to display in case of bad selections

    Returns: renders the index template and passes the list of maps and empty input form

    """
    map_list_mask = movingai_parser.get_map_list().Map.str.contains("256")
    map_list = movingai_parser.get_map_list().Map[map_list_mask]
    form = MapForm()
    return render_template("index.html", map_list=map_list, form=form, error=error)


@app.route("/select", methods=["POST"])
def process_selected_map():
    """

    Returns: Returns a view with the selected map and cheapest path per algorithm

    """
    form = MapForm(request.form)

    x_start = form.start_x.data
    y_start = form.start_y.data
    x_end = form.end_x.data
    y_end = form.end_y.data

    map_id = request.form["map_select"]

    map_data = process_map_file.process_map(map_id)
    map_data = map_data[4:260]

    error = ""

    if None in (x_start, y_start, x_end, y_end):
        error += "One of the coordinates missing"
        return index(error)

    if map_data[y_start][x_start] == "@":
        error += "Bad start selection. "

    if map_data[y_end][x_end] == "@":
        error += "Bad end selection."

    if error != "":
        return index(error)

    algorithm_results = {}

    if form.jps.data:
        algorithm_results["JPS"] = jps.jps(
            map_data, (y_start, x_start), (y_end, x_end))

    if form.a_star.data:
        algorithm_results["A*"] = a_star.astar(
            map_data, (y_start, x_start), (y_end, x_end), 1)

    if form.dijkstra.data:
        algorithm_results["Dijkstra"] = a_star.astar(
            map_data, (y_start, x_start), (y_end, x_end), 0)

    if not algorithm_results:
        error += "No algorithm was selected."
        return index(error)

    canvas_map = "background:url(https://movingai.com/benchmarks/street/" + \
                 map_id.replace(".map", ".png") + ")"

    return render_template("results.html", route=list(algorithm_results.values())[0][0], canvas_map=canvas_map,
                           algorithms=algorithm_results, x_start=x_start,
                           y_start=y_start, x_end=x_end,
                           y_end=y_end)
