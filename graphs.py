from flask_restful import Resource, reqparse
from models.item import ItemModel
from Matplotlib import Matplotlib.pyplot as plt

class Graphing():
   while True:
     item = ItemModel.find_by_measure(name)
     plt.plot([x+1], [item])   
     plt.show()
     
     
