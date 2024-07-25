from flask import Flask, make_response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/page/<pagename>')
def getPage(pagename):
    meda = open(f"raw/{pagename}/metadata.json").read()
    metadata = json.loads(meda)
    page = open(f"raw/{pagename}/{metadata['landPage']}").read()
    resp = make_response(page, 200)
    resp.mimetype = 'text/plain'
    return resp

@app.errorhandler(404)
def page_not_found(e):
    resp = make_response("# Page not found", 404)
    resp.mimetype = 'text/plain'
    return resp