from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/page/<pagename>')
def getPage(pagename):
    page = open(f"pages/{pagename}/index.md").read()
    return page