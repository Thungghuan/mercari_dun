from flask import Flask, send_from_directory
from api.mercari import Mercari
import urllib.parse

app = Flask('mercari_dun')
mercari_api = Mercari()

@app.route("/")
def root():
    return send_from_directory('web/', 'index.html')

@app.route("/index.js")
def root_js():
    return send_from_directory('web/', 'index.js')

@app.route("/index.css")
def root_css():
    return send_from_directory('web/', 'index.css')

@app.route("/search/<keyword>")
def search(keyword=None):
    keyword = urllib.parse.unquote(keyword)
    print(keyword)
    return mercari_api.search(keyword=keyword)

# app.run('0.0.0.0', 6789, debug=False)