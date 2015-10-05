import sys

"""
Briskei apo mia lista grafwn pou pairnei ws orisma ton grafo
me tous perissoterous komvous kai ton epistrefei
"""
def findbiggestgraph(graphslist):
	maxnodes = 0
	for graph in graphslist:
		if maxnodes < len(graph):
			maxnodes = len(graph)
			biggestgraph = graph
	return biggestgraph

"""
Briskei apo ena grafo pou pairnei ws orisma ton komvo me tis
perissoteres syndeseis kai epistrefei ton komvo kai ton arithmo
twn syndesewn aytwn
"""
def findmaxconsnode(biggestgraph):
	metric = maxnode = 0
	for node in biggestgraph:
		if metric < len(biggestgraph[node]):
			metric = len(biggestgraph[node])
			maxnode = node
	return maxnode, metric

"""
Gia kathe komvo pou pairnei ws orisma (node) dimiourgei apo tis syndeseis
toy ena neo grafo (newgraph) o opoios tha prostethei argotera sthn lista
twn grafwn (graphslist). Kai ayth h synarthsh einai DFS.
"""

def makenewgraph(biggestgraph, visited, node, newgraph):
	if visited[node] == True:
		return
	visited[node] = True
	for n in biggestgraph[node]:
		if visited[n] == False:
			makenewgraph(biggestgraph, visited, n, newgraph)
	newgraph[node] = biggestgraph[node]
	del biggestgraph[node]

"""
Me ayth thn synarthsh kai me tis kaloumenes apo aythn katastrefoume to diktyo
symfwna me ton 1o tropo ths ekfwnnhshs. Prwta briskoume ton grafo me tous perissoterous
komvous apo thn graphslist kai katopin se ayton ton grafo briskoume ton komvo pou
tha afairethei mazi me to metriko tou. Katopin afairoume ton komvo apo ton grafo
kai prosthetoume sthn graphslist ton komvo mono tou ws grafo, enw exafanizoume thn
parousia tou apo ton grafo pou briskotan. Apo tous komvous me tous opoioys syndeotan
o komvos pou afairethke briskoume ta epipleon diktya pou prokyptoyn kai ta prosthetoume
ws grafous sthn graphslist. Telos ektypwnoume to periexomeno ths
"""
def max_nodecons(graphslist, maxsignnode):
	biggestgraph = findbiggestgraph(graphslist)
	maxconsnode, metric = findmaxconsnode(biggestgraph)
	graphslist.remove(biggestgraph)
	connections = biggestgraph[maxconsnode]
	del biggestgraph[maxconsnode]
	graphslist.append({maxconsnode:[]})
	for node in connections:
		biggestgraph[node].remove(maxconsnode)
	visited = []
	for i in range(maxsignnode):
		visited.append(False)
	for node in connections:
		newgraph = {}
		makenewgraph(biggestgraph, visited, node, newgraph)
		if newgraph != {}:
			graphslist.append(newgraph)

	print("Removing node:",maxconsnode,"with metric:",metric)
	printgraphs(graphslist)

"""
Kaleitai apo thn findmaxinfluencenode() gia kathe komvo tou megalyterou grafou kai 
epistrefei tous komvous twn opoiwn to syntomotero monopati apo ton komvo pou pairnei
ws orisma einai radius. Sthn ousia einai enas DFS algorithmos me katallhles metatropes
wste na symplhrwnei thn lista twn komvwn (radnodeslist) pou ikanopoioun to krithrio
tou shortest path.
"""
def findradnodes(biggestgraph, visited, radnodeslist, checklist, node, radius, rcount):
	if visited[node] == True or rcount > radius:
		return
	rcount = rcount + 1
	visited[node] = True
	if rcount == radius:
		radnodeslist.append(node)
		return
	for n in biggestgraph[node]:
		if visited[n] == False and n not in checklist:
			findradnodes(biggestgraph, visited, radnodeslist, biggestgraph[node], n, radius, rcount)

"""
Edw gia kahte komvo tou megalyterou apo tous grafous pou yparxoun sthn graphslist
briskoyme to metriko tou symfwna me ton typo ths ekfwnisis kai me thn klhsh ths
synarthshs findradnodes()kai katopin briskoyme ton komvo me to megalytero metriko 
wste meta na ton afairesoume.
"""
def findmaxinfluencenode(biggestgraph, radius, maxsignnode):
	metric = 0
	influence = 0
	influencenode = 0
	for node in biggestgraph:
		radnodeslist = []
		visited = []
		for k in range(maxsignnode):
			visited.append(False)
		findradnodes(biggestgraph, visited, radnodeslist, [], node, radius, -1)
		for n in radnodeslist:
			influence = influence + len(biggestgraph[n]) - 1
		tempmetric = influence * (len(biggestgraph[node]) - 1)
		influence = 0
		if metric < tempmetric:
			metric = tempmetric
			influencenode = node
	return influencenode, metric
	
