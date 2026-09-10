# parent-function-grapher
A modular Python graphing engine designed with absolute abstraction layers to compute and visually render mathematical parent functions.

## 📐 Algorithmic Architecture & Engineering

The engine avoids direct coordinate hardcoding by implementing a strict mathematical translation layer to compute and plot equations dynamically:

1. **Strict Logic-View Abstraction:** Complete structural separation between the mathematical evaluation loop (the backend computation) and the canvas rendering engine (the frontend display module).
2. **Dynamic Cartesian Transformation:** Implements a custom pixel-mapping algorithm that scales abstract mathematical units into exact physical canvas coordinates, enabling perfect visualization across custom viewport sizes.
3. **Private Encapsulation Standards:** Code infrastructure relies on private naming conventions (`_`) to shield critical global scaling states from rendering modules, ensuring clean object boundaries.

---

## 📈 Supported Mathematical Parent Functions

The engine parses and plots core algebraic functional boundaries smoothly by dynamically resolving points across specified domain intervals:

* **Polynomial & Quadratic Functions:** Linear progressions and parabolic curves ($f(x) = ax^2 + bx + c$).
* **Rational & Reciprocal Functions:** Asymptotic handling and hyperbola mapping ($f(x) = \frac{1}{x}$).

---

## ⚙️ Mathematical to Pixel Pipeline

The rendering lifecycle transforms abstract mathematical data points into structural display vectors through the following precise path:

Define Function Interval (Domain [$x_{min}, x_{max}$])
  -> Step Resolution Loop (High-density analytical step generation)
        -> Mathematical Coordinate Evaluation ($x, y$)
              -> **Cartesian Transformation Matrix Call**
                    -> $Pixel_X = (x \times Scale_{Factor}) + Offset_X$
                    -> $Pixel_Y = (y \times Scale_{Factor}) + Offset_Y$
                          -> Vector Translation Command (Pure Turtle Line Draw)

---

## 🛠️ Performance & Layout Configurations

* **Non-Blocking Geometric Grids:** Automatically computes axis lines, dynamic grid markers, and origin targets proportional to the screen boundaries.
* **Pure Python Constraints:** Built entirely without heavy external numeric tracking suites (such as NumPy or Matplotlib), relying entirely on native math pipelines to demonstrate core algebraic programming principles.

## 🚀 How to Run

Ensure you have Python 3.10+ installed. Run the engine framework via your terminal:

### Execution Example:
```python
from ParentFuncs import lin_func_coords, draw_lin_func

# Extract coordinate tracks as a list of tuples
coordinates = lin_func_coords(1, 0)
print(coordinates)

# Plot a function over a specified domain interval
draw_lin_func(1,0)
```
