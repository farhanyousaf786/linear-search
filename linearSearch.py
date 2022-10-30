from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class LinearSearch(QMainWindow):

	number = [1,3,5,7,9,12,14,16,7,8,9,6,5,4,5]

	def __init__(self):
		super().__init__()

		# box title
		self.setWindowTitle("Linear search algorithm")

		# box geometry
		self.setGeometry(100, 100, 600, 400)

		# ui element
		self.UiElement()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiElement(self):

		# start flag
		self.start = False

		# list to hold labels
		self.label_list = []

		# desired value
		self.desired = 11

		# counter for keeping index
		self.counter = 0

		# local counter
		c = 0

		# iterating list of numbers
		for i in self.number:

			# creating label for each number
			label = QLabel(str(i), self)

			# adding background color and border
			label.setStyleSheet("border : 1px solid red; background : white;")

			# aligning the text
			label.setAlignment(Qt.AlignTop)

			# label.setFixedWidth(12)  

			label.setGeometry(50 + c * 30, 50, 20, i * 10 + 10)

			# adding label to the label list
			self.label_list.append(label)

			# incrementing local counter
			c = c + 1




App = QApplication(sys.argv)


linearSearch = LinearSearch()


sys.exit(App.exec())
