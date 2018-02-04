from flask_restful import Resource, reqparse
from models.item import ItemModel
from matplotlib import pyplot as plt

class Graphing():
   while True:
     item = ItemModel.find_by_measure(name)
     Pyplot.plot([x+1], [item])   
     Pyplot.show()
     
     
