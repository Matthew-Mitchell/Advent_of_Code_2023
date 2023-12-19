import re

class main:
	def __init__(self):
		self.neighbors = {}
		self.stepcount = 0
		self.node = "AAA"
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

