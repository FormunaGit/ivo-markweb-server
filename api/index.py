from flask import Flask, make_response
import json

app = Flask(__name__)

def manager(pagename: str, subpage=None):
    unparsedMetadata = open(f"raw/{pagename}/metadata.json").read()
    metadata = json.loads(unparsedMetadata)

    page = None
    code = 200
    if subpage == None:
        try:
            page = open(f"raw/{pagename}/{metadata['landPage']}").read()
        except Exception as e:
            page = 'Page does not exist'
            code = 404
    elif subpage != None:
        try:
            page = open(f"raw/{pagename}/{subpage}.md").read()
        except Exception as e:
            page = 'Subpage does not exist'
            code = 404
    else:
        page = 'Error'

    resp = make_response(page, code)
    resp.mimetype = 'text/plain'
    return resp


@app.route('/')
def home():
    return 'Hi :)'

@app.route('/page/<pagename>') # Domain
def getPage(pagename):
    return manager(pagename)

@app.route('/page/<pagename>/<subpage>') # Domain + Subpage
def getSubpage(pagename, subpage):
    return manager(pagename, subpage)

@app.errorhandler(404)
def page_not_found(e):
    resp = make_response("# Page not found", 404)
    resp.mimetype = 'text/plain'
    return resp