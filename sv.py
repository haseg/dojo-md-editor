from bottle import route, run, static_file, post, request
from urllib import urlopen
import json

@route('/index.html')
def index():
    return static_file('/index.html', root='.')

@post('/md')
def md():
    param = request.POST
    params = {
        "text": param.text,
        "mode": "gfm",
        "context": "github/gollum"
        }
    res = urlopen('https://api.github.com/markdown', json.dumps(params))
    return res.read()

run(host='localhost', port=8080, debug=True, reloader=True)
