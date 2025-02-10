
#? VER 1
# #! make a node
# def mn(name):
#     n = Node(name)
#     graph.add_node(n)
#     return n

# #! make an edge
# def me(n1,n2,name):
#     e = Edge(n1, n2, name)
#     graph.add_edge(e)
#     return e

# nodes = {}
# nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery"]
# for name in nodeNames:  
#     nodes[name] = mn(name)
# print(nodes)


# edgeRels = "12,13,14,15,16,17,18,19,110,23,24,610,89"
# allRels = edgeRels.split(",")
# names = [10,-10,-7,-1,9,8,10,10,-10,-9,-7,-10,10]
# edges = {}
# print(allRels)
# for k, j in enumerate(allRels):
#     try:
#         first, second = j
#     except(ValueError):
#         first, second = j[0], j[1:]
#     print(edges)
#     edges[f"e{str(j)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(names[k]))
# print(edges)



#? VER 2
# #! make a node
# def mn(name):
#     n = Node(name)
#     graph.add_node(n)
#     return n

# #! make an edge
# def me(n1,n2,name):
#     e = Edge(n1, n2, name)
#     graph.add_edge(e)
#     return e


# nodes = {}
# nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery"]
# colourMatching = {
#     "y":Color.YELLOW,
#     "t":Color.rgb(210,180,140),
#     "g":Color.LIGHT_GREY
#     }
# nodeColours = ["y","t","t","t","y","y","g","y","y","t"]
# for i, name in enumerate(nodeNames):  
#     nodes[name] = mn(name)
#     nodes[name].set_color(colourMatching[nodeColours[i]])
# print(nodes)



# edges = {}
# edgeInfo = [("12",10),("13",-10),("14",-7),("15",-1),("16",9),("17",8),("18",10),("19",10),("110",-10),("23",-9),("24",-7),("610",-10),("89",10)]
# for k, j in edgeInfo:
#     try:
#         first, second = k
#     except(ValueError):
#         first, second = k[0], k[1:]
#     edges[f"e{str(k)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(j))
# print(edges)


#? VER 3
# #! make a node
# def mn(name):
#     n = Node(name)
#     graph.add_node(n)
#     return n

# #! make an edge
# def me(n1,n2,name):
#     e = Edge(n1, n2, name)
#     graph.add_edge(e)
#     return e


# nodes = {}
# nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery","Bee Larry King","Waterbug","Judge Bumbleton","Ladybug"]
# colourMatching = {
#     "y":Color.YELLOW,
#     "t":Color(210,180,140),
#     "l":Color.LIGHT_GREY,
#     "b":Color.BLUE,
#     "p":Color(255,192,203),

#     "g":Color.GREEN,
#     "r":Color.RED,
#     "o":Color(255,165,0)
#     }
# nodeColours = ["y","t","t","t","y","y","l","y","y","t","y","b","t","p"]
# for i, name in enumerate(nodeNames):  
#     nodes[name] = mn(name)
#     nodes[name].set_color(colourMatching[nodeColours[i]])
# print(nodes)

# edges = {}
# edgeInfo = [("12",10),("13",-10),("14",-7),("15",-1),("16",9),("17",7),("18",10),("19",10),("110",-10),("111",0),("112",0),("113",7),("114",6),("23",-9),("24",-7),("213",7),("312",0),("610",-10),("714",8),("89",10)]
# for k, j in edgeInfo:
#     try:
#         first, second = k
#     except(ValueError):
#         first, second = k[0], k[1:]
#     edges[f"e{str(k)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(j))

#     if j > 0:
#         edges[f"e{str(k)}"].set_color(colourMatching["g"])
#     elif j < 0:
#         edges[f"e{str(k)}"].set_color(colourMatching["r"])
#     else:
#         edges[f"e{str(k)}"].set_color(colourMatching["o"])
    
# print(edges)


#? VER 4
# def get_colour(value):
#     # red: 255 0 0, orange 255 165 0, green 0 255 0
#     # red -> orange
#     if value < 0:
#         r = 255
#         g = int(165/10 * (value + 10))
#         b = 0
#     # orange -> green
#     else:
#         r = int(255 - ((255/10) * value))
#         g = int(165 + ((90/10) * value))
#         b = 0
    
#     return (r, g, b)

# #! make a node
# def mn(name):
#     n = Node(name)
#     graph.add_node(n)
#     return n

# #! make an edge
# def me(n1,n2,name):
#     e = Edge(n1, n2, name)
#     graph.add_edge(e)
#     return e

# nodes = {}
# nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery","Bee Larry King","Waterbug","Judge Bumbleton","Ladybug"]
# colourMatching = {
#     "y":Color.YELLOW,
#     "t":Color(247,220,180),
#     "l":Color.LIGHT_GREY,
#     "b":Color.BLUE,
#     "p":Color(255,192,203),
#     }
# nodeColours = ["y","t","t","t","y","y","l","y","y","t","y","b","t","p"]
# for i, name in enumerate(nodeNames):  
#     nodes[name] = mn(name)
#     nodes[name].set_color(colourMatching[nodeColours[i]])
#     nodes[name].set_size(size=15)
# print(nodes)

