#!/usr/bin/python
from wow import application
from wsgiref.simple_server import make_server

http = make_server('',9000,application)
print 'The server Run on htpp 9000...'
http.serve_forever()
