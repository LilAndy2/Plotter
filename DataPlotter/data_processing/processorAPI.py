from data_processing.PointCollection import PointCollection as pc
from data_processing.line import Line


class ProcessorAPI:
    def __init__(self):
        self.pointCollection = pc([])
        self.mode = 'none'
        self.polyfitMode = 'default'

    def __str__(self):
        return f'ProcessorAPI({self.pointCollection})'

    def __repr__(self):
        return f'ProcessorAPI({self.pointCollection})'

    # change mode of the dataset (user can choose between line, dtm and none)
    def change_mode(self, mode):
        if mode == 'line':
            self.pointCollection = Line(self.pointCollection.points)
            self.pointCollection.__setPolyFitDefault__()
            self.mode = 'line'
        elif mode == 'none':
            self.pointCollection = pc(self.pointCollection.points)
            self.mode = 'none'
        elif mode == 'dtm':
            self.pointCollection = DTM(self.pointCollection.points)
            self.mode = 'dtm'
        else:
            raise ValueError('Invalid mode')

    # add a point to the collection
    def add_point(self, point):
        self.pointCollection.__addPoint__(point)
        self.pointCollection.__sortPoints__()

    # add a list of points to the collection
    def add_list_points(self, points):
        self.pointCollection.__addPoints__(points)
        self.pointCollection.__sortPoints__()

    # remove a point from the collection
    def remove_point(self, point):
        self.pointCollection.__removePoint__(point)

    # remove a list of points from the collection
    def remove_list_points(self, points):
        for point in points:
            self.remove_point(point)

    def get_points(self):
        return self.pointCollection.points

    def get_x_array(self):
        # get an array of x values from the points array
        return self.pointCollection.__getXArray__()

    def get_y_array(self):
        # get an array of y values from the points array
        return self.pointCollection.__getYArray__()

    def get_mode(self):
        return self.mode

    def get_polyfit_set_order(self, order):
        self.mode = 'line'
        if self.mode == 'line':
            self.pointCollection = Line(self.pointCollection.points)
            self.pointCollection.__setPolyFit__(order)
            return self.pointCollection.__getPolyFit__()
        else:
            raise ValueError('Invalid mode')

    def get_polyfit_indices(self):
        self.pointCollection = Line(self.pointCollection.points)
        if len(self.pointCollection.points) == 0:
            return []
        if self.polyfitMode == 'default':
            self.pointCollection.__setPolyFitDefault__()
        elif self.polyfitMode == 'optimal':
            self.pointCollection.__setPolyFitOptimal__()
        return self.pointCollection.polyFitIndices

    def get_polyfit_lin_reg(self):
        self.mode = 'line'
        self.polyfitMode = 'default'
        return self.get_polyfit_set_order(1)

    def get_polyfit_optimal(self):
        self.mode = 'line'
        self.polyfitMode = 'optimal'
        if self.mode == 'line':
            self.pointCollection = Line(self.pointCollection.points)
            self.pointCollection.__setPolyFitOptimal__()
            return self.pointCollection.__getPolyFit__()
        else:
            raise ValueError('Invalid mode')

    def extrapolate(self, x):
        self.mode = 'line'
        if self.mode == 'line':
            self.pointCollection = Line(self.pointCollection.points)
            if self.polyfitMode == 'default':
                self.pointCollection.__setPolyFitDefault__()
            elif self.polyfitMode == 'optimal':
                self.pointCollection.__setPolyFitOptimal__()
            return self.pointCollection.__extrapolate__(x)
        else:
            raise ValueError('Invalid mode')

    def integrate(self, left, right, accuracy):
        self.pointCollection = Line(self.pointCollection.points)
        self.mode = 'line'
        self.get_polyfit_optimal()
        return self.pointCollection.__integrate__(left, right, len(self.pointCollection.points) * (accuracy * 10))

    def differentiate(self, x):
        if self.mode == 'line':
            self.pointCollection = Line(self.pointCollection.points)
            self.pointCollection.__differentiate__(x)
        else:
            raise ValueError('Invalid mode')

    def reset(self):
        self.pointCollection = pc([])
        self.mode = 'none'
        self.polyfitMode = 'default'

