from flask import Flask, jsonify

app = Flask(__name__)

DATA = [

{"ID":1,"Species name":"Tradescantia spathacea","lat":25.75370,"lon":80.37926},
{"ID":2,"Species name":"Ardisia crenata","lat":25.75501,"lon":80.37918},
{"ID":3,"Species name":"Schinus terebinthfolius","lat":25.75454,"lon":80.37985},
{"ID":4,"Species name":"Dioscorea bulbifera","lat":25.75434,"lon":80.37842},
{"ID":5,"Species name":"Ardisia crenata","lat":25.75429,"lon":80.37917}
]

@app.route("/")
def index():
    return """
    <h1>FIU Nature Preserve invasive plant species clusters</h1>
    <p> Try these endpoints:</p>
    <ul> 
        <li>a href="/api/hello">/api/hello</a></li>
        <li>a href="/api/data">/api/data</a></li>
    </ul>
    """

@app.route('/api/hello')
def hello():
    return jsonify({'Welcome': 'This app contains location data on clusters of invasive plant species in the FIU Nature '
                               'Preserve.'})

@app.route("/api/data")
def data():
    return jsonify(DATA), 200

if __name__ == "__main__":
    app.run(debug=True)