import turtle
import math 

e = math.e
t = turtle.Turtle()

def lin_func_coords(m, c):
    """Generates coordinate points for a linear function.

    Formula: y = m * x + c

    Args:
        m (float): The slope of the line.
        c (float): The y-intercept (where the line crosses the y-axis).

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = -5
    for i in range(11): # 2 * 5 + 1: multiply by 2 for both directions; 5 is the range; + 1 for the number of shown units to be 10 not 9
        y = m * x + c
        li.append((x, y))
        x += 1
    return li

def quad_func_coords(a, b, c):
    """Generates coordinate points for a quadratic function (parabola).

    Formula: y = a * (x - b)^2 + c

    Args:
        a (float): The vertical stretch/compression and direction factor.
        b (float): The horizontal shift (vertex x-coordinate).
        c (float): The vertical shift (vertex y-coordinate).

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = -5
    for i in range(81):  # -5 to 5 in steps of 0.125
        y = a * (x - b) ** 2 + c
        li.append((x, y))
        x += 0.125
    return li

def sqrt_func_coords(a, b, c):
    """Generates coordinate points for a square root function.

    Formula: y = a * sqrt(x - b) + c

    Args:
        a (float): The vertical stretch or compression factor.
        b (float): The horizontal shift (defines the starting domain point).
        c (float): The vertical shift (starting y-coordinate).

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = b
    for i in range(41):
        y = a * math.sqrt(x - b) + c
        li.append((x, y))
        x += .125
    return li

def log_func_coords(a, b, c):
    """Generates coordinate points for a natural logarithmic function.

    Formula: y = a * log(x - b) + c

    Args:
        a (float): The vertical stretch or compression factor.
        b (float): The horizontal shift (defines the vertical asymptote).
        c (float): The vertical shift.

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = b + .001
    for i in range(41):
        y = a * math.log(x - b) + c
        li.append((x, y))
        x += .125
    return li

