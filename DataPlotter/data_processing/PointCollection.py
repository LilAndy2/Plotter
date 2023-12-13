# define a class for a collection of 2d points

import numpy as np
from data_processing.point import Point


class PointCollection:
    def __init__(self):
        self.points = []

    def __str__(self):
        return f'PointCollection({self.points})'

    def __addPoint__(self, point):
        self.points.append(point)

    def __addPoints__(self, points):
        self.points.extend(points)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, index):
        return self.points[index]

    def __setitem__(self, index, value):
        self.points[index] = value

    def __delitem__(self, index):
        del self.points[index]

    def __reunite__(self, other):
        self.points.extend(other.points)

    def __intersect__(self, other):
        return [point for point in self.points if point in other.points]
