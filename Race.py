# COMP 1020 Assignment 2 / Yoonha Park u1527485

from Dice import *
from graphics import *

# Make the class for horse
class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.x_pos = 0
        self.dice = Dice(speed)
        self.y_pos = y_pos
        self.image = graphics.Image(Point(self.x_pos+25, self.y_pos), image)
        self.window = window
        self.image.draw(self.window)

    # Make the function to roll the dice and make the images move
    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)
        update()

    # Set the position
    def draw(self):
        self.image.draw(self.window)
       
    # Check if crossed the finish line
    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x


def main():
    # Make the background
    win = GraphWin("Race field", 700, 350)
    win.setBackground(color_rgb(0, 250, 250))

    # Set the images' positions
    horse1_image = "Knight.png"
    horse2_image = "Witch.png"

    # Set the speed and position of the images
    horse1 = Horse(6, 100, horse1_image, win)
    horse2 = Horse(6, 250, horse2_image, win)

    # Draw finish line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.draw(win)
    win.getMouse()

    race_over = False

    while not race_over:

        # Move the images
        horse1.move()
        horse2.move()

        # Print which one is the winner
        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
            race_over = True
            print("Tie")
        elif horse1.crossed_finish_line(650):
            race_over = True
            print("Horse 1 is the winner")
        elif horse2.crossed_finish_line(650):
            race_over = True
            print("Horse 2 is the winner")

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
