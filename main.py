import turtle


def hilbert(level, angle, step):
    if level == 0:

        return
    # Determine the direction of first move
    turtle.right(angle)
    hilbert(level - 1, -angle, step)
    # Draw first line of the element
    turtle.forward(step)
    turtle.left(angle)

    hilbert(level - 1, angle, step)
    # Draw second line of the element
    turtle.forward(step)

    hilbert(level - 1, angle, step)
    turtle.left(angle)
    # Draw third line of the element
    turtle.forward(step)

    hilbert(level - 1, -angle, step)
    turtle.right(angle)


if __name__ == '__main__':
    level = int(input('Enter the curve level: '))
    # Set default size for whole curve
    size = 500
    # Set default size of element
    each_element_size = size / (2 ** level - 1)
    # Set default element angle
    angle = 90
    # Set pen's speed
    turtle.speed('fastest')
    turtle.penup()
    # Go to initial point
    turtle.goto(-size / 2, size / 2)
    turtle.pendown()
    print(each_element_size)
    hilbert(level, angle, each_element_size)
    turtle.done()
