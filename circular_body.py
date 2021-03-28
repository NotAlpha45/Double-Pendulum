import pymunk
import pymunk.pygame_util as util
class Circular_body():
    def __init__(self, radius, mass, moment, position, obj_type='dynamic'):
        self.radius = radius
        self.mass = mass
        self.moment = moment
        self.position = position
        self.obj_type = obj_type
        self.obj = pymunk.Body(self.mass, self.moment)
        self.obj.position = self.position
        self.obj_body = pymunk.Circle(self.obj, self.radius)

    def place(self, space):
        '''
        Places the body in the given space
        '''
        space.add(self.obj, self.obj_body)
    def simulate(self, screen, space, step):
        '''
        Simulates physics on the object
        '''
        space.debug_draw(util.DrawOptions(screen))
        space.step(step)