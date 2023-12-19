import re
import sys

class main:
	def __init__(self):
		self.neighbors = {}
		self.stepcount = 0
		self.stepcount2 = 0
		self.node = "AAA"
		self.p2nodes = None
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
		if self.p2nodes == None:
			#Initialize p2nodes
			self.p2nodes = [node for node in self.nodes if node[-1]=="A"]
		for c in self.directions:
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
			if all([n[-1]=="Z" for n in self.p2nodes]):
				print(f"On step: {self.stepcount} from: {self.p2nodes} to: {next_nodes} via: {c}")
				print(f"Journey Completed! Process took: {self.stepcount}")
				#Exit
				return None
			elif self.stepcount % 100 == 0:
				pass
				sys.stdout.write(f"\rOn step: {self.stepcount} from: {self.p2nodes[:2]} to: {next_nodes[:2]} via: {c}")
		#If ZZZ not found, continue searching!
		self.pathlength2()

