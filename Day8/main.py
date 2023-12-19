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
	def pathlength2(self):
		#follow instructions
		#Instead of recursion, just go ad infinitum:
		if self.p2nodes == None:
			#Initialize p2nodes
			self.p2nodes = [node for node in self.nodes if node[-1]=="A"]
			self.original_p2nodes = self.p2nodes
			self.p2node_cycles = [None for node in self.p2nodes]
			self.p2node_zzzs = {} #Dict of lists
		while (any([n[-1]!="Z" for n in self.p2nodes])) and (any([x==None for x in self.p2node_cycles])):
			idx = self.stepcount % len(self.directions)
			c = self.directions[idx]
			self.stepcount += 1
			LRs = [self.neighbors[node] for node in self.p2nodes]
			if c == "L":
				next_nodes = [LR[0] for LR in LRs]
			elif c == "R":
				next_nodes = [LR[1] for LR in LRs]
			else:
				assert False , f"Hit Error! Encountered: {c} in instructions."
			self.p2nodes = next_nodes
			#if zzz terminate
			zzzs = [n[-1]=="Z" for n in self.p2nodes]
			nodes_that_reset_in_cycle = [(n, node) for n, node in enumerate(next_nodes) if node == self.original_p2nodes[n]]
			if all(zzzs):
				print(f"On step: {self.stepcount} from: {self.p2nodes} to: {next_nodes} via: {c}")
				print(f"Journey Completed! Process took: {self.stepcount}")
				#Exit
				return None
			
			elif (len(nodes_that_reset_in_cycle) > 0) & (idx == 0):
				for n, node in nodes_that_reset_in_cycle:
					print(f"Node {n}: {node} resets after {self.stepcount} steps.")
					#Update Node cycles
					self.p2node_cycles.pop(n)
					self.p2node_cycles.insert(n, self.stepcount)
			elif any(zzzs):
				for n, TF in enumerate(zzzs):
					if TF:
						node = self.original_p2nodes[n]
						#print(f"Node {n}: {node} ends in Z after {self.stepcount} steps.")
						self.p2node_zzzs[node] = self.stepcount
			elif self.stepcount % 100 == 0:
				sys.stdout.write(f"\rOn step: {self.stepcount:,}            ")
				sys.stdout.flush()
		#If ZZZ not found, continue searching!
		print("While loop completed!!!!")
		# print("This does not occur, since termination is within while loop from return.")
		# print(f"Journey Completed! Process took: {self.stepcount}")
		#Now its up to you! Please Calculate the Journey length based on zzzs and cycles.

