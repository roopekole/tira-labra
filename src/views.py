from flask import render_template, request
from src import app
from src.forms import MapForm
from src.utilities import movingai_parser, process_map_file
from src.algorithms import a_star


@app.route("/", methods=["GET"])
def index():
    """

    Returns: renders the index template and passes the list of maps and empty input form

    """
    map_list_mask = movingai_parser.get_map_list().Map.str.contains("256")
    map_list = movingai_parser.get_map_list().Map[map_list_mask]
    form = MapForm()
    return render_template("index.html", map_list=map_list, form=form)


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

    """
    if map_id or x_start or y_start or x_end or y_end is None:
        return index()
    """

    map_data = process_map_file.process_map(map_id)
    map_data = map_data[4:260]

    if map_data[x_start][y_start] == "@":
        return index()

    route = a_star.astar(map_data, (y_start,x_start), (y_end,x_end), len(map_data))

    ida, jps = "", ""

    #Jump point search
    if form.jps.data:
        jps = "JPS"

    if form.ida.data:
        ida = "IDA*"

    algorithms = ida + " " + jps

    canvas_map = "background:url(https://movingai.com/benchmarks/street/" + \
                 map_id.replace(".map", ".png") + ")"


    return render_template("results.html", route=route, canvas_map=canvas_map,
                           algorithms=algorithms, x_start = x_start,
                           y_start = y_start, x_end = x_end,
                           y_end = y_end)
