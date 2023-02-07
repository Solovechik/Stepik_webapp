def hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    response_body = environ['QUERY_STRING'].split('&')
    return ['\n'.join(response_body).encode('utf-8')]

