# test.py
from fluent import sender
from fluent import event
sender.setup('fluentd.test', host='localhost', port=24224)
event.Event('follow', {
  'from': 'userA',
  'to':   'userB'
})

event.Event('info',{'dic':'TEXTO TAMBIENT SE PUEDE ENVIAR'})