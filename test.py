
import turtle


def spiral(num_lines, step_size):
    n = 1
    for i in range(num_lines):
        turtle.forward(n*step_size+1)
        turtle.left(90)
        n = n + 1
        if i % 2 == 0:
            n -= 1
    turtle.exitonclick()


if __name__ == '__main__':
    spiral(20, 20)
    