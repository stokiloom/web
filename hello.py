def myapp(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = [p + '\n' for p in environ['QUERY_STRING'].decode('ascii').split('&')]
    start_response(status, headers)
    return body

