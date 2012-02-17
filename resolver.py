#! /usr/bin/python3

import sys
import id_store
import yaml

conf = yaml.load(open("./conf/resolver.yml", 'r'))

while sys.stdin:
#  print("http://lmgtfy.com/?q=" + sys.stdin.readline().rstrip())
#  map = id_store.IdStore('/www/resolver/')
  map = IdStore('/www/resolver/')
  try:
    result = map.getId(sys.stdin.readline().rstrip())
  except KeyboardInterrupt:
    break
  if result:
    print(result)
  else:
    print("http://" + conf['base_url'] + "/" + conf['static_pages']['error'])
  sys.stdout.flush()
