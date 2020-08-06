def myapp(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = [bytes(p + '\n', 'ascii') for p in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body

