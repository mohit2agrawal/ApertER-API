from bottle import get, route, post, run, request  # or route
from newmoon import er_, json_


@route('/')
def root():
    """default route

    Returns:
        str: html body for error page
    """

    return '''
        <h1>Wrong Route</h1>
    '''


@post('/er')
def er():
    """emotion recognition endpoint
    accepts POST request

    Returns:
        str: json string of status, data, and message
    """

    try:
        em = -1
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