"""
Me ayth thn synarthsh kai me tis kaloumenes apo aythn katastrefoume to diktyo
symfwna me ton 2o tropo ths ekfwnnhshs. Prwta briskoume ton grafo me tous perissoterous
komvous apo thn graphslist kai katopin se ayton ton grafo briskoume ton komvo pou
tha afairethei mazi me to metriko tou. Katopin afairoume ton komvo apo ton grafo
kai prosthetoume sthn graphslist ton komvo mono tou ws grafo, enw exafanizoume thn
parousia tou apo ton grafo pou briskotan. Apo tous komvous me tous opoioys syndeotan
o komvos pou afairethke briskoume ta epipleon diktya pou prokyptoyn kai ta prosthetoume
ws grafous sthn graphslist. Telos ektypwnoume to periexomeno ths
"""
def collective_influence(graphslist, radius, maxsignnode):
	biggestgraph = findbiggestgraph(graphslist)
	requestnode, metric = findmaxinfluencenode(biggestgraph, radius, maxsignnode)
	graphslist.remove(biggestgraph)
	connections = biggestgraph[requestnode]
	del biggestgraph[requestnode]
	graphslist.append({requestnode:[]})
	for node in connections:
		biggestgraph[node].remove(requestnode)
	visited = []
	for i in range(maxsignnode):
		visited.append(False)
	for node in connections:
		newgraph = {}
		makenewgraph(biggestgraph, visited, node, newgraph)
		if newgraph != {}:
			graphslist.append(newgraph)

	print("Removing node:",requestnode,"with metric:",metric)
	printgraphs(graphslist)
	
"""
Me thn synarthsh ayth ektypwnoume tous grafous pou periexei h graphslist
symfwna me tis ypodeixeis ths ekfwnhshs kai frontizontas oi grafoi na
einai taxinomhmenoi. Ayto ginetai eykola an metatrepsoume ta kleidia enos
evrethriou pou anaparista ena grafo se lista kai katopin efarmosoume sort()
se ayth. Epishs frontizoume na ektypwnetai sthn arxh mexri ton 79 character
(xekinaei apo 0), kai oi ypoloipoi an yparxoun sthn deyterh grammh
"""
def printgraphs(graphslist):
	listmembers = []
	for graph in graphslist:
		listnode = []
		for node in graph:
			listnode.append(node)
		listnode.sort()
		listmembers.append(listnode)
	listmembers.sort()
	for members in listmembers:
		memberstr = 'Size: ' + str(len(members)) + ' members: ' + str(members)
		if len(memberstr) < 80:
			print(memberstr)
		else:
			k = 79
			while	 memberstr[k] != ' ':
				k = k - 1
			print(memberstr[0:k])
			print('   ', memberstr[k+1:])

"""
Einai h kyria synarthsh tou programmatos pou kalei tis ypoloipes synarthshs
meta to parsing twn orismatwn pou exei dwsei o xrhsths. Gia tnn anaparastash
twn graphwn xrhsimopoioyme thn adjacency list pou brisketai mesa se ena
eyrethrio (graph) enw oloi oi grafoi pou prokyptoyn einai kai aytoi eyrethria
mesa se mia lista pou einai h graphlist sto programma. Sthn arxh h lista ayth
periexei mono ton grapho pou diabazoume apo to arxeio. Epishs thn wra pou 
dimiourgoume ton grafo apo to arxeio briskoyme kai to megalytero numero me
to opoio anaparistatai se ayton enas komvos wste na xeroyme argotera to megethos
ths visited list pou tha xrhsimopoihsoume sths opoias kathe thesh (ektos apo thn
prwth) anaparistatai enas komvos.
"""
def main(argv):
	graph = {}
	graphslist = [graph]
	filename = ''
	rounds = 0
	choise = 0
	argsnum = len(argv)
	if argsnum < 2 or argsnum > 4:
		print('usage:network_destruction.py [-c] [-r RADIUS] num_nodes input_file')
		exit()
	if argsnum == 2:
		rounds = int(argv[0])
		filename = argv[1]
		radius = 2
		choise = 1
	elif argsnum == 3:
		rounds = int(argv[1])
		filename = argv[2]
		choise = 2
	else:
		radius = int(argv[1])
		rounds = int(argv[2])
		filename = argv[3]
		choise = 3
	
	fline = ''
	t = []
	node1 = node2 = maxsignnode = 0
	f = open(filename, 'r')
	for fline in f:
		t = fline.split()
		node1 = int(t[0])
		node2 = int(t[1])
		if maxsignnode < node1:
			maxsignnode = node1
		if maxsignnode < node2:
			maxsignnode = node2
		if node1 in graph:
			graph[node1].append(node2)
		else:
			graph[node1] = [node2]
		if node2 in graph:
			graph[node2].append(node1)
		else:
			graph[node2] = [node1]
	printgraphs([graph])
	if choise == 1:
		for round in range(rounds):
			collective_influence(graphslist, radius, maxsignnode + 1)
	elif choise == 2:
		for round in range(rounds):
			max_nodecons(graphslist, maxsignnode + 1)
	else:
		for round in range(rounds):
			collective_influence(graphslist, radius, maxsignnode + 1)


"""
Apo edw xekinaei to programma me thn klhsh ths synarthshs main kathws kai
me to orisma pou periexei tis epiloges tou xrhsth
"""		
if __name__ == "__main__":
	main(sys.argv[1:])