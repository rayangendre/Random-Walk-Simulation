from random import choice
class RandomWalk:
    '''Class to generate random walks'''

    def __init__(self, num_points=5000):
        '''Initialiaze the attributes of a walk'''
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all points in the walk'''

        # keep going until the walk is at a certain length
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)