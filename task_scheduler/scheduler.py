"""
@ Schwinn Zhang

This file provides an object called Scheduler that utilizes the Min Queue data structure to schedule tasks
"""
import heapq
class Scheduler(object):

	def __init__(self):
		self.schedule = []
		self.size = 0
		self.table = {} # table hashes rank to task; rank is unique key; task can be repeated

	# rank_and_task shall be a tuple of the form (int, str)
	def add_task(self,rank_and_task):
		assert type(rank_and_task) is tuple
		assert len(rank_and_task) == 2
		rank = rank_and_task[0]
		task = rank_and_task[1]
		assert type(rank) is int
		assert type(task) is str

		if rank in self.table.keys():
			return 'Errro: Rank already exists. Pick a new rank'
		# priority of task depends on rank
		heapq.heappush(self.schedule, rank_and_task)
		self.size += 1
		self.table[rank] = task


	# pop n tasks with the highest priorities, with n default to 1 if not specified
	# note that task is returned and removed from queue 
	def fetch_task(self,n=1):
		if self.size == 0:
			return None 

		if n <= 0:
			return None

		tasks = []
		for _ in range(n):
			try:
				temp = heapq.heappop(self.schedule)
				tasks.append(temp)
				self.size -= 1
			except:
				print('pop an empty queue')
		
		return tasks

	# clear all tasks in the scheduling queue
	def clear_all(self):
		while(self.size):
			self.fetch_task()

		assert self.schedule == []


if __name__ == "__main__":
	print('create schedule')
	alex = Scheduler()
	print('add tasks')
	alex.add_task((1,'brush teeth'))
	alex.add_task((2,'eat breakfast'))
	alex.add_task((3,'commute'))
	alex.add_task((4,'write amazing software'))

	print('fetch a task')
	print(alex.fetch_task())

	print('fetch 2 tasks')
	print(alex.fetch_task(2))

	print('current schedule')	
	print(alex.schedule)
	alex.clear_all()
	print('after clear all')
	print(alex.schedule)
