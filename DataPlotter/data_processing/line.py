# define a line class to extend pointcollection and have a vector of 10 indices to represent it as a polynomial func

import numpy as np
from scipy import integrate

from data_processing.point import Point
from data_processing.PointCollection import PointCollection


class Line(PointCollection):
    def __init__(self, points):
        super().__init__(points)
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
        for i in range(len(self.polyFitIndices)):
            y += self.polyFitIndices[i] * x ** i

        print(x, y, len(self.polyFitIndices))
        return Point(x, y)

    def __setPolyFit__(self, i):
        if i < 0 or i > 9:
            raise ValueError('Index out of range')

        x = [point.x for point in self.points]
        y = [point.y for point in self.points]

        # get the polynomial indices
        self.polyFitIndices = np.polyfit(x, y, i)
        # swap the polyFitIndices array
        self.polyFitIndices = np.flip(self.polyFitIndices)

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
            if 0.1 > self.polyFitIndices[i] > -0.1:
                return
            errors.append(self.__getPolyFitError__())

        # set the polyfit with the lowest error only if the highest order
        # index is not close to 0
        self.__setPolyFit__(errors.index(min(errors)))

    def __getPolyFitIntegral__(self, a, b, numParts):
        x = np.linspace(a, b, round(numParts))
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = self.__extrapolate__(x[i]).y

        print(x, y)
        integral = integrate.trapezoid(y, x)


        print(integral)
        return integral

    def __getPolyFitDerivative__(self, x):
        # calculate the derivative of the polynomial function
        derivative = 0
        for i in range(1, len(self.polyFitIndices)):
            derivative += i * self.polyFitIndices[i] * x ** (i - 1)

        return derivative

    def __integrate__(self, left, right, num_parts):
        return self.__getPolyFitIntegral__(left, right, num_parts)

    def __differentiate__(self, x):
        return self.__getPolyFitDerivative__(x)
