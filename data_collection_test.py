import unittest
import DataCollection

class dataCollectionTest(unittest.TestCase):
	def setUp(self):
		self.dataCol = DataCollection.dataCollection()

		self.x_card = ['megaminion', 'graveyard', 'archers', 'log', 'tombstone', 'golem', 'fireball', 'zap']
		self.y_card = ['goblingang', 'firespirits', 'lightning', 'skeletonarmy', 'wizard', 'hogrider',
		               'elitebarbarians', 'zap']
		self.winner = 0

	def testRawData(self):
		raw_test = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ' \
		           '0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, ' \
		           '0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, ' \
		           '0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ' \
		           '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\n'
		self.assertEqual(raw_test, self.dataCol.createRawDataSample(self.x_card, self.y_card, self.winner))

	def testApprOneData(self):
		apprOne_test = '1, 3, 1, 1, 3, 4, 1, 1, 2, 4, 2, 4, 1, 1, 2, 0, 0, 2, 2, 0, 6, 2, 1, 3, 2, 3, 3, 5, 1, 0, 3, 0, 0\n'
		self.assertEqual(apprOne_test, self.dataCol.createApprOneDataSample(self.x_card, self.y_card, self.winner))

	def testApprTwoData(self):
		apprTwo_test = '9593, 3.75, 142.2, 1, 3, 2, 1, 22, 4, 1, 2, 4763, 3.875, 234.8, 0, 4, 1, 0, 25, 5, 1, 1, 0\n'
		self.assertEqual(apprTwo_test, self.dataCol.createApprTwoDataSample(self.x_card, self.y_card, self.winner))


if __name__ == '__main__':
	unittest.main()
