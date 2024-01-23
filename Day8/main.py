import re
import sys

class main:
	def __init__(self):
		self.neighbors = {}
		self.stepcount = 0
		self.stepcount2 = 0
		self.node = "AAA"
		self.p2nodes = None
		self.p2node_cycles = None
		#Increase Recursion Limit
		sys.setrecursionlimit(16385)
	def read(self, filename):
		neighbors = self.neighbors
		with open(filename) as f:
			nodes = []
			count = 0
			for line in f.readlines():
				if count == 0:
					self.directions = line.strip()
					count += 1
				elif line.strip() == "":
					continue
				else:
					# print(line)
					matches = re.findall("([A-Z]{3}) = [(]([A-Z]{3}), ([A-Z]{3})[)]", line)
					# print(matches)
					assert len(matches[0]) == 3, "Else error parsing input file. "
					node, left, right = matches[0]
					nodes.append(node)
					neighbors[node] = (left, right)
		self.neighbors = neighbors
		self.nodes = nodes
	def pathlength(self):
		#follow instructions
		for c in self.directions:
			cur_node = self.node
			self.stepcount += 1
			LR = self.neighbors[cur_node]
			if c == "L":
				next_node = LR[0]
			elif c == "R":
				next_node = LR[1]
			else:
				assert False , f"Hit Error! Encountered: {c} in instructions."
			self.node = next_node
			#if zzz terminate
			if self.node == "ZZZ":
				# print(f"On step: {self.stepcount} from: {cur_node} to: {next_node} via: {c}")
				print(f"Journey Completed! Process took: {self.stepcount}")
				#Exit
				return None
			elif self.stepcount % 100 == 0:
				pass
				#print(f"On step: {self.stepcount} from: {cur_node} to: {next_node} via: {c}")				
		#If ZZZ not found, continue searching!
		self.pathlength()
	def traverse_p2_path(self):
		start_node = self.node
		cur_node = start_node
		stepcount = 0 #reset step count
		zcount = 0
		node_zzzs = []
		for c in self.directions:
			stepcount += 1
			LR = self.neighbors[cur_node]
			if c == "L":
				next_node = LR[0]
			elif c == "R":
				next_node = LR[1]
			else:
				assert False , f"Hit Error! Encountered: {c} in instructions."
			cur_node = next_node
			#Record if Ends in Z....
			if next_node[-1] == "Z":
				node_zzzs.append(stepcount)
				zcount += 1
		self.p2node_zzzs[start_node] = node_zzzs
		self.p2node_maps[start_node] = next_node
		self.p2node_zcount_maps[start_node] = zcount
	def pathlength2(self):
		#follow instructions
		#Instead of recursion, just go ad infinitum:
		if self.p2nodes == None:
			#Initialize p2nodes
			self.p2nodes = [node for node in self.nodes if node[-1]=="A"]
			self.original_p2nodes = self.p2nodes
			self.p2node_maps = {}
			self.p2node_zzzs = {} #Dict of lists
			self.p2node_zcount_maps = {}
		nodes = self.nodes
		for n, node in enumerate(nodes):
			#Where does this node terminate after the direction sequence?
			#What z nodes does it encounter along the journey?
			sys.stdout.write(f"\r On node {node:^6} {n:<4,} of {len(nodes):<4,}    ")
			sys.stdout.flush()
			self.node = node
			self.traverse_p2_path()
		print("Node mappings completed!!!!")
		#Now its up to you! Please Calculate the Journey length based on zzzs and cycles.

