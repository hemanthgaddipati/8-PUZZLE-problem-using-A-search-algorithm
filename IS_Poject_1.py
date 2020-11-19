import copy
class Node:
    # Initialize new node with the data
    def __init__(self,data,level,hval,parent):
        self.state = data
        # level : path cost
        self.level = level
        # hval : heuristic value(heuristic 1 or heuristic 2 which is manhatten distance)
        self.hval = hval
        # fval : total cost = levelCost+HeuristicValue = level+ hval
        self.fval = level+hval 
        self.parent = parent
        self.children = []
            
    # get_position function returns position of any number in a given state
    # But we specifically use it to find the position of the 0 in the puzzle
    def get_position(self,mat,num):
        for row in range(0,len(self.state)):
            for col in range(0,len(self.state)):
                if mat[row][col] == num:
                    return row,col    
    
    # creates possible moves by moving the 0 in either left, right, up or down directions
    def generate_child_nodes(self):
        self.zero = self.get_position(self.state,0)
        i,j = self.get_position(self.state,0)
        self.child_nodes = []
        maxrows = 2
        maxcols = 2
        left = j - 1
        if(left >= 0):
            self.child_nodes.append((i, left))
        down = i + 1
        if(down <= maxrows):
            self.child_nodes.append((down, j))
        up = i - 1
        if(up >= 0):
            self.child_nodes.append((up, j))
        right = j + 1
        if(right <= maxcols):
            self.child_nodes.append((i, right))
    
    # Move the 0 in the given direction and if the position is out of limits the return None
    def shuffle(self,state1,state2):
        temp_matrix = copy.deepcopy(self.state)
        i1 = state1[0]
        j1 = state1[1]
        i2 = state2[0]
        j2 = state2[1]
        mx = temp_matrix[i1][j1]
        temp_matrix[i1][j1] = temp_matrix[i2][j2]
        temp_matrix[i2][j2] = mx
        return temp_matrix


class Astar_8_puzzle:
    def __init__(self):
        self.opened = []
        self.closed = []
    
    # get_position function returns position of any number in a given state
    # But we specifically use it to find the position of the 0 in the puzzle
    def get_position(self,mat,num):
        for row in range(0,len(mat)):
            for col in range(0,len(mat)):
                if mat[row][col] == num:
                    return row,col                
    
    # takes the input for the puzzle from the user and returns the input state as a 3*3 matrix
    def input_matrix(self,title):
        matrix = []
        while True:
            try:
                print("\n",title,"State = ")
                state = list(input("Enter the state matrix seperated by ',':").strip().split(','))[:9]
                if len(state) != 9:
                    print("Please provide correct input length for the puzzle")
                else:
                    for elem in range(0,9):
                        if(state[elem]!=''):
                            state[elem]=int(state[elem])
                        else:
                            state[elem]=0
                    break
            except ValueError:
                    print("Please provide the CORRECT INPUT.\nEnter the state matrix seperated by ',':")
                    input_matrix(title)
        return [state[0:3],state[3:6],state[6:9]]
    
    # Read the states {start,goal} and initialize node count to 0
    def read_states(self):
        self.start_state = self.input_matrix("Start")
        self.goal_state = self.input_matrix("Goal")
        self.node_count = 0
    
    # get the heuristic {h1, h2} from the user
    def heuristic(self):
        while True:
            self.heuristic_type = input("\nPlease select a heuristic as h1 or h2:")
            if self.heuristic_type == "h1" or self.heuristic_type == "h2":
                break
            else:
                print("Please provide Valid Input!!!")
    
    # h1 calculates the distance between current state and goal state
    def h1(self,current_state,goal_state):
        h1_value = 0
        for num in range(0,9):
            current_position = self.get_position(current_state,num)
            goal_position = self.get_position(goal_state,num)
            if current_position != goal_position:
                h1_value += 1
        return h1_value
       
    # h2 calculates manhatten distance
    def h2(self,current_state,goal_state):
        h2_value = 0
        for num in range(0,9):
            current_position = self.get_position(current_state,num)
            goal_position = self.get_position(goal_state,num)
            m_distance = abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])
            h2_value += m_distance
        return h2_value
    
    # selected node with f,g and h values
    def selected_node(self,node,info = True):
        curstate = node
        if info == True:
            print("cost g(x) = ", node.level, "heuristic h(x) = ",node.hval, "total cost f(x) = g(x)+h(x)",node.fval)
            curstate = node.state
        for i in curstate:
            print(i)
        print("\n\n")
        
    def path(self,node):
        self.selected_node(node,False)
        if node.parent == None:
            return
        self.path(node.parent)
        
    # f calculates hueristic value => f(x) = h(x) + g(x)
    def f(self,current_state,goal_state,h_type):
        if h_type == 'h1':
            return self.h1(current_state,goal_state)+current_state.level
        else:
            return self.h2(current_state,goal_state)+current_state.level

    def Execution_process(self):
        self.read_states()
        self.heuristic()
        if self.heuristic == "h1":
            initial_hval = self.h1(self.start_state,self.goal_state)
        else:
            initial_hval = self.h2(self.start_state,self.goal_state)
        
        print("Provide your start state matrix \n")
        self.selected_node(self.start_state,False)
        
        print("Provide the final/goal state matrix \n")        
        self.selected_node(self.goal_state,False)
        print(self.start_state)
        # Initialize start state and append the start node to opened list 
        start_state = Node(self.start_state,0,initial_hval,None)
        self.opened.append(start_state)
        
        while True:
            cur_node = self.opened[0]
            self.node_count += 1
            self.selected_node(cur_node)
            if cur_node.hval == 0:
                print("***********************************************************")
                break
            cur_node.generate_child_nodes()
            for node in cur_node.child_nodes:
                temp_node = cur_node.shuffle(node,cur_node.zero)
                if self.heuristic == 'h1':
                    temp_hval = self.h1(temp_node,self.goal_state)
                else:
                    temp_hval = self.h2(temp_node,self.goal_state)
                cur_node.children.append(Node(temp_node,cur_node.level+1,temp_hval,cur_node))
            
            for node in cur_node.children:
                self.opened.append(node)
            self.closed.append(cur_node)
            del self.opened[0]
            self.opened.sort(key = lambda val:val.fval,reverse=False)
            
            # if the program is unable to find solution after 150 iterations then we end it saying no solution is found
            if self.node_count > 150:
                print("Unable to find solution after 150 iterations!!")
                break


puzzle = Astar_8_puzzle()
puzzle.Execution_process()
print("Number of nodes expanded: ", len(puzzle.closed))
print("Number of nodes generated: ", len(puzzle.closed) + len(puzzle.closed))