def exp_func_coords(a, b):
    """Generates coordinate points for an exponential function.

    Formula: y = a * b^x

    Args:
        a (float): The initial value or vertical scaling factor.
        b (float/str): The base of the exponent (e.g., a number or the string 'e').

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = -5
    for i in range(81):
        y = a * b ** x
        li.append((x, y))
        x += .125
    return li

def recip_func_coords(a, b, c):
    """Generates split coordinate points for a reciprocal rational function.

    Formula: y = a / (x - b) + c

    Args:
        a (float): The scaling factor.
        b (float): The vertical asymptote position (where x is undefined).
        c (float): The horizontal asymptote position.

    Returns:
        tuple: A tuple containing two lists: (left_branch, right_branch).
    """

    left = []
    right = []
    x = -5
    for i in range(81):
        if abs(x - b) > 0.001:
            y = a / (x - b) + c
            if x < b:
                left.append((x, y))
            else:
                right.append((x, y))
        x += 0.125
    return left, right

def abs_func_coords(a, b, c):
    """Generates coordinate points for an absolute value function.

    Formula: y = a * |x - b| + c

    Args:
        a (float): The slope/stretch factor of the V-shape.
        b (float): The horizontal shift of the vertex.
        c (float): The vertical shift of the vertex.

    Returns:
        list: A list of (x, y) coordinate tuples.
    """

    li = []
    x = -5
    for i in range(81):
        y = a * abs(x - b) + c
        li.append((x, y))
        x += .125
    return li

def _draw_grid(t):
    """Draws the green grid coordinate system on a black background.

    Marks the x and y axes with ticks and unit labels from -5 to 5.

    Args:
        t (turtle.Turtle): The turtle instance responsible for drawing the grid.
    """

    s = turtle.Screen()
    x_range = 5
    y_range = 5
    current_xPos = -500
    current_yPos = -500
    grid_num = -5

    # draws the lines
    s.tracer(0)
    turtle.bgcolor("black")
    t.pencolor("green")
    t.penup()
    t.goto(-500, 0)
    t.pendown()
    t.pensize(3)
    t.goto(500, 0)
    t.penup()
    t.goto(0, -500)
    t.pendown()
    t.goto(0, 500)

    # marks the x units
    for x in range(2 * x_range + 1):
        t.penup()
        t.goto(current_xPos, 10)
        t.pendown()
        t.goto(current_xPos, -10)
        t.penup()
        
        if grid_num == 0:
            t.goto(current_xPos + 19, -35)
        else: 
            t.goto(current_xPos, -35)

        t.write(grid_num, align="center", font=("Arial", 16, "normal"))
        grid_num += 1
        current_xPos += 100

    grid_num = -5

    #marks the y units
    for y in range(2 * y_range + 1):
        t.penup()
        t.goto(10, current_yPos)
        t.pendown()
        t.goto(-10, current_yPos)
        t.penup()

        if grid_num < 0:
            t.goto(-20, current_yPos - 12)
        else:
            t.goto(-18, current_yPos - 12)

        if grid_num != 0:
            t.write(grid_num, align="center", font=("Arial", 16, "normal"))

        grid_num += 1
        current_yPos += 100

def _init_turtle():
    """Initializes the turtle renderer and draws the baseline background grid.

    Returns:
        turtle.Turtle: The prepared turtle instance configured for plotting.
    """

    t.pensize(3)
    _draw_grid(t)
    return t

def _done_turtle():
    """Finalizes the canvas render, hides the cursor, and keeps the window open."""

    t.hideturtle()
    turtle.update()
    turtle.done()

def draw_lin_func(m, c):
    """Plots a linear function directly onto the grid environment.

    Args:
        m (float): The slope of the line.
        c (float): The y-intercept.
    """

    _init_turtle()

    t.goto(-500, lin_func_coords(m, c)[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    t.goto(500, lin_func_coords(m, c)[10][1] * 100)

    _done_turtle()

def draw_quad_func(a, b, c):
    """Plots a quadratic parabola function onto the grid environment.

    Args:
        a (float): Vertical scale / orientation.
        b (float): Horizontal vertex shift.
        c (float): Vertical vertex shift.
    """

    _init_turtle()

    points = quad_func_coords(a, b, c)
    t.goto(points[0][0] * 100, points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()

def draw_sqrt_func(a, b, c):
    """Plots a square root function onto the grid environment.

    Args:
        a (float): Vertical scale.
        b (float): Horizontal vertex shift.
        c (float): Vertical vertex shift.
    """

    _init_turtle()

    points = sqrt_func_coords(a, b, c)
    t.goto(points[0][0] * 100, points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()

def draw_log_func(a, b, c):
    """Plots a natural logarithmic function onto the grid environment.

    Args:
        a (float): Vertical scale.
        b (float): Horizontal asymptote shift.
        c (float): Vertical shift.
    """

    _init_turtle()

    points = log_func_coords(a, b, c)
    t.goto(points[0][0] * 100, points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()

def draw_exp_func(a, b):
    """Plots an exponential function onto the grid environment.

    Args:
        a (float): Vertical scaling factor.
        b (float/str): Exponent base value (supports 'e' or '-e' strings).
    """
    
    _init_turtle()

    if b == "e":
        b = e
    elif b == "-e":
        b = -e

    points = exp_func_coords(a, b)
    t.goto(points[0][0] * 100, points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()

def draw_recip_func(a, b, c):
    """Plots a reciprocal hyperbola split into left and right asymptotic branches.

    Args:
        a (float): Scaling factor.
        b (float): Vertical asymptote position.
        c (float): Horizontal asymptote position.
    """

    _init_turtle()

    left_points, right_points = recip_func_coords(a, b, c)

    t.goto(left_points[0][0] * 100, left_points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in left_points:
        t.goto(point[0] * 100, point[1] * 100)

    t.penup()
    t.goto(right_points[0][0] * 100, right_points[0][1] * 100)
    t.pendown()
    for point in right_points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()

def draw_abs_func(a, b, c):
    """Plots an absolute value V-shaped function onto the grid environment.

    Args:
        a (float): Slope/stretch of the branches.
        b (float): Horizontal vertex shift.
        c (float): Vertical vertex shift.
    """

    _init_turtle()

    points = abs_func_coords(a, b, c)
    t.goto(points[0][0] * 100, points[0][1] * 100)
    t.pencolor("blue")
    t.pendown()
    for point in points:
        t.goto(point[0] * 100, point[1] * 100)
    
    _done_turtle()
