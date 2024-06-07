import pygame
import sys
import random



# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = random.randint(1,50)


        self.speed_y = random.randint(1,5)

        self.speed_x = random.randint(1,5)


    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.y > self.screen.get_height() - self.radius or self.y < 0 + self.radius:
            self.speed_y = -1*self.speed_y
        if self.x > self.screen.get_width() - self.radius or self.x < 0 + self.radius:
            self.speed_x = -1*self.speed_x




    def draw(self):
        pygame.draw.circle(self.screen, (200, 0, 200), (self.x, self.y), self.radius)










# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball = Ball(screen, screen.get_width()/2,screen.get_height()/2)

    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        ball.draw()
        ball.move()

        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
