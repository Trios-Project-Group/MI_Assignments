<<<<<<< HEAD
def A_star_Traversal(cost,heuristic,start_point,goals):
	l = []
	Astart_destination = goals[:]

	priority_queue = [(start_point,0,0 + heuristic[start_point],[start_point])]   # (currnode,currcost->g,totalcost->f,path)
	 
	visit = [0] * len(cost)
	visit[start_point] = 1
	
	GOALS = {}

	while priority_queue != []:
		node,path_cost,total_cost,path = priority_queue.pop(0)

		if node in Astart_destination:
			if node not in GOALS:
				GOALS[node] = (total_cost,path)            
			Astart_destination.remove(node)
			
			if Astart_destination == []:
				break
			
		for i in range(1,len(cost)):
			
			if not(visit[i]) and cost[node][i] > 0:
				child_path = path[:]
				child_path.append(i)  
				g = path_cost+cost[node][i]
				f = g + heuristic[i]
				priority_queue.append((i,g,f,child_path))
				visit[i] = 1
			
			if visit[i] and cost[node][i] > 0:
				c = [(q,r,s) for p,q,r,s in priority_queue if p == i] # total_cost
				if c != [] and path_cost + cost[node][i] + heuristic[i] < c[0][1]:
					child_path = path[:]
					child_path.append(i)
					g = path_cost+cost[node][i]
					f = g + heuristic[i]
					priority_queue.remove((i,c[0][0],c[0][1],c[0][2]))
					priority_queue.append((i,g,f,child_path))
					
		priority_queue = sorted(priority_queue, key = lambda x: x[2])
		# print(priority_queue)
					
	# print(path)
	# print(GOALS)
	
	GOALS = {k: v for k, v in sorted(GOALS.items(), key=lambda item: item[1][0])}
	
	try:
		cost,l = GOALS.pop(list(GOALS.keys())[0])
	except:
		pass
	
	# print(cost)

	return l

def UCS_Traversal(cost,start_point,goals):
	l = []
	ucs_destination = goals[:]
	
	priority_queue = [(start_point,0,[start_point])]  # (currnode,pathcost,path -> [])
	
	visit = [0] * len(cost)
	visit[start_point] = 1
	
	GOALS = {}

	while priority_queue != []:
		node,path_cost,path = priority_queue.pop(0)

		if node in ucs_destination:
			
			if node not in GOALS:
				GOALS[node] = (path_cost,path)

			ucs_destination.remove(node)
			
			if ucs_destination == []:
				break
			
		
		for i in range(1,len(cost)):   # for all child
			
			if not(visit[i]) and cost[node][i] > 0:  # if child is not visited
				child_path = path[:]
				child_path.append(i)
				priority_queue.append((i,path_cost+cost[node][i],child_path))
				visit[i] = 1
				
			
			if visit[i] and cost[node][i] > 0:  # if child is visited
				c = [(q,r) for p,q,r in priority_queue if p == i]
				if c != [] and path_cost + cost[node][i] <= c[0][0]:  # path to child is less, then update
					child_path = path[:]
					child_path.append(i)
					priority_queue.remove((i,c[0][0],c[0][1]))  
					priority_queue.append((i,path_cost+cost[node][i],child_path))
				
				
		priority_queue = sorted(priority_queue, key = lambda x: x[1])
		# print(priority_queue)
		
	# print(path)
	# print(GOALS)
	GOALS = {k: v for k, v in sorted(GOALS.items(), key=lambda item: item[1][0])}
	
	try:
		cost,l = GOALS.pop(list(GOALS.keys())[0])
	except:
		pass
	
	# print(cost)
	
	return l

def DFS_Traversal(
	#add your parameters 
):
	l = []

	return l


'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you can call in the given fucntion
'''

def tri_traversal(cost, heuristic, start_point, goals):
	l = []

	t1 = DFS_Traversal()
	
	t2 = UCS_Traversal(cost,start_point,goals)
	
	t3 = A_star_Traversal(cost, heuristic, start_point, goals)

	l.append(t1)
	l.append(t2)
	l.append(t3)

	return l
=======


def UCS_Traversal(cost, start_point, goals):
   
    l = []
    return l

def recursive_dfs(cost,start,goals,path,explored_list):

	explored_list[start] = 1		#explored set , mark a node to prevent cyclic looping

	for goal in goals:				#check if the current node is any of the  goal node

		if start == goal:			#if yes add to path list 

			path.append(start)

			path.append("END")
		
			return path				#return the path list 

	

	path.append(start)				#since we're currently here , this node is along the path

	dead_end = 1
	
	for node in range(1,len(cost)): #looking at all the adjacent and reachable neighs from this node
		
		if cost[start][node] > 0 and explored_list[node]==0:	#neigh that is reachable and yet to be visited 

			dead_end = 0
			
			print('*'*10*start)
			print(start ,"------>",node)						#current edge
			print("explored :: ", explored_list)				#current explored list
			print("pre path :: ",path)								#displaying path list
			 
			recursive_dfs(cost, node, goals, path, explored_list) #call recursive dfs on current neighbor

			print("post path in ",start," :: ",path)

			if(path[-1]=="END"):

				return path






			

	if(dead_end):

		path.pop()
		print('popping out  ', start)

	elif(path[-1] != 'END'):
		path.pop()
			
	return path 






	




def DFS_Traversal(cost,start,goals):

    path =[]


    explored_list = [0 for i in range(0,len(cost))]


    node_route = recursive_dfs(cost,start,goals,path,explored_list)


    return node_route[:-1]


class node:

	def __init__(self,child,parent,cost):

		self.child = child
		self.parent = parent
		self.cost = cost

	def get_child(self):

		return self.child


	





def UCS_Traversal(cost,start,goals):

	print('*'*10,"UCS BEGINS")

	
	frontier =[]

	explored = [0 for i in range(0,len(cost))]

	frontier.append(node(start,start,0))	
	
	
	while len(frontier):

		frontier.sort(key = lambda objs : (objs.cost,objs.child))

		current_node = frontier.pop(0)

		child_value = current_node.get_child()

		print("curr edge ::",child_value)

		explored[child_value] = 1

		for goal in goals:

			if goal == child_value:

				path_list=[]

				back_track = current_node

				while True :

					path_list.insert(0, back_track.get_child())

					back_track = back_track.parent

					if back_track.parent==start:

						path_list.insert(0, back_track.get_child())

						break


				return path_list

		for adj in range(1,len(cost)):

			edge_cost =cost[child_value][adj]

			if explored[adj]==0 and edge_cost > 0:

				new_node = node(adj,current_node, edge_cost+current_node.cost)

				print(child_value,">>>>>>",adj," :: ",edge_cost)

				frontier.append(new_node)

		print(explored)
        
        
       return []


'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you can call in the given fucntion
'''

def tri_traversal(cost, heuristic, start_point, goals):
    l = []

    t1 = DFS_Traversal(cost, start_point, goals)

    t2 = UCS_Traversal(cost, start_point, goals)
    
    t3 = A_star_Traversal(cost, heuristic, start_point, goals)
    
    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
>>>>>>> dbdc7526898c1a22d75dbc61ce1443d934592a3d
