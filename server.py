from bottle import get, route, post, run, request # or route
from aperter import er_, json_


@route('/')
def root():
    return '''
        <h1>Wrong Route</h1>
    '''


@post('/er')
def er():
    try:
        em=-1
        url = request.forms.get('url')
        em = er_(url=url)
    except:
        print("url: "+url+" ,emotion: "+str(em))
        json = json_(status="fail")
        return json
    else:
        print("url: "+url+" ,emotion: "+str(em))
        json = json_(status="success",em=em,url=url)
        return json


if __name__ == '__main__':
    print("Do not close this window")
    run(host='localhost', port=8880)