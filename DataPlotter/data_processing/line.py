# define a line class to extend pointcollection and have a vector of 10 indices to represent it as a polynomial func

import numpy as np
from data_processing.point import Point
from data_processing.PointCollection import PointCollection


class Line(PointCollection):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.polyFitIndices = np.zeros(10)

    def __str__(self):
        return f'Line({self.points})'

    def __repr__(self):
        return f'Line({self.points})'

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

    def __extrapolate__(self, x):
        # calculate the point using the polynomial function
        y = 0
        for i in range(10):
            y += self.polyFitIndices[i] * x ** i

        return Point(x, y)

    def __setPolyFit__(self, i):
        if i < 0 or i > 9:
            raise ValueError('Index out of range')

        x = [point.x for point in self.points]
        y = [point.y for point in self.points]

        # get the polynomial indices
        self.polyFitIndices = np.polyfit(x, y, i)

    def __getPolyFitOrder__(self):
        # get the order of the polynomial function
        return len(self.polyFitIndices) - 1

    def __setPolyFitDefault__(self):
        self.__setPolyFit__(1)

    def __getPolyFit__(self):
        return self.polyFitIndices

    def __getPolyFitError__(self):
        # calculate the error of the polynomial function
        error = 0
        for point in self.points:
            error += (point.y - self.__extrapolate__(point.x).y) ** 2

        return error

    def __setPolyFitOptimal__(self):
        # find the polyfit with the least error
        errors = []
        for i in range(10):
            self.__setPolyFit__(i)
            errors.append(self.__getPolyFitError__())

        self.__setPolyFit__(np.argmin(errors))

    def __getPolyFitIntegral__(self, a, b, numParts):
        # calculate the integral of the polynomial function
        # break the interval into numParts parts
        # use the trapezoidal rule
        integral = 0
        for i in range(numParts):
            integral += (self.__extrapolate__(a + i * (b - a) / numParts).y +
                         self.__extrapolate__(a + (i + 1) * (b - a) / numParts).y) * (b - a) / numParts / 2

        return integral

    def __getPolyFitDerivative__(self, x):
        # calculate the derivative of the polynomial function
        derivative = 0
        for i in range(1, len(self.polyFitIndices)):
            derivative += i * self.polyFitIndices[i] * x ** (i - 1)

        return derivative
