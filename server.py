from bottle import route, run, static_file, post, request
from urllib import urlopen
import json

@route('/index.html')
def index():
    return static_file('/index.html', root='.')

@post('/md')
def md():
    requestedParam = request.POST
    params = {
        "text": requestedParam.text,
        "mode": "gfm"
        }
    res = urlopen('https://api.github.com/markdown', json.dumps(params))
    return res.read()

run(host='localhost', port=8080, debug=True, reloader=True)
