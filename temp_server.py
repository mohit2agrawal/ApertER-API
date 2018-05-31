from bottle import get, route, post, run, request # or route
from moon import img


@route('/')
def root():
    return '''
        <h1>Hello World</h1>
        <a href="http://localhost:3000/face">go</a>
    '''


@get('/face') # or @route('/login')
def login():
    return '''
        <form action="/face" method="post">
            URL: <input name="url" type="text" />
            <input value="Enter" type="submit" />
        </form>
    '''

@post('/face') # or @route('/login', method='POST')
def do_login():
    url = request.forms.get('url')
    s=img(url)
    return s

if __name__ == '__main__':
    run(host='localhost', port=3000)