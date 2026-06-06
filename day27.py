import random
questions = [
    "What do you call the 'dots' in a graph?",
    "What do you call the 'lines' that connect the dots?",
    "What is a graph with arrows showing a one-way path called?",
    "What is a graph where you can go both ways on every line called?",
    "If a line has a number (like distance) on it, what is that called?",
    "Can a graph have a dot that isn't connected to anything?",
    "What do you call a path that starts and ends at the same dot?",
    "In an adjacency list, what do we store for each node?",
    "If node A is connected to node B, are they called 'neighbors'?",
    "What is the 'degree' of a node?",
    "Can two different lines connect the same two dots?",
    "What is a 'path' in a graph?",
    "What is a 'Self-loop'?",
    "Which is better for a giant graph with few lines: Matrix or List?",
    "If a graph has no cycles, what is it often called?",
    "How many neighbors does a 'leaf' node in a tree have?",
    "What does BFS stand for?",
    "What does DFS stand for?",
    "If a graph is 'Connected,' can you reach every dot?",
    "Is a social network like Facebook a graph?"
]


answers = [
    "nodes", "edges", "directed graph", "undirected graph", "weighted edge",
    "yes", "a cycle", "list of neighbors", "yes", "number of edges",
    "yes", "a sequence of nodes", "edge to itself", "adjacency list", "a tree",
    "only one", "breadth-first search", "depth-first search", "yes", "yes"
]





print("Welcome to Kbc")
totalWon=0
for i in range (10):
    r=random.choice(questions)
    print(r)
    ans=answers[questions.index(r)]
    n=input()
    if(n.lower()==ans):
        totalWon+=10000
        print("Correct Answer!!")
        print(" Current winning :",totalWon)
    
    else:
        print("Wrong ANswer!!")
        break;

print ("TOtal Wining:",totalWon)
        


 