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
			
			if not(visit[i]) and cost[node][i] != -1:
				child_path = path[:]
				child_path.append(i)  
				g = path_cost+cost[node][i]
				f = g + heuristic[i]
				priority_queue.append((i,g,f,child_path))
				visit[i] = 1
			
			if visit[i] and cost[node][i] != -1:
				c = [(q,r,s) for p,q,r,s in priority_queue if p == i] # total_cost
				if c != [] and path_cost + cost[node][i] + heuristic[i] <= c[0][1]:
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

def A_star_Traversal(cost, heuristic, start_point, goals):
    l = []
    size =len(cost[0])
    Visit = []
    Frontier = []
    value = 0

    Frontier.append((start_point,0 + heuristic[start_point]))
    while (Frontier):
        Frontier = sorted(Frontier,key = lambda x:(x[1],x[0]), reverse=True)
        t = Frontier.pop()
        node = t[0]
        value = t[1] - heuristic[node]
        Visit.append(node)
        l.append(t)
        if node in goals:
            n = len(l)
            for i in range(n-1,0,-1):
                if cost[l[i-1][0]][l[i][0]]<= 0 and cost[l[i-1][0]][l[i][0]] != l[i][1]-l[i-1][1]+heuristic[l[i-1][0]]-heuristic[l[i][0]]:
                    l.remove(l[i-1])
            l = [x[0] for x in l]
            return l
        for i in range(1,size):
            if cost[node][i]>0 and i not in Visit:
                p = 1
                for j in Frontier:
                    if i == j[0]:
                        p = 0
                        if cost[node][i]+value+heuristic[i] < j[1]:
                            Frontier.remove((i, j[1]))
                            Frontier.append((i, cost[node][i] + value + heuristic[i]))
                if(p):
                    Frontier.append((i, cost[node][i] + value + heuristic[i]))
    l = []
    return l

def UCS_Traversal(cost, start_point, goals):
    l = []
    size = len(cost[0])
    Visit = []
    Frontier = []
    value = 0

    Frontier.append((start_point,0))
    while (Frontier):
        Frontier = sorted(Frontier,key = lambda x:(x[1],x[0]), reverse=True)
        t = Frontier.pop()
        node = t[0]
        value = t[1]
        Visit.append(node)
        l.append(t)
        if node in goals:
            n = len(l)
            for i in range(n-1,0,-1):
                if cost[l[i-1][0]][l[i][0]] != l[i][1]-l[i-1][1]:
                    l.remove(l[i-1])
            l = [x[0] for x in l]
            return l
        for i in range(1,size):
            if cost[node][i]>0 and i not in Visit:
                p = 1
                for j in Frontier:
                    if i == j[0]:
                        p = 0
                        if cost[node][i]+value < j[1]:
                            Frontier.remove((i, j[1]))
                            Frontier.append((i, cost[node][i] + value))
                if(p):
                    Frontier.append((i, cost[node][i] + value))
    l = []
    return l

def DFS_Traversal(cost, start_point, goals):
    l = []
    size = len(cost[0]) - 1
    Visit = []
    Frontier = []

    Frontier.append(start_point)
    while (Frontier):
        node = Frontier.pop()
        Visit.append(node)
        l.append(node)
        if node in goals:
            return l
        p = 0
        for i in range(size,0,-1):
            if cost[node][i]>0 and i not in Visit:
                if i in Frontier:
                    Frontier.remove(i)
                Frontier.append(i)
                p = 1
        if p==0:
            l.pop()
            while(l and Frontier and cost[l[-1]][Frontier[-1]]<=0):
                l.pop()
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

    t1 = DFS_Traversal(cost, start_point, goals)

    t2 = UCS_Traversal(cost, start_point, goals)
    
    t3 = A_star_Traversal(cost, heuristic, start_point, goals)
    
    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
>>>>>>> 065f731a84d350970eb273939dd165829b4c4562
