def makes10(a, b):
  sum = a + b

  if a or b == 10:
    return True
  elif sum == 10:
    return True
  else:
    return False

# failed 2 tests

# solution is here
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)