#!/usr/bin/python
def application(envirment,startup_response):
  nst = envirment['PATH_INFO'][1:]
  nst = nst.decode('utf-8').encode('gb2312')
  startup_response('200 OK',[('Content-Type','text/html')])
  return '<h1>hello world! %s</h1>' %(nst or 'web')
