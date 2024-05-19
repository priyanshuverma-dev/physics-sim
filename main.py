import sys, random

random.seed(1)  # make the simulation the same each time, easier to debug
import pygame
import pymunk
import pymunk.pygame_util


def add_ball(space):
    mass = 3
    radius = 25
    body = pymunk.Body()  # 1
    x = random.randint(120, 300)
    body.position = x, 50  # 2
    shape = pymunk.Circle(body, radius)  # 3
    shape.mass = mass  # 4
    shape.friction = 1
    space.add(body, shape)  # 5
    return shape


def add_static_L(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)  # 2
    # l2 = pymunk.Segment(body, (-150, 0), (-150, -50), 5)
    l1.friction = 1  # 3
    # l2.friction = 1

    space.add(body, l1)  # 4
    return l1


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Physics Simulation")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 900.0)

    lines = add_static_L(space)
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        space.step(1 / 50.0)

        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)


if __name__ == "__main__":
    main()
