from Dice import *
from graphics import *

# Make the class for horse
class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.speed = speed
        self.dice = Dice(speed)
        self.x_pos = 100
        self.y_pos = y_pos
        self.image = image
        self.window = window
        self.image.draw(self.window)

    # Make the function to roll the dice and make the images move
    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)

    # Set the position
    def draw(self):
        self.image.undraw()
        self.image.draw(self.window)
       
    # Check if crossed the finish line
    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x


def main():
    # Make the background
    win = GraphWin("Race field", 700, 350, autoflush=False)
    win.setBackground(color_rgb(0, 250, 250))

    # Set the images' positions
    horse1_image = Image(Point(100, 100), "https://github.com/yulia2432/A2/row/4e06a791633154b8ffab57baa919684cb1989ce0/Horse1.gif")
    horse2_image = Image(Point(100, 250), "https://github.com/yulia2432/A2/row/4e06a791633154b8ffab57baa919684cb1989ce0/Horse2.gif")

    # Set the speed and position of the images
    horse1 = Horse(6, 100, horse1_image, win)
    horse2 = Horse(6, 250, horse2_image, win)

    # Draw finish line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.draw(win)
    win.getMouse()

    race_over = False
    while not race_over:
        win.clear_win()

        # Move the images
        horse1.move()
        horse2.move()
        horse1.draw()
        horse2.draw()
        finish_line.draw(win)
        update(10)

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
