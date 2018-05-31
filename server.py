from bottle import get, route, post, run, request # or route
from moon import img,xjson


@route('/')
def root():
    return '''
        <h1>Wrong Route</h1>
    '''


@post('/face') # or @route('/login', method='POST')
def do_login():
    try:
        url = request.forms.get('url')
        s=img(url)
    except:
        s= xjson("fail")
        return s
    else:
        s= xjson("success",s,url)
        return s
if __name__ == '__main__':
    run(host='localhost', port=3000)