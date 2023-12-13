# predicter class extends pointcollection class
# will support 3 methods of prediction:
# - linear regression
# - decision tree mining
# - clustering -> for predicting the cluster of a new point

import numpy as np
import pandas as pd

from data_processing.point import Point
from data_processing.PointCollection import PointCollection


class Predicter(PointCollection):
    def __init__(self, points):
        super().__init__()
        self.points = points
