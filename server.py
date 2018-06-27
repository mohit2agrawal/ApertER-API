from bottle import get, route, post, run, request # or route
from moon import fr_, json_


@route('/')
def root():
    return '''
        <h1>Wrong Route</h1>
    '''

@post('/fr')
def fr():
    try:
        url = request.forms.get('url')
        face = fr_(url=url)
    except:
        json = json_(status="fail")
        return json
    else:
        json = json_(status="success",face=face,url=url)
        return json

if __name__ == '__main__':
    print("Do not close this window")
    run(host='localhost', port=8880)