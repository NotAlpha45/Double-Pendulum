import pygame
import pymunk
import pymunk.pygame_util as util
from circular_body import *
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


IS_RUNNING = True


def main():
    # A physics system that will contain physics object
    space = pymunk.Space()
    # The vector of gravity, (acceleration_x, acceleration_y)
    space.gravity = (0, 900)
    space.damping = 0.999
    b0 = space.static_body
    b0.position = (WIDTH//2, 100)
    bob1_pos = (300, 300)
    bob2_pos = (300, 450)

    obj1 = Circular_body(20, 1, 10, bob1_pos)
    obj2 = Circular_body(20, 1, 10, bob2_pos)

    joint = pymunk.constraints.PinJoint(b0, obj1.obj)
    joint2 = pymunk.constraints.PinJoint(obj1.obj, obj2.obj)
    space.add(joint, joint2)
    obj2.place(space)
    obj1.place(space)
    last_pos = bob2_pos
    curr_pos = (int(space.bodies[0].position[0]),
                int(space.bodies[0].position[1]))

    def draw(space, last_pos, curr_pos):
        '''
        Draws objects on the space and shows them on the screen.
        '''
        screen.fill(WHITE)
        space.debug_draw(util.DrawOptions(screen))
        space.step(0.01)
        pygame.draw.line(screen, RED, last_pos, curr_pos, 2)
        pygame.display.update()

    def reset():
        '''
        Resets the positions of the two bobs
        '''
        bob1_pos = (300, 300)
        bob2_pos = (300, 450)
        space.bodies[0].position = bob2_pos
        space.bodies[1].position = bob1_pos

    clock = pygame.time.Clock()
    global IS_RUNNING
    # last position of bob1
    while IS_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IS_RUNNING = False
            # pygame.KEYDOWN means an event where a key is pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    IS_RUNNING = False
                if event.key == pygame.K_r:
                    reset()

        # print(space.bodies[1].position[1])
        curr_pos = (int(space.bodies[0].position[0]),
                    int(space.bodies[0].position[1]))
        draw(space, last_pos, curr_pos)
        print(last_pos, curr_pos)

        last_pos = curr_pos

        clock.tick(60)


main()
