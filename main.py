
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature):
  return temperature>=100.4

# this is where I finished the code and where I can mess around
temperature = 100
if check_fever(temperature):
  print ("sadly you have a fever")
else:
  print("congrats you don't have a fever")

  