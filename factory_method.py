class Logistic(object):
	"""
		Tao ra 1 class van chuyen lam goc
	"""
	def __init__(self):
		super(Logistic, self).__init__()
		self.transport_name = 'truck'
		self.create_transport()

	def create_transport(self):
		pass


class RoadLogistic(Logistic):
	def create_transport(self):
		self.transport_name = 'truck'
		self.deliver_type = Truck().deliver()
		

class SeaLogistic(Logistic):
	def create_transport(self):
		self.transport_name = 'Ship'
		self.deliver_type = Ship().deliver()


class Transport(object):
	"""
	Tao ra 1 class phuong tien van chuyen
	"""
	def __init__(self):
		super(Transport, self).__init__()

	def deliver(self):
		pass


class Truck(Transport):
	def deliver(self):
		return 'Deliver by land in a box'


class Ship(Transport):
	def deliver(self):
		return 'Deliver by sea in a container'


"""
Tao ra 2 Object tuong ung voi 2 loai hinh van chuyen
"""
logistic1 = RoadLogistic()
print(logistic1.__dict__)

logistic2 = SeaLogistic()
print(logistic2.__dict__)