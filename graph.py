graph={'a':['b','c'],
       'b':['a','d'],
       'c':['a','d'],
       'd':['b','c','e'],
       'e':['d']}
print(graph)
print(graph.keys())
print(graph.values())

graph['f']= ['h','i']
print(graph)
