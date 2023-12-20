# predicter class extends pointcollection class
# will support 3 methods of prediction:
# - linear regression
# - decision tree mining
# - clustering -> for predicting the cluster of a new point

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from data_processing.point import Point
from data_processing.PointCollection import PointCollection


class DTM(PointCollection):
    def __init__(self, points):
        super().__init__(points)

    def __str__(self):
        return f'DTM({self.points})'

    def __predictNextPoint__(self):
        # predict the next point using a decision tree
        y = np.array([point.toTuple() for point in self.points])
        x = np.array([i for i in range(len(self.points))])

        # Create a decision tree regressor
        regressor = DecisionTreeRegressor()

        # Train the model
        regressor.fit(x, y)

        # Predict the next point
        next_point = regressor.predict([[len(self.points)]])[0]

        return Point(next_point[0], next_point[1])
