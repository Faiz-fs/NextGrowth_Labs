import re

s = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or anobject that implements Countable (153)"}]}'

pattern=r':\s*(\d+)' #Pattern to find the numbers

match=[int(x) for x in re.findall(pattern,s)]  #Collecting number from the data and making a list 

print(match) #displaying the list of number