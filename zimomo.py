#!/usr/bin/env python3

import json
import inspect
import sys
import getopt
import os
import core.mcp

GLOBAL_NS_STORE = []
GLOBAL_FN_STORE = []

class Namespace:
  pass

def extractGlobals(fn):
  global GLOBAL_NS_STORE, GLOBAL_FN_STORE
  if not os.path.isfile(fn):
    sys.stderr.write("fatal: '%s' is not a file" % fn)
    sys.stderr.flush()
    sys.exit(-1)
  with open(fn,"r") as f:
    code = f.read()
  ns = Namespace()
  exec(code,ns.__dict__)
  out = []
  for i in ns.__dict__.keys():
    if callable(ns.__dict__[i]):
      GLOBAL_FN_STORE.append(ns.__dict__[i])
  GLOBAL_NS_STORE.append(ns)

def domain():
  args, opts = getopt.getopt(sys.argv[1:],"f:",["file="])
  for (arg, val) in args:
    if arg in ["-f","--file"]:
      extractGlobals(val) 
  core.mcp.start_mcp(GLOBAL_FN_STORE) 
 
if __name__ == "__main__":
  domain()