# edges = {}
# edgeInfo = [("12",10),("13",-10),("14",-7),("15",-3),("16",9),("17",7),("18",10),("19",10),("110",-10),("111",1),("112",0),("113",7),("114",6),("23",-9),("24",-7),("213",7),("312",-1),("610",-10),("714",8),("89",10)]
# for k, j in edgeInfo:
#     try:
#         first, second = k
#     except(ValueError):
#         first, second = k[0], k[1:]
#     edges[f"e{str(k)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(j))

#     r,g,b = get_colour(j)
#     edges[f"e{str(k)}"].set_color(Color(r,g,b))

# pynode_core.add_event(pynode_core.Event(pynode_core.js_set_spread, [100]))
# print(edges)
# print([get_colour(val) for val in range(-10,11)])


#? VER 5
# def get_colour(val):
#     # red: 255 0 0, orange 255 165 0, green 0 255 0
#     # red -> orange
#     if val < 0:
#         r = 255
#         g = int(165/10 * (val + 10))
#         b = 0
#     # orange -> green
#     else:
#         r = int(255 - ((255/10) * val))
#         g = int(165 + ((90/10) * val))
#         b = 0
#     return (r, g, b)

# def get_size(n):
#     return 15 + n.degree()

# #! make a node
# def mn(name):
#     n = Node(name)
#     graph.add_node(n)
#     return n

# #! make an edge
# def me(n1,n2,name):
#     e = Edge(n1, n2, name)
#     graph.add_edge(e)
#     return e

# colourMatching = {
#     "y":Color.YELLOW,
#     "t":Color(247,220,180),
#     "l":Color.LIGHT_GREY,
#     "b":Color.BLUE,
#     "p":Color(255,192,203),
#     }
# nodes = {}
# nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery","Bee Larry King","Waterbug","Judge Bumbleton","Ladybug"]
# nodeColours = ["y","t","t","t","y","y","l","y","y","t","y","b","t","p"]
# for i, name in enumerate(nodeNames):  
#     nodes[name] = mn(name)
#     nodes[name].set_color(colourMatching[nodeColours[i]])
# print(nodes)

# edges = {}
# edgeInfo = [("12",10),("13",-10),("14",-7),("15",-3),("16",9),("17",7),("18",10),("19",10),("110",-10),("111",1),("112",0),("113",7),("114",6),("23",-9),("24",-7),("213",7),("312",-1),("610",-10),("714",8),("89",10)]
# for k, j in edgeInfo:
#     try:
#         first, second = k
#     except(ValueError):
#         first, second = k[0], k[1:]
#     edges[f"e{str(k)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(j))

#     r,g,b = get_colour(j)
#     edges[f"e{str(k)}"].set_color(Color(r,g,b))

# [nodes[name].set_size(size=get_size(nodes[name])) for name in nodeNames]

# pynode_core.add_event(pynode_core.Event(pynode_core.js_set_spread, [130]))
# print(edges)
# print([get_colour(val) for val in range(-10,11)])

#? FINAL VER
# returns a colour between red and green for an edge
def get_colour(val):
    # red: 255 0 0, orange 255 165 0, green 0 255 0
    # red -> orange
    if val < 0:
        r = 255
        g = int(165/10 * (val + 10))
        b = 0
    # orange -> green
    else:
        r = int(255 - ((255/10) * val))
        g = int(165 + ((90/10) * val))
        b = 0
    return (r, g, b)

# returns a size for the node
def get_size(n):
    return 15 + n.degree()

#! make a node
def mn(name):
    n = Node(name)
    graph.add_node(n)
    return n

#! make an edge
def me(n1,n2,name):
    e = Edge(n1, n2, name)
    graph.add_edge(e)
    return e

# colour legend
colourMatching = {
    "y":Color.YELLOW,
    "t":Color(247,220,180),
    "l":Color.LIGHT_GREY,
    "b":Color.BLUE,
    "p":Color(255,192,203),
    }

nodes = {}
nodeNames = ["Barry Benson","Vanessa Bloome","Ken","Bud Ditchwater","Jock","Adam Flayman","Mooseblood","Janet Benson","Martin Benson","Leyton T. Mongomery","Bee Larry King","Waterbug","Judge Bumbleton","Ladybug"]
nodeColours = ["y","t","t","t","y","y","l","y","y","t","y","b","t","p"]
for i, name in enumerate(nodeNames):  
    nodes[name] = mn(name)
    nodes[name].set_color(colourMatching[nodeColours[i]])

edges = {}
edgeInfo = [("12",10),("13",-10),("14",-7),("15",-3),("16",9),("17",7),("18",10),("19",10),("110",-10),("111",1),("112",0),("113",7),("114",6),("23",-9),("24",-7),("213",7),("312",-1),("610",-10),("714",8),("89",10)]
for k, j in edgeInfo:
    try:
        first, second = k
    except(ValueError):
        first, second = k[0], k[1:]
    edges[f"e{str(k)}"] = me(nodes[nodeNames[int(first)-1]], nodes[nodeNames[int(second)-1]], str(j))

    r,g,b = get_colour(j)
    edges[f"e{str(k)}"].set_color(Color(r,g,b))

[nodes[name].set_size(size=get_size(nodes[name])) for name in nodeNames]

pynode_core.add_event(pynode_core.Event(pynode_core.js_set_spread, [130]))

print(nodes)
print(edges)
print([get_colour(val) for val in range(-10,11)])





