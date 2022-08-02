import flask
from flask import request, jsonify, send_file, render_template, redirect, url_for
import plot_hitter
import io

from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
hitters = plot_hitter.hitter()


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/api/v1/resources/hitters/all', methods=['GET'])
def api_all():
    return jsonify(hitters.hitters['Name'].tolist())

       
@app.route('/api/v2/resources/hitters/<player>', methods=['GET'])
def register(player):
    new_graph_name = hitters.plot_player_stats(player)

    return render_template('player_stat.html', graph=new_graph_name)

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        player = request.form["nm"]
        new_graph_name = hitters.plot_player_stats(player)
        return render_template('player_stat.html', graph=new_graph_name)
    else:
        return render_template("search_player.html")

app.run(host="ec2-52-26-254-252.us-west-2.compute.amazonaws.com", port=80, debug=True)

