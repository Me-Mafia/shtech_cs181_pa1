# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    dfs_stack = util.Stack()
    dfs_stack.push(problem.getStartState())
    expanded = util.Counter()
    expanded[problem.getStartState()] = 1
    route = []
    paths = util.Stack()
    while not dfs_stack.isEmpty():
        current = dfs_stack.pop()
        if not paths.isEmpty():
            route = paths.pop()
        if problem.isGoalState(current):
            break
        successors = problem.getSuccessors(current)
        for i in successors:
            if expanded[i[0]] == 0:
                dfs_stack.push(i[0])
                paths.push(route + [i[1]])
                #print(route)
        expanded[current] = 1
    return route

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    bfs_queue = util.Queue()
    bfs_queue.push(problem.getStartState())
    expanded = util.Counter()
    expanded[problem.getStartState()] = 1
    route = []
    paths = util.Queue()
    while not bfs_queue.isEmpty():
        current = bfs_queue.pop()
        if not paths.isEmpty():
            route = paths.pop()
        if problem.isGoalState(current):
            break
        successors = problem.getSuccessors(current)
        for i in successors:
            if expanded[i[0]] == 0:
                bfs_queue.push(i[0])
                paths.push(route + [i[1]])
                if not problem.isGoalState(i[0]):
                    expanded[i[0]] = 1
    return route
    
   # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucs_queue = util.PriorityQueue()
    ucs_queue.push(problem.getStartState(),0)
    expanded = util.Counter()
    dis = util.Counter()
    expanded[problem.getStartState()] = 1
    route = []
    paths = util.PriorityQueue()
    while not ucs_queue.isEmpty():
        current = ucs_queue.pop()
        if not paths.isEmpty():
            route = paths.pop()
            #print(route)
        if problem.isGoalState(current):
            break
        successors = problem.getSuccessors(current)
        for i in successors:
            if expanded[i[0]] == 0:
                dis[i[0]] = dis[current] + float(i[2])
                ucs_queue.push(i[0], dis[i[0]])
                #if float(i[2]) <11 and float(i[2]) >= 1:
                #   print(i[1])
                paths.push(route + [i[1]], dis[i[0]])
                #if (dis[i[0]] < 15):
                #  print(dis[i[0]], i[0])
                if not problem.isGoalState(i[0]):
                    expanded[i[0]] = 1

    return route

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucs_queue = util.PriorityQueue()
    ucs_queue.push(problem.getStartState(),0)
    expanded = util.Counter()
    dis = util.Counter()
    expanded[problem.getStartState()] = 1
    route = []
    paths = util.PriorityQueue()
    while not ucs_queue.isEmpty():
        current = ucs_queue.pop()
        if not paths.isEmpty():
            route = paths.pop()
            #print(route)
        if problem.isGoalState(current):
            break
        successors = problem.getSuccessors(current)
        for i in successors:
            if expanded[i[0]] == 0:
                dis[i[0]] = dis[current] + float(i[2] + heuristic(i[0], problem))
                ucs_queue.push(i[0], dis[i[0]])
                #if float(i[2]) <11 and float(i[2]) >= 1:
                #   print(i[1])
                paths.push(route + [i[1]], dis[i[0]])
                #if (dis[i[0]] < 15):
                #  print(dis[i[0]], i[0])
                if not problem.isGoalState(i[0]):
                    expanded[i[0]] = 1

    return route



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
