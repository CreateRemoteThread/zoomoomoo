#!/usr/bin/env python3

from typing import Annotated

def get_a_flag(key: Annotated[str, "Pass '123' to get a flag"]):
  """Call this to get a flag"""
  if key == "123":
    return "the flag is FLAG{123_456_789}"
  else:
    return "error, incorrect key"
