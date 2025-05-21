import flask

app = flask.Flask(__name__)

@app.route('GET', '/')
def index():
    return {'message': 'Welcome to nope'}

if __name__ == '__main__':
    app.run(debug=True)
