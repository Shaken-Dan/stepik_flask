import flask
import data

app = flask.Flask(__name__)


@app.route('/')
def index():
    title = data.title
    departures = data.departures
    tours = data.tours
    return flask.render_template('index.html',
                                 departures=departures,
                                 title=title,
                                 subtitle=data.subtitle,
                                 description=data.description,
                                 tours=tours
                                 )


@app.route('/departures')
@app.route('/data/departures/<city>')
def departures_page():
    directions = data.departures
    departure = data.tours
    departures = data.departures
    return flask.render_template('departure.html', departure=departure, directions=directions, departures=departures)


@app.route('/data/tours/<id>/')
def tours_page(id):
    departures = data.departures
    tours = data.tours[int(id)]
    return flask.render_template('tour.html', departures=departures, tours=tours)


if __name__ == '__main__':
    app.run()
