### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](development.html "Development Tools") |
* [previous](idle.html "IDLE — Python editor and shell") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `turtle` — Turtle graphics
* |
* Theme
  Auto
  Light
  Dark
   |

# `turtle` — Turtle graphics[¶](#module-turtle "Link to this heading")

**Source code:** [Lib/turtle.py](https://github.com/python/cpython/tree/3.14/Lib/turtle.py)

---

## Introduction[¶](#introduction "Link to this heading")

Turtle graphics is an implementation of [the popular geometric drawing tools
introduced in Logo](https://en.wikipedia.org/wiki/Turtle_(robot)), developed by Wally Feurzeig, Seymour Papert and Cynthia Solomon
in 1967.

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

## Get started[¶](#get-started "Link to this heading")

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an `import turtle`, give it the
command `turtle.forward(15)`, and it moves (on-screen!) 15 pixels in the
direction it is facing, drawing a line as it moves. Give it the command
`turtle.right(25)`, and it rotates in-place 25 degrees clockwise.

Turtle star

Turtle can draw intricate shapes using programs that repeat simple
moves.

![../_images/turtle-star.png](../_images/turtle-star.png)

In Python, turtle graphics provides a representation of a physical “turtle”
(a little robot with a pen) that draws on a sheet of paper on the floor.

It’s an effective and well-proven way for learners to encounter
programming concepts and interaction with software, as it provides instant,
visible feedback. It also provides convenient access to graphical output
in general.

Turtle drawing was originally created as an educational tool, to be used by
teachers in the classroom. For the programmer who needs to produce some
graphical output it can be a way to do that without the overhead of
introducing more complex or external libraries into their work.

## Tutorial[¶](#tutorial "Link to this heading")

New users should start here. In this tutorial we’ll explore some of the
basics of turtle drawing.

### Starting a turtle environment[¶](#starting-a-turtle-environment "Link to this heading")

In a Python shell, import all the objects of the `turtle` module:

```
from turtle import *
```

If you run into a `No module named '_tkinter'` error, you’ll have to
install the [`Tk interface package`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") on your system.

### Basic drawing[¶](#basic-drawing "Link to this heading")

Send the turtle forward 100 steps:

```
forward(100)
```

You should see (most likely, in a new window on your display) a line
drawn by the turtle, heading East. Change the direction of the turtle,
so that it turns 120 degrees left (anti-clockwise):

```
left(120)
```

Let’s continue by drawing a triangle:

```
forward(100)
left(120)
forward(100)
```

Notice how the turtle, represented by an arrow, points in different
directions as you steer it.

Experiment with those commands, and also with `backward()` and
`right()`.

#### Pen control[¶](#pen-control "Link to this heading")

Try changing the color - for example, `color('blue')` - and
width of the line - for example, `width(3)` - and then drawing again.

You can also move the turtle around without drawing, by lifting up the pen:
`up()` before moving. To start drawing again, use `down()`.

#### The turtle’s position[¶](#the-turtle-s-position "Link to this heading")

Send your turtle back to its starting-point (useful if it has disappeared
off-screen):

```
home()
```

The home position is at the center of the turtle’s screen. If you ever need to
know them, get the turtle’s x-y coordinates with:

```
pos()
```

Home is at `(0, 0)`.

And after a while, it will probably help to clear the window so we can start
anew:

```
clearscreen()
```

### Making algorithmic patterns[¶](#making-algorithmic-patterns "Link to this heading")

Using loops, it’s possible to build up geometric patterns:

```
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
```

- which of course, are limited only by the imagination!

Let’s draw the star shape at the top of this page. We want red lines,
filled in with yellow:

```
color('red')
fillcolor('yellow')
```

Just as `up()` and `down()` determine whether lines will be drawn,
filling can be turned on and off:

```
begin_fill()
```

Next we’ll create a loop:

```
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
```

`abs(pos()) < 1` is a good way to know when the turtle is back at its
home position.

Finally, complete the filling:

```
end_fill()
```

(Note that filling only actually takes place when you give the
`end_fill()` command.)

## How to…[¶](#how-to "Link to this heading")

This section covers some typical turtle use-cases and approaches.

### Get started as quickly as possible[¶](#get-started-as-quickly-as-possible "Link to this heading")

One of the joys of turtle graphics is the immediate, visual feedback that’s
available from simple commands - it’s an excellent way to introduce children
to programming ideas, with a minimum of overhead (not just children, of
course).

The turtle module makes this possible by exposing all its basic functionality
as functions, available with `from turtle import *`. The [turtle
graphics tutorial](#turtle-tutorial) covers this approach.

It’s worth noting that many of the turtle commands also have even more terse
equivalents, such as `fd()` for [`forward()`](#turtle.forward "turtle.forward"). These are especially
useful when working with learners for whom typing is not a skill.

> You’ll need to have the [`Tk interface package`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") installed on
> your system for turtle graphics to work. Be warned that this is not
> always straightforward, so check this in advance if you’re planning to
> use turtle graphics with a learner.

### Automatically begin and end filling[¶](#automatically-begin-and-end-filling "Link to this heading")

Starting with Python 3.14, you can use the [`fill()`](#turtle.fill "turtle.fill") [context manager](../glossary.html#term-context-manager)
instead of [`begin_fill()`](#turtle.begin_fill "turtle.begin_fill") and [`end_fill()`](#turtle.end_fill "turtle.end_fill") to automatically begin and
end fill. Here is an example:

```
with fill():
    for i in range(4):
        forward(100)
        right(90)

forward(200)
```

The code above is equivalent to:

```
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()

forward(200)
```

### Use the `turtle` module namespace[¶](#use-the-turtle-module-namespace "Link to this heading")

Using `from turtle import *` is convenient - but be warned that it imports a
rather large collection of objects, and if you’re doing anything but turtle
graphics you run the risk of a name conflict (this becomes even more an issue
if you’re using turtle graphics in a script where other modules might be
imported).

The solution is to use `import turtle` - `fd()` becomes
`turtle.fd()`, `width()` becomes `turtle.width()` and so on. (If typing
“turtle” over and over again becomes tedious, use for example `import turtle
as t` instead.)

### Use turtle graphics in a script[¶](#use-turtle-graphics-in-a-script "Link to this heading")

It’s recommended to use the `turtle` module namespace as described
immediately above, for example:

```
import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
```

Another step is also required though - as soon as the script ends, Python
will also close the turtle’s window. Add:

```
t.mainloop()
```

to the end of the script. The script will now wait to be dismissed and
will not exit until it is terminated, for example by closing the turtle
graphics window.

### Use object-oriented turtle graphics[¶](#use-object-oriented-turtle-graphics "Link to this heading")

See also

[Explanation of the object-oriented interface](#turtle-explanation)

Other than for very basic introductory purposes, or for trying things out
as quickly as possible, it’s more usual and much more powerful to use the
object-oriented approach to turtle graphics. For example, this allows
multiple turtles on screen at once.

In this approach, the various turtle commands are methods of objects (mostly of
`Turtle` objects). You *can* use the object-oriented approach in the shell,
but it would be more typical in a Python script.

The example above then becomes:

```
from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()
```

Note the last line. `t.screen` is an instance of the [`Screen`](#turtle.Screen "turtle.Screen")
that a Turtle instance exists on; it’s created automatically along with
the turtle.

The turtle’s screen can be customised, for example:

```
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")
```

## Turtle graphics reference[¶](#turtle-graphics-reference "Link to this heading")

Note

In the following documentation the argument list for functions is given.
Methods, of course, have the additional first argument *self* which is
omitted here.

### Turtle methods[¶](#turtle-methods "Link to this heading")

Turtle motion
:   Move and draw
    :   [`forward()`](#turtle.forward "turtle.forward") | [`fd()`](#turtle.fd "turtle.fd")

        [`backward()`](#turtle.backward "turtle.backward") | [`bk()`](#turtle.bk "turtle.bk") | [`back()`](#turtle.back "turtle.back")

        [`right()`](#turtle.right "turtle.right") | [`rt()`](#turtle.rt "turtle.rt")

        [`left()`](#turtle.left "turtle.left") | [`lt()`](#turtle.lt "turtle.lt")

        [`goto()`](#turtle.goto "turtle.goto") | [`setpos()`](#turtle.setpos "turtle.setpos") | [`setposition()`](#turtle.setposition "turtle.setposition")

        [`teleport()`](#turtle.teleport "turtle.teleport")

        [`setx()`](#turtle.setx "turtle.setx")

        [`sety()`](#turtle.sety "turtle.sety")

        [`setheading()`](#turtle.setheading "turtle.setheading") | [`seth()`](#turtle.seth "turtle.seth")

        [`home()`](#turtle.home "turtle.home")

        [`circle()`](#turtle.circle "turtle.circle")

        [`dot()`](#turtle.dot "turtle.dot")

        [`stamp()`](#turtle.stamp "turtle.stamp")

        [`clearstamp()`](#turtle.clearstamp "turtle.clearstamp")

        [`clearstamps()`](#turtle.clearstamps "turtle.clearstamps")

        [`undo()`](#turtle.undo "turtle.undo")

        [`speed()`](#turtle.speed "turtle.speed")

    Tell Turtle’s state
    :   [`position()`](#turtle.position "turtle.position") | [`pos()`](#turtle.pos "turtle.pos")

        [`towards()`](#turtle.towards "turtle.towards")

        [`xcor()`](#turtle.xcor "turtle.xcor")

        [`ycor()`](#turtle.ycor "turtle.ycor")

        [`heading()`](#turtle.heading "turtle.heading")

        [`distance()`](#turtle.distance "turtle.distance")

    Setting and measurement
    :   [`degrees()`](#turtle.degrees "turtle.degrees")

        [`radians()`](#turtle.radians "turtle.radians")

Pen control
:   Drawing state
    :   [`pendown()`](#turtle.pendown "turtle.pendown") | [`pd()`](#turtle.pd "turtle.pd") | [`down()`](#turtle.down "turtle.down")

        [`penup()`](#turtle.penup "turtle.penup") | [`pu()`](#turtle.pu "turtle.pu") | [`up()`](#turtle.up "turtle.up")

        [`pensize()`](#turtle.pensize "turtle.pensize") | [`width()`](#turtle.width "turtle.width")

        [`pen()`](#turtle.pen "turtle.pen")

        [`isdown()`](#turtle.isdown "turtle.isdown")

    Color control
    :   [`color()`](#turtle.color "turtle.color")

        [`pencolor()`](#turtle.pencolor "turtle.pencolor")

        [`fillcolor()`](#turtle.fillcolor "turtle.fillcolor")

    Filling
    :   [`filling()`](#turtle.filling "turtle.filling")

        [`fill()`](#turtle.fill "turtle.fill")

        [`begin_fill()`](#turtle.begin_fill "turtle.begin_fill")

        [`end_fill()`](#turtle.end_fill "turtle.end_fill")

    More drawing control
    :   [`reset()`](#turtle.reset "turtle.reset")

        [`clear()`](#turtle.clear "turtle.clear")

        [`write()`](#turtle.write "turtle.write")

Turtle state
:   Visibility
    :   [`showturtle()`](#turtle.showturtle "turtle.showturtle") | [`st()`](#turtle.st "turtle.st")

        [`hideturtle()`](#turtle.hideturtle "turtle.hideturtle") | [`ht()`](#turtle.ht "turtle.ht")

        [`isvisible()`](#turtle.isvisible "turtle.isvisible")

    Appearance
    :   [`shape()`](#turtle.shape "turtle.shape")

        [`resizemode()`](#turtle.resizemode "turtle.resizemode")

        [`shapesize()`](#turtle.shapesize "turtle.shapesize") | [`turtlesize()`](#turtle.turtlesize "turtle.turtlesize")

        [`shearfactor()`](#turtle.shearfactor "turtle.shearfactor")

        [`tiltangle()`](#turtle.tiltangle "turtle.tiltangle")

        [`tilt()`](#turtle.tilt "turtle.tilt")

        [`shapetransform()`](#turtle.shapetransform "turtle.shapetransform")

        [`get_shapepoly()`](#turtle.get_shapepoly "turtle.get_shapepoly")

Using events
:   [`onclick()`](#turtle.onclick "turtle.onclick")

    [`onrelease()`](#turtle.onrelease "turtle.onrelease")

    [`ondrag()`](#turtle.ondrag "turtle.ondrag")

Special Turtle methods
:   [`poly()`](#turtle.poly "turtle.poly")

    [`begin_poly()`](#turtle.begin_poly "turtle.begin_poly")

    [`end_poly()`](#turtle.end_poly "turtle.end_poly")

    [`get_poly()`](#turtle.get_poly "turtle.get_poly")

    [`clone()`](#turtle.clone "turtle.clone")

    [`getturtle()`](#turtle.getturtle "turtle.getturtle") | [`getpen()`](#turtle.getpen "turtle.getpen")

    [`getscreen()`](#turtle.getscreen "turtle.getscreen")

    [`setundobuffer()`](#turtle.setundobuffer "turtle.setundobuffer")

    [`undobufferentries()`](#turtle.undobufferentries "turtle.undobufferentries")

### Methods of TurtleScreen/Screen[¶](#methods-of-turtlescreen-screen "Link to this heading")

Window control
:   [`bgcolor()`](#turtle.bgcolor "turtle.bgcolor")

    [`bgpic()`](#turtle.bgpic "turtle.bgpic")

    [`clearscreen()`](#turtle.clearscreen "turtle.clearscreen")

    [`resetscreen()`](#turtle.resetscreen "turtle.resetscreen")

    [`screensize()`](#turtle.screensize "turtle.screensize")

    [`setworldcoordinates()`](#turtle.setworldcoordinates "turtle.setworldcoordinates")

Animation control
:   [`no_animation()`](#turtle.no_animation "turtle.no_animation")

    [`delay()`](#turtle.delay "turtle.delay")

    [`tracer()`](#turtle.tracer "turtle.tracer")

    [`update()`](#turtle.update "turtle.update")

Using screen events
:   [`listen()`](#turtle.listen "turtle.listen")

    [`onkey()`](#turtle.onkey "turtle.onkey") | [`onkeyrelease()`](#turtle.onkeyrelease "turtle.onkeyrelease")

    [`onkeypress()`](#turtle.onkeypress "turtle.onkeypress")

    [`onclick()`](#turtle.onclick "turtle.onclick") | [`onscreenclick()`](#turtle.onscreenclick "turtle.onscreenclick")

    [`ontimer()`](#turtle.ontimer "turtle.ontimer")

    [`mainloop()`](#turtle.mainloop "turtle.mainloop") | [`done()`](#turtle.done "turtle.done")

Settings and special methods
:   [`mode()`](#turtle.mode "turtle.mode")

    [`colormode()`](#turtle.colormode "turtle.colormode")

    [`getcanvas()`](#turtle.getcanvas "turtle.getcanvas")

    [`getshapes()`](#turtle.getshapes "turtle.getshapes")

    [`register_shape()`](#turtle.register_shape "turtle.register_shape") | [`addshape()`](#turtle.addshape "turtle.addshape")

    [`turtles()`](#turtle.turtles "turtle.turtles")

    [`window_height()`](#turtle.window_height "turtle.window_height")

    [`window_width()`](#turtle.window_width "turtle.window_width")

Input methods
:   [`textinput()`](#turtle.textinput "turtle.textinput")

    [`numinput()`](#turtle.numinput "turtle.numinput")

Methods specific to Screen
:   [`bye()`](#turtle.bye "turtle.bye")

    [`exitonclick()`](#turtle.exitonclick "turtle.exitonclick")

    [`save()`](#turtle.save "turtle.save")

    [`setup()`](#turtle.setup "turtle.setup")

    [`title()`](#turtle.title "turtle.title")

## Methods of RawTurtle/Turtle and corresponding functions[¶](#methods-of-rawturtle-turtle-and-corresponding-functions "Link to this heading")

Most of the examples in this section refer to a Turtle instance called
`turtle`.

### Turtle motion[¶](#turtle-motion "Link to this heading")

turtle.forward(*distance*)[¶](#turtle.forward "Link to this definition")

turtle.fd(*distance*)[¶](#turtle.fd "Link to this definition")
:   Parameters:
    :   **distance** – a number (integer or float)

    Move the turtle forward by the specified *distance*, in the direction the
    turtle is headed.

    ```
    >>> turtle.position()
    (0.00,0.00)
    >>> turtle.forward(25)
    >>> turtle.position()
    (25.00,0.00)
    >>> turtle.forward(-75)
    >>> turtle.position()
    (-50.00,0.00)
    ```

turtle.back(*distance*)[¶](#turtle.back "Link to this definition")

turtle.bk(*distance*)[¶](#turtle.bk "Link to this definition")

turtle.backward(*distance*)[¶](#turtle.backward "Link to this definition")
:   Parameters:
    :   **distance** – a number

    Move the turtle backward by *distance*, opposite to the direction the
    turtle is headed. Do not change the turtle’s heading.

    ```
    >>> turtle.position()
    (0.00,0.00)
    >>> turtle.backward(30)
    >>> turtle.position()
    (-30.00,0.00)
    ```

turtle.right(*angle*)[¶](#turtle.right "Link to this definition")

turtle.rt(*angle*)[¶](#turtle.rt "Link to this definition")
:   Parameters:
    :   **angle** – a number (integer or float)

    Turn turtle right by *angle* units. (Units are by default degrees, but
    can be set via the [`degrees()`](#turtle.degrees "turtle.degrees") and [`radians()`](#turtle.radians "turtle.radians") functions.) Angle
    orientation depends on the turtle mode, see [`mode()`](#turtle.mode "turtle.mode").

    ```
    >>> turtle.heading()
    22.0
    >>> turtle.right(45)
    >>> turtle.heading()
    337.0
    ```

turtle.left(*angle*)[¶](#turtle.left "Link to this definition")

turtle.lt(*angle*)[¶](#turtle.lt "Link to this definition")
:   Parameters:
    :   **angle** – a number (integer or float)

    Turn turtle left by *angle* units. (Units are by default degrees, but
    can be set via the [`degrees()`](#turtle.degrees "turtle.degrees") and [`radians()`](#turtle.radians "turtle.radians") functions.) Angle
    orientation depends on the turtle mode, see [`mode()`](#turtle.mode "turtle.mode").

    ```
    >>> turtle.heading()
    22.0
    >>> turtle.left(45)
    >>> turtle.heading()
    67.0
    ```

turtle.goto(*x*, *y=None*)[¶](#turtle.goto "Link to this definition")

turtle.setpos(*x*, *y=None*)[¶](#turtle.setpos "Link to this definition")

turtle.setposition(*x*, *y=None*)[¶](#turtle.setposition "Link to this definition")
:   Parameters:
    :   * **x** – a number or a pair/vector of numbers
        * **y** – a number or `None`

    If *y* is `None`, *x* must be a pair of coordinates or a [`Vec2D`](#turtle.Vec2D "turtle.Vec2D")
    (e.g. as returned by [`pos()`](#turtle.pos "turtle.pos")).

    Move turtle to an absolute position. If the pen is down, draw line. Do
    not change the turtle’s orientation.

    ```
    >>> tp = turtle.pos()
    >>> tp
    (0.00,0.00)
    >>> turtle.setpos(60,30)
    >>> turtle.pos()
    (60.00,30.00)
    >>> turtle.setpos((20,80))
    >>> turtle.pos()
    (20.00,80.00)
    >>> turtle.setpos(tp)
    >>> turtle.pos()
    (0.00,0.00)
    ```

turtle.teleport(*x*, *y=None*, *\**, *fill\_gap=False*)[¶](#turtle.teleport "Link to this definition")
:   Parameters:
    :   * **x** – a number or `None`
        * **y** – a number or `None`
        * **fill\_gap** – a boolean

    Move turtle to an absolute position. Unlike goto(x, y), a line will not
    be drawn. The turtle’s orientation does not change. If currently
    filling, the polygon(s) teleported from will be filled after leaving,
    and filling will begin again after teleporting. This can be disabled
    with fill\_gap=True, which makes the imaginary line traveled during
    teleporting act as a fill barrier like in goto(x, y).

    ```
    >>> tp = turtle.pos()
    >>> tp
    (0.00,0.00)
    >>> turtle.teleport(60)
    >>> turtle.pos()
    (60.00,0.00)
    >>> turtle.teleport(y=10)
    >>> turtle.pos()
    (60.00,10.00)
    >>> turtle.teleport(20, 30)
    >>> turtle.pos()
    (20.00,30.00)
    ```

    Added in version 3.12.

turtle.setx(*x*)[¶](#turtle.setx "Link to this definition")
:   Parameters:
    :   **x** – a number (integer or float)

    Set the turtle’s first coordinate to *x*, leave second coordinate
    unchanged.

    ```
    >>> turtle.position()
    (0.00,240.00)
    >>> turtle.setx(10)
    >>> turtle.position()
    (10.00,240.00)
    ```

turtle.sety(*y*)[¶](#turtle.sety "Link to this definition")
:   Parameters:
    :   **y** – a number (integer or float)

    Set the turtle’s second coordinate to *y*, leave first coordinate unchanged.

    ```
    >>> turtle.position()
    (0.00,40.00)
    >>> turtle.sety(-10)
    >>> turtle.position()
    (0.00,-10.00)
    ```

turtle.setheading(*to\_angle*)[¶](#turtle.setheading "Link to this definition")

turtle.seth(*to\_angle*)[¶](#turtle.seth "Link to this definition")
:   Parameters:
    :   **to\_angle** – a number (integer or float)

    Set the orientation of the turtle to *to\_angle*. Here are some common
    directions in degrees:

    | standard mode | logo mode |
    | --- | --- |
    | 0 - east | 0 - north |
    | 90 - north | 90 - east |
    | 180 - west | 180 - south |
    | 270 - south | 270 - west |

    ```
    >>> turtle.setheading(90)
    >>> turtle.heading()
    90.0
    ```

turtle.home()[¶](#turtle.home "Link to this definition")
:   Move turtle to the origin – coordinates (0,0) – and set its heading to
    its start-orientation (which depends on the mode, see [`mode()`](#turtle.mode "turtle.mode")).

    ```
    >>> turtle.heading()
    90.0
    >>> turtle.position()
    (0.00,-10.00)
    >>> turtle.home()
    >>> turtle.position()
    (0.00,0.00)
    >>> turtle.heading()
    0.0
    ```

turtle.circle(*radius*, *extent=None*, *steps=None*)[¶](#turtle.circle "Link to this definition")
:   Parameters:
    :   * **radius** – a number
        * **extent** – a number (or `None`)
        * **steps** – an integer (or `None`)

    Draw a circle with given *radius*. The center is *radius* units left of
    the turtle; *extent* – an angle – determines which part of the circle
    is drawn. If *extent* is not given, draw the entire circle. If *extent*
    is not a full circle, one endpoint of the arc is the current pen
    position. Draw the arc in counterclockwise direction if *radius* is
    positive, otherwise in clockwise direction. Finally the direction of the
    turtle is changed by the amount of *extent*.

    As the circle is approximated by an inscribed regular polygon, *steps*
    determines the number of steps to use. If not given, it will be
    calculated automatically. May be used to draw regular polygons.

    ```
    >>> turtle.home()
    >>> turtle.position()
    (0.00,0.00)
    >>> turtle.heading()
    0.0
    >>> turtle.circle(50)
    >>> turtle.position()
    (-0.00,0.00)
    >>> turtle.heading()
    0.0
    >>> turtle.circle(120, 180)  # draw a semicircle
    >>> turtle.position()
    (0.00,240.00)
    >>> turtle.heading()
    180.0
    ```

turtle.dot()[¶](#turtle.dot "Link to this definition")

turtle.dot(*size*)

turtle.dot(*color*, */*)

turtle.dot(*size*, *color*, */*)

turtle.dot(*size*, *r*, *g*, *b*, */*)
:   Parameters:
    :   * **size** – an integer >= 1 (if given)
        * **color** – a colorstring or a numeric color tuple

    Draw a circular dot with diameter *size*, using *color*. If *size* is
    not given, the maximum of `pensize+4` and `2*pensize` is used.

    ```
    >>> turtle.home()
    >>> turtle.dot()
    >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
    >>> turtle.position()
    (100.00,-0.00)
    >>> turtle.heading()
    0.0
    ```

turtle.stamp()[¶](#turtle.stamp "Link to this definition")
:   Stamp a copy of the turtle shape onto the canvas at the current turtle
    position. Return a stamp\_id for that stamp, which can be used to delete
    it by calling `clearstamp(stamp_id)`.

    ```
    >>> turtle.color("blue")
    >>> stamp_id = turtle.stamp()
    >>> turtle.fd(50)
    ```

turtle.clearstamp(*stampid*)[¶](#turtle.clearstamp "Link to this definition")
:   Parameters:
    :   **stampid** – an integer, must be return value of previous
        [`stamp()`](#turtle.stamp "turtle.stamp") call

    Delete stamp with given *stampid*.

    ```
    >>> turtle.position()
    (150.00,-0.00)
    >>> turtle.color("blue")
    >>> astamp = turtle.stamp()
    >>> turtle.fd(50)
    >>> turtle.position()
    (200.00,-0.00)
    >>> turtle.clearstamp(astamp)
    >>> turtle.position()
    (200.00,-0.00)
    ```

turtle.clearstamps(*n=None*)[¶](#turtle.clearstamps "Link to this definition")
:   Parameters:
    :   **n** – an integer (or `None`)

    Delete all or first/last *n* of turtle’s stamps. If *n* is `None`, delete
    all stamps, if *n* > 0 delete first *n* stamps, else if *n* < 0 delete
    last *n* stamps.

    ```
    >>> for i in range(8):
    ...     unused_stamp_id = turtle.stamp()
    ...     turtle.fd(30)
    >>> turtle.clearstamps(2)
    >>> turtle.clearstamps(-2)
    >>> turtle.clearstamps()
    ```

turtle.undo()[¶](#turtle.undo "Link to this definition")
:   Undo (repeatedly) the last turtle action(s). Number of available
    undo actions is determined by the size of the undobuffer.

    ```
    >>> for i in range(4):
    ...     turtle.fd(50); turtle.lt(80)
    ...
    >>> for i in range(8):
    ...     turtle.undo()
    ```

turtle.speed(*speed=None*)[¶](#turtle.speed "Link to this definition")
:   Parameters:
    :   **speed** – an integer in the range 0..10 or a speedstring (see below)

    Set the turtle’s speed to an integer value in the range 0..10. If no
    argument is given, return current speed.

    If input is a number greater than 10 or smaller than 0.5, speed is set
    to 0. Speedstrings are mapped to speedvalues as follows:

    * “fastest”: 0
    * “fast”: 10
    * “normal”: 6
    * “slow”: 3
    * “slowest”: 1

    Speeds from 1 to 10 enforce increasingly faster animation of line drawing
    and turtle turning.

    Attention: *speed* = 0 means that *no* animation takes
    place. forward/back makes turtle jump and likewise left/right make the
    turtle turn instantly.

    ```
    >>> turtle.speed()
    3
    >>> turtle.speed('normal')
    >>> turtle.speed()
    6
    >>> turtle.speed(9)
    >>> turtle.speed()
    9
    ```

### Tell Turtle’s state[¶](#tell-turtle-s-state "Link to this heading")

turtle.position()[¶](#turtle.position "Link to this definition")

turtle.pos()[¶](#turtle.pos "Link to this definition")
:   Return the turtle’s current location (x,y) (as a [`Vec2D`](#turtle.Vec2D "turtle.Vec2D") vector).

    ```
    >>> turtle.pos()
    (440.00,-0.00)
    ```

turtle.towards(*x*, *y=None*)[¶](#turtle.towards "Link to this definition")
:   Parameters:
    :   * **x** – a number or a pair/vector of numbers or a turtle instance
        * **y** – a number if *x* is a number, else `None`

    Return the angle between the line from turtle position to position specified
    by (x,y), the vector or the other turtle. This depends on the turtle’s start
    orientation which depends on the mode - “standard”/”world” or “logo”.

    ```
    >>> turtle.goto(10, 10)
    >>> turtle.towards(0,0)
    225.0
    ```

turtle.xcor()[¶](#turtle.xcor "Link to this definition")
:   Return the turtle’s x coordinate.

    ```
    >>> turtle.home()
    >>> turtle.left(50)
    >>> turtle.forward(100)
    >>> turtle.pos()
    (64.28,76.60)
    >>> print(round(turtle.xcor(), 5))
    64.27876
    ```

turtle.ycor()[¶](#turtle.ycor "Link to this definition")
:   Return the turtle’s y coordinate.

    ```
    >>> turtle.home()
    >>> turtle.left(60)
    >>> turtle.forward(100)
    >>> print(turtle.pos())
    (50.00,86.60)
    >>> print(round(turtle.ycor(), 5))
    86.60254
    ```

turtle.heading()[¶](#turtle.heading "Link to this definition")
:   Return the turtle’s current heading (value depends on the turtle mode, see
    [`mode()`](#turtle.mode "turtle.mode")).

    ```
    >>> turtle.home()
    >>> turtle.left(67)
    >>> turtle.heading()
    67.0
    ```

turtle.distance(*x*, *y=None*)[¶](#turtle.distance "Link to this definition")
:   Parameters:
    :   * **x** – a number or a pair/vector of numbers or a turtle instance
        * **y** – a number if *x* is a number, else `None`

    Return the distance from the turtle to (x,y), the given vector, or the given
    other turtle, in turtle step units.

    ```
    >>> turtle.home()
    >>> turtle.distance(30,40)
    50.0
    >>> turtle.distance((30,40))
    50.0
    >>> joe = Turtle()
    >>> joe.forward(77)
    >>> turtle.distance(joe)
    77.0
    ```

### Settings for measurement[¶](#settings-for-measurement "Link to this heading")

turtle.degrees(*fullcircle=360.0*)[¶](#turtle.degrees "Link to this definition")
:   Parameters:
    :   **fullcircle** – a number

    Set angle measurement units, i.e. set number of “degrees” for a full circle.
    Default value is 360 degrees.

    ```
    >>> turtle.home()
    >>> turtle.left(90)
    >>> turtle.heading()
    90.0

    >>> # Change angle measurement unit to grad (also known as gon,
    >>> # grade, or gradian and equals 1/100-th of the right angle.)
    >>> turtle.degrees(400.0)
    >>> turtle.heading()
    100.0
    >>> turtle.degrees(360)
    >>> turtle.heading()
    90.0
    ```

turtle.radians()[¶](#turtle.radians "Link to this definition")
:   Set the angle measurement units to radians. Equivalent to
    `degrees(2*math.pi)`.

    ```
    >>> turtle.home()
    >>> turtle.left(90)
    >>> turtle.heading()
    90.0
    >>> turtle.radians()
    >>> turtle.heading()
    1.5707963267948966
    ```

### Pen control[¶](#id1 "Link to this heading")

#### Drawing state[¶](#drawing-state "Link to this heading")

turtle.pendown()[¶](#turtle.pendown "Link to this definition")

turtle.pd()[¶](#turtle.pd "Link to this definition")

turtle.down()[¶](#turtle.down "Link to this definition")
:   Pull the pen down – drawing when moving.

turtle.penup()[¶](#turtle.penup "Link to this definition")

turtle.pu()[¶](#turtle.pu "Link to this definition")

turtle.up()[¶](#turtle.up "Link to this definition")
:   Pull the pen up – no drawing when moving.

turtle.pensize(*width=None*)[¶](#turtle.pensize "Link to this definition")

turtle.width(*width=None*)[¶](#turtle.width "Link to this definition")
:   Parameters:
    :   **width** – a positive number

    Set the line thickness to *width* or return it. If resizemode is set to
    “auto” and turtleshape is a polygon, that polygon is drawn with the same line
    thickness. If no argument is given, the current pensize is returned.

    ```
    >>> turtle.pensize()
    1
    >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
    ```

turtle.pen(*pen=None*, *\*\*pendict*)[¶](#turtle.pen "Link to this definition")
:   Parameters:
    :   * **pen** – a dictionary with some or all of the below listed keys
        * **pendict** – one or more keyword-arguments with the below listed keys as keywords

    Return or set the pen’s attributes in a “pen-dictionary” with the following
    key/value pairs:

    * “shown”: True/False
    * “pendown”: True/False
    * “pencolor”: color-string or color-tuple
    * “fillcolor”: color-string or color-tuple
    * “pensize”: positive number
    * “speed”: number in range 0..10
    * “resizemode”: “auto” or “user” or “noresize”
    * “stretchfactor”: (positive number, positive number)
    * “outline”: positive number
    * “tilt”: number

    This dictionary can be used as argument for a subsequent call to [`pen()`](#turtle.pen "turtle.pen")
    to restore the former pen-state. Moreover one or more of these attributes
    can be provided as keyword-arguments. This can be used to set several pen
    attributes in one statement.

    ```
    >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
    >>> sorted(turtle.pen().items())
    [('fillcolor', 'black'), ('outline', 1), ('pencolor', 'red'),
     ('pendown', True), ('pensize', 10), ('resizemode', 'noresize'),
     ('shearfactor', 0.0), ('shown', True), ('speed', 9),
     ('stretchfactor', (1.0, 1.0)), ('tilt', 0.0)]
    >>> penstate=turtle.pen()
    >>> turtle.color("yellow", "")
    >>> turtle.penup()
    >>> sorted(turtle.pen().items())[:3]
    [('fillcolor', ''), ('outline', 1), ('pencolor', 'yellow')]
    >>> turtle.pen(penstate, fillcolor="green")
    >>> sorted(turtle.pen().items())[:3]
    [('fillcolor', 'green'), ('outline', 1), ('pencolor', 'red')]
    ```

turtle.isdown()[¶](#turtle.isdown "Link to this definition")
:   Return `True` if pen is down, `False` if it’s up.

    ```
    >>> turtle.penup()
    >>> turtle.isdown()
    False
    >>> turtle.pendown()
    >>> turtle.isdown()
    True
    ```

#### Color control[¶](#color-control "Link to this heading")

turtle.pencolor()[¶](#turtle.pencolor "Link to this definition")

turtle.pencolor(*color*, */*)

turtle.pencolor(*r*, *g*, *b*, */*)
:   Return or set the pencolor.

    Four input formats are allowed:

    `pencolor()`
    :   Return the current pencolor as color specification string or
        as a tuple (see example). May be used as input to another
        color/pencolor/fillcolor/bgcolor call.

    `pencolor(colorstring)`
    :   Set pencolor to *colorstring*, which is a Tk color specification string,
        such as `"red"`, `"yellow"`, or `"#33cc8c"`.

    `pencolor((r, g, b))`
    :   Set pencolor to the RGB color represented by the tuple of *r*, *g*, and
        *b*. Each of *r*, *g*, and *b* must be in the range 0..colormode, where
        colormode is either 1.0 or 255 (see [`colormode()`](#turtle.colormode "turtle.colormode")).

    `pencolor(r, g, b)`
    :   Set pencolor to the RGB color represented by *r*, *g*, and *b*. Each of
        *r*, *g*, and *b* must be in the range 0..colormode.

    If turtleshape is a polygon, the outline of that polygon is drawn with the
    newly set pencolor.

    ```
    >>> colormode()
    1.0
    >>> turtle.pencolor()
    'red'
    >>> turtle.pencolor("brown")
    >>> turtle.pencolor()
    'brown'
    >>> tup = (0.2, 0.8, 0.55)
    >>> turtle.pencolor(tup)
    >>> turtle.pencolor()
    (0.2, 0.8, 0.5490196078431373)
    >>> colormode(255)
    >>> turtle.pencolor()
    (51.0, 204.0, 140.0)
    >>> turtle.pencolor('#32c18f')
    >>> turtle.pencolor()
    (50.0, 193.0, 143.0)
    ```

turtle.fillcolor()[¶](#turtle.fillcolor "Link to this definition")

turtle.fillcolor(*color*, */*)

turtle.fillcolor(*r*, *g*, *b*, */*)
:   Return or set the fillcolor.

    Four input formats are allowed:

    `fillcolor()`
    :   Return the current fillcolor as color specification string, possibly
        in tuple format (see example). May be used as input to another
        color/pencolor/fillcolor/bgcolor call.

    `fillcolor(colorstring)`
    :   Set fillcolor to *colorstring*, which is a Tk color specification string,
        such as `"red"`, `"yellow"`, or `"#33cc8c"`.

    `fillcolor((r, g, b))`
    :   Set fillcolor to the RGB color represented by the tuple of *r*, *g*, and
        *b*. Each of *r*, *g*, and *b* must be in the range 0..colormode, where
        colormode is either 1.0 or 255 (see [`colormode()`](#turtle.colormode "turtle.colormode")).

    `fillcolor(r, g, b)`
    :   Set fillcolor to the RGB color represented by *r*, *g*, and *b*. Each of
        *r*, *g*, and *b* must be in the range 0..colormode.

    If turtleshape is a polygon, the interior of that polygon is drawn
    with the newly set fillcolor.

    ```
    >>> turtle.fillcolor("violet")
    >>> turtle.fillcolor()
    'violet'
    >>> turtle.pencolor()
    (50.0, 193.0, 143.0)
    >>> turtle.fillcolor((50, 193, 143))  # Integers, not floats
    >>> turtle.fillcolor()
    (50.0, 193.0, 143.0)
    >>> turtle.fillcolor('#ffffff')
    >>> turtle.fillcolor()
    (255.0, 255.0, 255.0)
    ```

turtle.color()[¶](#turtle.color "Link to this definition")

turtle.color(*color*, */*)

turtle.color(*r*, *g*, *b*, */*)

turtle.color(*pencolor*, *fillcolor*, */*)
:   Return or set pencolor and fillcolor.

    Several input formats are allowed. They use 0 to 3 arguments as
    follows:

    `color()`
    :   Return the current pencolor and the current fillcolor as a pair of color
        specification strings or tuples as returned by [`pencolor()`](#turtle.pencolor "turtle.pencolor") and
        [`fillcolor()`](#turtle.fillcolor "turtle.fillcolor").

    `color(colorstring)`, `color((r,g,b))`, `color(r,g,b)`
    :   Inputs as in [`pencolor()`](#turtle.pencolor "turtle.pencolor"), set both, fillcolor and pencolor, to the
        given value.

    `color(colorstring1, colorstring2)`, `color((r1,g1,b1), (r2,g2,b2))`
    :   Equivalent to `pencolor(colorstring1)` and `fillcolor(colorstring2)`
        and analogously if the other input format is used.

    If turtleshape is a polygon, outline and interior of that polygon is drawn
    with the newly set colors.

    ```
    >>> turtle.color("red", "green")
    >>> turtle.color()
    ('red', 'green')
    >>> color("#285078", "#a0c8f0")
    >>> color()
    ((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))
    ```

See also: Screen method [`colormode()`](#turtle.colormode "turtle.colormode").

#### Filling[¶](#filling "Link to this heading")

turtle.filling()[¶](#turtle.filling "Link to this definition")
:   Return fillstate (`True` if filling, `False` else).

    ```
    >>> turtle.begin_fill()
    >>> if turtle.filling():
    ...    turtle.pensize(5)
    ... else:
    ...    turtle.pensize(3)
    ```

turtle.fill()[¶](#turtle.fill "Link to this definition")
:   Fill the shape drawn in the `with turtle.fill():` block.

    ```
    >>> turtle.color("black", "red")
    >>> with turtle.fill():
    ...     turtle.circle(80)
    ```

    Using `fill()` is equivalent to adding the [`begin_fill()`](#turtle.begin_fill "turtle.begin_fill") before the
    fill-block and [`end_fill()`](#turtle.end_fill "turtle.end_fill") after the fill-block:

    ```
    >>> turtle.color("black", "red")
    >>> turtle.begin_fill()
    >>> turtle.circle(80)
    >>> turtle.end_fill()
    ```

    Added in version 3.14.

turtle.begin\_fill()[¶](#turtle.begin_fill "Link to this definition")
:   To be called just before drawing a shape to be filled.

turtle.end\_fill()[¶](#turtle.end_fill "Link to this definition")
:   Fill the shape drawn after the last call to [`begin_fill()`](#turtle.begin_fill "turtle.begin_fill").

    Whether or not overlap regions for self-intersecting polygons
    or multiple shapes are filled depends on the operating system graphics,
    type of overlap, and number of overlaps. For example, the Turtle star
    above may be either all yellow or have some white regions.

    ```
    >>> turtle.color("black", "red")
    >>> turtle.begin_fill()
    >>> turtle.circle(80)
    >>> turtle.end_fill()
    ```

#### More drawing control[¶](#more-drawing-control "Link to this heading")

turtle.reset()[¶](#turtle.reset "Link to this definition")
:   Delete the turtle’s drawings from the screen, re-center the turtle and set
    variables to the default values.

    ```
    >>> turtle.goto(0,-22)
    >>> turtle.left(100)
    >>> turtle.position()
    (0.00,-22.00)
    >>> turtle.heading()
    100.0
    >>> turtle.reset()
    >>> turtle.position()
    (0.00,0.00)
    >>> turtle.heading()
    0.0
    ```

turtle.clear()[¶](#turtle.clear "Link to this definition")
:   Delete the turtle’s drawings from the screen. Do not move turtle. State and
    position of the turtle as well as drawings of other turtles are not affected.

turtle.write(*arg*, *move=False*, *align='left'*, *font=('Arial', 8, 'normal')*)[¶](#turtle.write "Link to this definition")
:   Parameters:
    :   * **arg** – object to be written to the TurtleScreen
        * **move** – True/False
        * **align** – one of the strings “left”, “center” or right”
        * **font** – a triple (fontname, fontsize, fonttype)

    Write text - the string representation of *arg* - at the current turtle
    position according to *align* (“left”, “center” or “right”) and with the given
    font. If *move* is true, the pen is moved to the bottom-right corner of the
    text. By default, *move* is `False`.

    ```
    >>> turtle.write("Home = ", True, align="center")
    >>> turtle.write((0,0), True)
    ```

### Turtle state[¶](#turtle-state "Link to this heading")

#### Visibility[¶](#visibility "Link to this heading")

turtle.hideturtle()[¶](#turtle.hideturtle "Link to this definition")

turtle.ht()[¶](#turtle.ht "Link to this definition")
:   Make the turtle invisible. It’s a good idea to do this while you’re in the
    middle of doing some complex drawing, because hiding the turtle speeds up the
    drawing observably.

    ```
    >>> turtle.hideturtle()
    ```

turtle.showturtle()[¶](#turtle.showturtle "Link to this definition")

turtle.st()[¶](#turtle.st "Link to this definition")
:   Make the turtle visible.

    ```
    >>> turtle.showturtle()
    ```

turtle.isvisible()[¶](#turtle.isvisible "Link to this definition")
:   Return `True` if the Turtle is shown, `False` if it’s hidden.

    ```
    >>> turtle.hideturtle()
    >>> turtle.isvisible()
    False
    >>> turtle.showturtle()
    >>> turtle.isvisible()
    True
    ```

#### Appearance[¶](#appearance "Link to this heading")

turtle.shape(*name=None*)[¶](#turtle.shape "Link to this definition")
:   Parameters:
    :   **name** – a string which is a valid shapename

    Set turtle shape to shape with given *name* or, if name is not given, return
    name of current shape. Shape with *name* must exist in the TurtleScreen’s
    shape dictionary. Initially there are the following polygon shapes: “arrow”,
    “turtle”, “circle”, “square”, “triangle”, “classic”. To learn about how to
    deal with shapes see Screen method [`register_shape()`](#turtle.register_shape "turtle.register_shape").

    ```
    >>> turtle.shape()
    'classic'
    >>> turtle.shape("turtle")
    >>> turtle.shape()
    'turtle'
    ```

turtle.resizemode(*rmode=None*)[¶](#turtle.resizemode "Link to this definition")
:   Parameters:
    :   **rmode** – one of the strings “auto”, “user”, “noresize”

    Set resizemode to one of the values: “auto”, “user”, “noresize”. If *rmode*
    is not given, return current resizemode. Different resizemodes have the
    following effects:

    * “auto”: adapts the appearance of the turtle corresponding to the value of pensize.
    * “user”: adapts the appearance of the turtle according to the values of
      stretchfactor and outlinewidth (outline), which are set by
      [`shapesize()`](#turtle.shapesize "turtle.shapesize").
    * “noresize”: no adaption of the turtle’s appearance takes place.

    `resizemode("user")` is called by [`shapesize()`](#turtle.shapesize "turtle.shapesize") when used with arguments.

    ```
    >>> turtle.resizemode()
    'noresize'
    >>> turtle.resizemode("auto")
    >>> turtle.resizemode()
    'auto'
    ```

turtle.shapesize(*stretch\_wid=None*, *stretch\_len=None*, *outline=None*)[¶](#turtle.shapesize "Link to this definition")

turtle.turtlesize(*stretch\_wid=None*, *stretch\_len=None*, *outline=None*)[¶](#turtle.turtlesize "Link to this definition")
:   Parameters:
    :   * **stretch\_wid** – positive number
        * **stretch\_len** – positive number
        * **outline** – positive number

    Return or set the pen’s attributes x/y-stretchfactors and/or outline. Set
    resizemode to “user”. If and only if resizemode is set to “user”, the turtle
    will be displayed stretched according to its stretchfactors: *stretch\_wid* is
    stretchfactor perpendicular to its orientation, *stretch\_len* is
    stretchfactor in direction of its orientation, *outline* determines the width
    of the shape’s outline.

    ```
    >>> turtle.shapesize()
    (1.0, 1.0, 1)
    >>> turtle.resizemode("user")
    >>> turtle.shapesize(5, 5, 12)
    >>> turtle.shapesize()
    (5, 5, 12)
    >>> turtle.shapesize(outline=8)
    >>> turtle.shapesize()
    (5, 5, 8)
    ```

turtle.shearfactor(*shear=None*)[¶](#turtle.shearfactor "Link to this definition")
:   Parameters:
    :   **shear** – number (optional)

    Set or return the current shearfactor. Shear the turtleshape according to
    the given shearfactor shear, which is the tangent of the shear angle.
    Do *not* change the turtle’s heading (direction of movement).
    If shear is not given: return the current shearfactor, i. e. the
    tangent of the shear angle, by which lines parallel to the
    heading of the turtle are sheared.

    ```
    >>> turtle.shape("circle")
    >>> turtle.shapesize(5,2)
    >>> turtle.shearfactor(0.5)
    >>> turtle.shearfactor()
    0.5
    ```

turtle.tilt(*angle*)[¶](#turtle.tilt "Link to this definition")
:   Parameters:
    :   **angle** – a number

    Rotate the turtleshape by *angle* from its current tilt-angle, but do *not*
    change the turtle’s heading (direction of movement).

    ```
    >>> turtle.reset()
    >>> turtle.shape("circle")
    >>> turtle.shapesize(5,2)
    >>> turtle.tilt(30)
    >>> turtle.fd(50)
    >>> turtle.tilt(30)
    >>> turtle.fd(50)
    ```

turtle.tiltangle(*angle=None*)[¶](#turtle.tiltangle "Link to this definition")
:   Parameters:
    :   **angle** – a number (optional)

    Set or return the current tilt-angle. If angle is given, rotate the
    turtleshape to point in the direction specified by angle,
    regardless of its current tilt-angle. Do *not* change the turtle’s
    heading (direction of movement).
    If angle is not given: return the current tilt-angle, i. e. the angle
    between the orientation of the turtleshape and the heading of the
    turtle (its direction of movement).

    ```
    >>> turtle.reset()
    >>> turtle.shape("circle")
    >>> turtle.shapesize(5,2)
    >>> turtle.tilt(45)
    >>> turtle.tiltangle()
    45.0
    ```

turtle.shapetransform(*t11=None*, *t12=None*, *t21=None*, *t22=None*)[¶](#turtle.shapetransform "Link to this definition")
:   Parameters:
    :   * **t11** – a number (optional)
        * **t12** – a number (optional)
        * **t21** – a number (optional)
        * **t12** – a number (optional)

    Set or return the current transformation matrix of the turtle shape.

    If none of the matrix elements are given, return the transformation
    matrix as a tuple of 4 elements.
    Otherwise set the given elements and transform the turtleshape
    according to the matrix consisting of first row t11, t12 and
    second row t21, t22. The determinant t11 \* t22 - t12 \* t21 must not be
    zero, otherwise an error is raised.
    Modify stretchfactor, shearfactor and tiltangle according to the
    given matrix.

    ```
    >>> turtle = Turtle()
    >>> turtle.shape("square")
    >>> turtle.shapesize(4,2)
    >>> turtle.shearfactor(-0.5)
    >>> turtle.shapetransform()
    (4.0, -1.0, -0.0, 2.0)
    ```

turtle.get\_shapepoly()[¶](#turtle.get_shapepoly "Link to this definition")
:   Return the current shape polygon as tuple of coordinate pairs. This
    can be used to define a new shape or components of a compound shape.

    ```
    >>> turtle.shape("square")
    >>> turtle.shapetransform(4, -1, 0, 2)
    >>> turtle.get_shapepoly()
    ((50, -20), (30, 20), (-50, 20), (-30, -20))
    ```

### Using events[¶](#using-events "Link to this heading")

turtle.onclick(*fun*, *btn=1*, *add=None*)
:   Parameters:
    :   * **fun** – a function with two arguments which will be called with the
          coordinates of the clicked point on the canvas
        * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
        * **add** – `True` or `False` – if `True`, a new binding will be
          added, otherwise it will replace a former binding

    Bind *fun* to mouse-click events on this turtle. If *fun* is `None`,
    existing bindings are removed. Example for the anonymous turtle, i.e. the
    procedural way:

    ```
    >>> def turn(x, y):
    ...     left(180)
    ...
    >>> onclick(turn)  # Now clicking into the turtle will turn it.
    >>> onclick(None)  # event-binding will be removed
    ```

turtle.onrelease(*fun*, *btn=1*, *add=None*)[¶](#turtle.onrelease "Link to this definition")
:   Parameters:
    :   * **fun** – a function with two arguments which will be called with the
          coordinates of the clicked point on the canvas
        * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
        * **add** – `True` or `False` – if `True`, a new binding will be
          added, otherwise it will replace a former binding

    Bind *fun* to mouse-button-release events on this turtle. If *fun* is
    `None`, existing bindings are removed.

    ```
    >>> class MyTurtle(Turtle):
    ...     def glow(self,x,y):
    ...         self.fillcolor("red")
    ...     def unglow(self,x,y):
    ...         self.fillcolor("")
    ...
    >>> turtle = MyTurtle()
    >>> turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
    >>> turtle.onrelease(turtle.unglow) # releasing turns it to transparent.
    ```

turtle.ondrag(*fun*, *btn=1*, *add=None*)[¶](#turtle.ondrag "Link to this definition")
:   Parameters:
    :   * **fun** – a function with two arguments which will be called with the
          coordinates of the clicked point on the canvas
        * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
        * **add** – `True` or `False` – if `True`, a new binding will be
          added, otherwise it will replace a former binding

    Bind *fun* to mouse-move events on this turtle. If *fun* is `None`,
    existing bindings are removed.

    Remark: Every sequence of mouse-move-events on a turtle is preceded by a
    mouse-click event on that turtle.

    ```
    >>> turtle.ondrag(turtle.goto)
    ```

    Subsequently, clicking and dragging the Turtle will move it across
    the screen thereby producing handdrawings (if pen is down).

### Special Turtle methods[¶](#special-turtle-methods "Link to this heading")

turtle.poly()[¶](#turtle.poly "Link to this definition")
:   Record the vertices of a polygon drawn in the `with turtle.poly():` block.
    The first and last vertices will be connected.

    ```
    >>> with turtle.poly():
    ...     turtle.forward(100)
    ...     turtle.right(60)
    ...     turtle.forward(100)
    ```

    Added in version 3.14.

turtle.begin\_poly()[¶](#turtle.begin_poly "Link to this definition")
:   Start recording the vertices of a polygon. Current turtle position is first
    vertex of polygon.

turtle.end\_poly()[¶](#turtle.end_poly "Link to this definition")
:   Stop recording the vertices of a polygon. Current turtle position is last
    vertex of polygon. This will be connected with the first vertex.

turtle.get\_poly()[¶](#turtle.get_poly "Link to this definition")
:   Return the last recorded polygon.

    ```
    >>> turtle.home()
    >>> turtle.begin_poly()
    >>> turtle.fd(100)
    >>> turtle.left(20)
    >>> turtle.fd(30)
    >>> turtle.left(60)
    >>> turtle.fd(50)
    >>> turtle.end_poly()
    >>> p = turtle.get_poly()
    >>> register_shape("myFavouriteShape", p)
    ```

turtle.clone()[¶](#turtle.clone "Link to this definition")
:   Create and return a clone of the turtle with same position, heading and
    turtle properties.

    ```
    >>> mick = Turtle()
    >>> joe = mick.clone()
    ```

turtle.getturtle()[¶](#turtle.getturtle "Link to this definition")

turtle.getpen()[¶](#turtle.getpen "Link to this definition")
:   Return the Turtle object itself. Only reasonable use: as a function to
    return the “anonymous turtle”:

    ```
    >>> pet = getturtle()
    >>> pet.fd(50)
    >>> pet
    <turtle.Turtle object at 0x...>
    ```

turtle.getscreen()[¶](#turtle.getscreen "Link to this definition")
:   Return the [`TurtleScreen`](#turtle.TurtleScreen "turtle.TurtleScreen") object the turtle is drawing on.
    TurtleScreen methods can then be called for that object.

    ```
    >>> ts = turtle.getscreen()
    >>> ts
    <turtle._Screen object at 0x...>
    >>> ts.bgcolor("pink")
    ```

turtle.setundobuffer(*size*)[¶](#turtle.setundobuffer "Link to this definition")
:   Parameters:
    :   **size** – an integer or `None`

    Set or disable undobuffer. If *size* is an integer, an empty undobuffer of
    given size is installed. *size* gives the maximum number of turtle actions
    that can be undone by the [`undo()`](#turtle.undo "turtle.undo") method/function. If *size* is
    `None`, the undobuffer is disabled.

    ```
    >>> turtle.setundobuffer(42)
    ```

turtle.undobufferentries()[¶](#turtle.undobufferentries "Link to this definition")
:   Return number of entries in the undobuffer.

    ```
    >>> while undobufferentries():
    ...     undo()
    ```

### Compound shapes[¶](#compound-shapes "Link to this heading")

To use compound turtle shapes, which consist of several polygons of different
color, you must use the helper class [`Shape`](#turtle.Shape "turtle.Shape") explicitly as described
below:

1. Create an empty Shape object of type “compound”.
2. Add as many components to this object as desired, using the
   [`addcomponent()`](#turtle.Shape.addcomponent "turtle.Shape.addcomponent") method.

   For example:

   ```
   >>> s = Shape("compound")
   >>> poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
   >>> s.addcomponent(poly1, "red", "blue")
   >>> poly2 = ((0,0),(10,-5),(-10,-5))
   >>> s.addcomponent(poly2, "blue", "red")
   ```
3. Now add the Shape to the Screen’s shapelist and use it:

   ```
   >>> register_shape("myshape", s)
   >>> shape("myshape")
   ```

Note

The [`Shape`](#turtle.Shape "turtle.Shape") class is used internally by the [`register_shape()`](#turtle.register_shape "turtle.register_shape")
method in different ways. The application programmer has to deal with the
Shape class *only* when using compound shapes like shown above!

## Methods of TurtleScreen/Screen and corresponding functions[¶](#methods-of-turtlescreen-screen-and-corresponding-functions "Link to this heading")

Most of the examples in this section refer to a TurtleScreen instance called
`screen`.

### Window control[¶](#window-control "Link to this heading")

turtle.bgcolor()[¶](#turtle.bgcolor "Link to this definition")

turtle.bgcolor(*color*, */*)

turtle.bgcolor(*r*, *g*, *b*, */*)
:   Return or set the background color of the TurtleScreen.

    Four input formats are allowed:

    `bgcolor()`
    :   Return the current background color as color specification string or
        as a tuple (see example). May be used as input to another
        color/pencolor/fillcolor/bgcolor call.

    `bgcolor(colorstring)`
    :   Set the background color to *colorstring*, which is a Tk color
        specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

    `bgcolor((r, g, b))`
    :   Set the background color to the RGB color represented by the tuple of
        *r*, *g*, and *b*.
        Each of *r*, *g*, and *b* must be in the range 0..colormode, where
        colormode is either 1.0 or 255 (see [`colormode()`](#turtle.colormode "turtle.colormode")).

    `bgcolor(r, g, b)`
    :   Set the background color to the RGB color represented by *r*, *g*, and *b*. Each of
        *r*, *g*, and *b* must be in the range 0..colormode.

    ```
    >>> screen.bgcolor("orange")
    >>> screen.bgcolor()
    'orange'
    >>> screen.bgcolor("#800080")
    >>> screen.bgcolor()
    (128.0, 0.0, 128.0)
    ```

turtle.bgpic(*picname=None*)[¶](#turtle.bgpic "Link to this definition")
:   Parameters:
    :   **picname** – a string, name of an image file (PNG, GIF, PGM, and PPM)
        or `"nopic"`, or `None`

    Set background image or return name of current backgroundimage. If *picname*
    is a filename, set the corresponding image as background. If *picname* is
    `"nopic"`, delete background image, if present. If *picname* is `None`,
    return the filename of the current backgroundimage.

    ```
    >>> screen.bgpic()
    'nopic'
    >>> screen.bgpic("landscape.gif")
    >>> screen.bgpic()
    "landscape.gif"
    ```

turtle.clear()
:   Note

    This TurtleScreen method is available as a global function only under the
    name `clearscreen`. The global function `clear` is a different one
    derived from the Turtle method `clear`.

turtle.clearscreen()[¶](#turtle.clearscreen "Link to this definition")
:   Delete all drawings and all turtles from the TurtleScreen. Reset the now
    empty TurtleScreen to its initial state: white background, no background
    image, no event bindings and tracing on.

turtle.reset()
:   Note

    This TurtleScreen method is available as a global function only under the
    name `resetscreen`. The global function `reset` is another one
    derived from the Turtle method `reset`.

turtle.resetscreen()[¶](#turtle.resetscreen "Link to this definition")
:   Reset all Turtles on the Screen to their initial state.

turtle.screensize(*canvwidth=None*, *canvheight=None*, *bg=None*)[¶](#turtle.screensize "Link to this definition")
:   Parameters:
    :   * **canvwidth** – positive integer, new width of canvas in pixels
        * **canvheight** – positive integer, new height of canvas in pixels
        * **bg** – colorstring or color-tuple, new background color

    If no arguments are given, return current (canvaswidth, canvasheight). Else
    resize the canvas the turtles are drawing on. Do not alter the drawing
    window. To observe hidden parts of the canvas, use the scrollbars. With this
    method, one can make visible those parts of a drawing which were outside the
    canvas before.

    ```
    >>> screen.screensize()
    (400, 300)
    >>> screen.screensize(2000,1500)
    >>> screen.screensize()
    (2000, 1500)
    ```

    e.g. to search for an erroneously escaped turtle ;-)

turtle.setworldcoordinates(*llx*, *lly*, *urx*, *ury*)[¶](#turtle.setworldcoordinates "Link to this definition")
:   Parameters:
    :   * **llx** – a number, x-coordinate of lower left corner of canvas
        * **lly** – a number, y-coordinate of lower left corner of canvas
        * **urx** – a number, x-coordinate of upper right corner of canvas
        * **ury** – a number, y-coordinate of upper right corner of canvas

    Set up user-defined coordinate system and switch to mode “world” if
    necessary. This performs a `screen.reset()`. If mode “world” is already
    active, all drawings are redrawn according to the new coordinates.

    **ATTENTION**: in user-defined coordinate systems angles may appear
    distorted.

    ```
    >>> screen.reset()
    >>> screen.setworldcoordinates(-50,-7.5,50,7.5)
    >>> for _ in range(72):
    ...     left(10)
    ...
    >>> for _ in range(8):
    ...     left(45); fd(2)   # a regular octagon
    ```

### Animation control[¶](#animation-control "Link to this heading")

turtle.no\_animation()[¶](#turtle.no_animation "Link to this definition")
:   Temporarily disable turtle animation. The code written inside the
    `no_animation` block will not be animated;
    once the code block is exited, the drawing will appear.

    ```
    >>> with screen.no_animation():
    ...     for dist in range(2, 400, 2):
    ...         fd(dist)
    ...         rt(90)
    ```

    Added in version 3.14.

turtle.delay(*delay=None*)[¶](#turtle.delay "Link to this definition")
:   Parameters:
    :   **delay** – positive integer

    Set or return the drawing *delay* in milliseconds. (This is approximately
    the time interval between two consecutive canvas updates.) The longer the
    drawing delay, the slower the animation.

    Optional argument:

    ```
    >>> screen.delay()
    10
    >>> screen.delay(5)
    >>> screen.delay()
    5
    ```

turtle.tracer(*n=None*, *delay=None*)[¶](#turtle.tracer "Link to this definition")
:   Parameters:
    :   * **n** – nonnegative integer
        * **delay** – nonnegative integer

    Turn turtle animation on/off and set delay for update drawings. If
    *n* is given, only each n-th regular screen update is really
    performed. (Can be used to accelerate the drawing of complex
    graphics.) When called without arguments, returns the currently
    stored value of n. Second argument sets delay value (see
    [`delay()`](#turtle.delay "turtle.delay")).

    ```
    >>> screen.tracer(8, 25)
    >>> dist = 2
    >>> for i in range(200):
    ...     fd(dist)
    ...     rt(90)
    ...     dist += 2
    ```

turtle.update()[¶](#turtle.update "Link to this definition")
:   Perform a TurtleScreen update. To be used when tracer is turned off.

See also the RawTurtle/Turtle method [`speed()`](#turtle.speed "turtle.speed").

### Using screen events[¶](#using-screen-events "Link to this heading")

turtle.listen(*xdummy=None*, *ydummy=None*)[¶](#turtle.listen "Link to this definition")
:   Set focus on TurtleScreen (in order to collect key-events). Dummy arguments
    are provided in order to be able to pass [`listen()`](#turtle.listen "turtle.listen") to the onclick method.

turtle.onkey(*fun*, *key*)[¶](#turtle.onkey "Link to this definition")

turtle.onkeyrelease(*fun*, *key*)[¶](#turtle.onkeyrelease "Link to this definition")
:   Parameters:
    :   * **fun** – a function with no arguments or `None`
        * **key** – a string: key (e.g. “a”) or key-symbol (e.g. “space”)

    Bind *fun* to key-release event of key. If *fun* is `None`, event bindings
    are removed. Remark: in order to be able to register key-events, TurtleScreen
    must have the focus. (See method [`listen()`](#turtle.listen "turtle.listen").)

    ```
    >>> def f():
    ...     fd(50)
    ...     lt(60)
    ...
    >>> screen.onkey(f, "Up")
    >>> screen.listen()
    ```

turtle.onkeypress(*fun*, *key=None*)[¶](#turtle.onkeypress "Link to this definition")
:   Parameters:
    :   * **fun** – a function with no arguments or `None`
        * **key** – a string: key (e.g. “a”) or key-symbol (e.g. “space”)

    Bind *fun* to key-press event of key if key is given,
    or to any key-press-event if no key is given.
    Remark: in order to be able to register key-events, TurtleScreen
    must have focus. (See method [`listen()`](#turtle.listen "turtle.listen").)

    ```
    >>> def f():
    ...     fd(50)
    ...
    >>> screen.onkey(f, "Up")
    >>> screen.listen()
    ```

turtle.onclick(*fun*, *btn=1*, *add=None*)[¶](#turtle.onclick "Link to this definition")

turtle.onscreenclick(*fun*, *btn=1*, *add=None*)[¶](#turtle.onscreenclick "Link to this definition")
:   Parameters:
    :   * **fun** – a function with two arguments which will be called with the
          coordinates of the clicked point on the canvas
        * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
        * **add** – `True` or `False` – if `True`, a new binding will be
          added, otherwise it will replace a former binding

    Bind *fun* to mouse-click events on this screen. If *fun* is `None`,
    existing bindings are removed.

    Example for a TurtleScreen instance named `screen` and a Turtle instance
    named `turtle`:

    ```
    >>> screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will
    >>>                             # make the turtle move to the clicked point.
    >>> screen.onclick(None)        # remove event binding again
    ```

    Note

    This TurtleScreen method is available as a global function only under the
    name `onscreenclick`. The global function `onclick` is another one
    derived from the Turtle method `onclick`.

turtle.ontimer(*fun*, *t=0*)[¶](#turtle.ontimer "Link to this definition")
:   Parameters:
    :   * **fun** – a function with no arguments
        * **t** – a number >= 0

    Install a timer that calls *fun* after *t* milliseconds.

    ```
    >>> running = True
    >>> def f():
    ...     if running:
    ...         fd(50)
    ...         lt(60)
    ...         screen.ontimer(f, 250)
    >>> f()   ### makes the turtle march around
    >>> running = False
    ```

turtle.mainloop()[¶](#turtle.mainloop "Link to this definition")

turtle.done()[¶](#turtle.done "Link to this definition")
:   Starts event loop - calling Tkinter’s mainloop function.
    Must be the last statement in a turtle graphics program.
    Must *not* be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.

    ```
    >>> screen.mainloop()
    ```

### Input methods[¶](#input-methods "Link to this heading")

turtle.textinput(*title*, *prompt*)[¶](#turtle.textinput "Link to this definition")
:   Parameters:
    :   * **title** – string
        * **prompt** – string

    Pop up a dialog window for input of a string. Parameter title is
    the title of the dialog window, prompt is a text mostly describing
    what information to input.
    Return the string input. If the dialog is canceled, return `None`.

    ```
    >>> screen.textinput("NIM", "Name of first player:")
    ```

turtle.numinput(*title*, *prompt*, *default=None*, *minval=None*, *maxval=None*)[¶](#turtle.numinput "Link to this definition")
:   Parameters:
    :   * **title** – string
        * **prompt** – string
        * **default** – number (optional)
        * **minval** – number (optional)
        * **maxval** – number (optional)

    Pop up a dialog window for input of a number. title is the title of the
    dialog window, prompt is a text mostly describing what numerical information
    to input. default: default value, minval: minimum value for input,
    maxval: maximum value for input.
    The number input must be in the range minval .. maxval if these are
    given. If not, a hint is issued and the dialog remains open for
    correction.
    Return the number input. If the dialog is canceled, return `None`.

    ```
    >>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
    ```

### Settings and special methods[¶](#settings-and-special-methods "Link to this heading")

turtle.mode(*mode=None*)[¶](#turtle.mode "Link to this definition")
:   Parameters:
    :   **mode** – one of the strings “standard”, “logo” or “world”

    Set turtle mode (“standard”, “logo” or “world”) and perform reset. If mode
    is not given, current mode is returned.

    Mode “standard” is compatible with old `turtle`. Mode “logo” is
    compatible with most Logo turtle graphics. Mode “world” uses user-defined
    “world coordinates”. **Attention**: in this mode angles appear distorted if
    `x/y` unit-ratio doesn’t equal 1.

    | Mode | Initial turtle heading | positive angles |
    | --- | --- | --- |
    | “standard” | to the right (east) | counterclockwise |
    | “logo” | upward (north) | clockwise |

    ```
    >>> mode("logo")   # resets turtle heading to north
    >>> mode()
    'logo'
    ```

turtle.colormode(*cmode=None*)[¶](#turtle.colormode "Link to this definition")
:   Parameters:
    :   **cmode** – one of the values 1.0 or 255

    Return the colormode or set it to 1.0 or 255. Subsequently *r*, *g*, *b*
    values of color triples have to be in the range 0..\*cmode\*.

    ```
    >>> screen.colormode(1)
    >>> turtle.pencolor(240, 160, 80)
    Traceback (most recent call last):
         ...
    TurtleGraphicsError: bad color sequence: (240, 160, 80)
    >>> screen.colormode()
    1.0
    >>> screen.colormode(255)
    >>> screen.colormode()
    255
    >>> turtle.pencolor(240,160,80)
    ```

turtle.getcanvas()[¶](#turtle.getcanvas "Link to this definition")
:   Return the Canvas of this TurtleScreen. Useful for insiders who know what to
    do with a Tkinter Canvas.

    ```
    >>> cv = screen.getcanvas()
    >>> cv
    <turtle.ScrolledCanvas object ...>
    ```

turtle.getshapes()[¶](#turtle.getshapes "Link to this definition")
:   Return a list of names of all currently available turtle shapes.

    ```
    >>> screen.getshapes()
    ['arrow', 'blank', 'circle', ..., 'turtle']
    ```

turtle.register\_shape(*name*, *shape=None*)[¶](#turtle.register_shape "Link to this definition")

turtle.addshape(*name*, *shape=None*)[¶](#turtle.addshape "Link to this definition")
:   There are four different ways to call this function:

    1. *name* is the name of an image file (PNG, GIF, PGM, and PPM) and *shape* is `None`: Install the
       corresponding image shape.

       ```
       >>> screen.register_shape("turtle.gif")
       ```

       Note

       Image shapes *do not* rotate when turning the turtle, so they do not
       display the heading of the turtle!
    2. *name* is an arbitrary string and *shape* is the name of an image file (PNG, GIF, PGM, and PPM): Install the
       corresponding image shape.

       ```
       >>> screen.register_shape("turtle", "turtle.gif")
       ```

       Note

       Image shapes *do not* rotate when turning the turtle, so they do not
       display the heading of the turtle!
    3. *name* is an arbitrary string and *shape* is a tuple of pairs of
       coordinates: Install the corresponding polygon shape.

       ```
       >>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))
       ```
    4. *name* is an arbitrary string and *shape* is a (compound) [`Shape`](#turtle.Shape "turtle.Shape")
       object: Install the corresponding compound shape.

    Add a turtle shape to TurtleScreen’s shapelist. Only thusly registered
    shapes can be used by issuing the command `shape(shapename)`.

    Changed in version 3.14: Added support for PNG, PGM, and PPM image formats.
    Both a shape name and an image file name can be specified.

turtle.turtles()[¶](#turtle.turtles "Link to this definition")
:   Return the list of turtles on the screen.

    ```
    >>> for turtle in screen.turtles():
    ...     turtle.color("red")
    ```

turtle.window\_height()[¶](#turtle.window_height "Link to this definition")
:   Return the height of the turtle window.

    ```
    >>> screen.window_height()
    480
    ```

turtle.window\_width()[¶](#turtle.window_width "Link to this definition")
:   Return the width of the turtle window.

    ```
    >>> screen.window_width()
    640
    ```

### Methods specific to Screen, not inherited from TurtleScreen[¶](#methods-specific-to-screen-not-inherited-from-turtlescreen "Link to this heading")

turtle.bye()[¶](#turtle.bye "Link to this definition")
:   Shut the turtlegraphics window.

turtle.exitonclick()[¶](#turtle.exitonclick "Link to this definition")
:   Bind `bye()` method to mouse clicks on the Screen.

    If the value “using\_IDLE” in the configuration dictionary is `False`
    (default value), also enter mainloop. Remark: If IDLE with the `-n` switch
    (no subprocess) is used, this value should be set to `True` in
    `turtle.cfg`. In this case IDLE’s own mainloop is active also for the
    client script.

turtle.save(*filename*, *overwrite=False*)[¶](#turtle.save "Link to this definition")
:   Save the current turtle drawing (and turtles) as a PostScript file.

    Parameters:
    :   * **filename** – the path of the saved PostScript file
        * **overwrite** – if `False` and there already exists a file with the given
          filename, then the function will raise a
          `FileExistsError`. If it is `True`, the file will be
          overwritten.

    ```
    >>> screen.save("my_drawing.ps")
    >>> screen.save("my_drawing.ps", overwrite=True)
    ```

    Added in version 3.14.

turtle.setup(*width=\_CFG['width']*, *height=\_CFG['height']*, *startx=\_CFG['leftright']*, *starty=\_CFG['topbottom']*)[¶](#turtle.setup "Link to this definition")
:   Set the size and position of the main window. Default values of arguments
    are stored in the configuration dictionary and can be changed via a
    `turtle.cfg` file.

    Parameters:
    :   * **width** – if an integer, a size in pixels, if a float, a fraction of the
          screen; default is 50% of screen
        * **height** – if an integer, the height in pixels, if a float, a fraction of
          the screen; default is 75% of screen
        * **startx** – if positive, starting position in pixels from the left
          edge of the screen, if negative from the right edge, if `None`,
          center window horizontally
        * **starty** – if positive, starting position in pixels from the top
          edge of the screen, if negative from the bottom edge, if `None`,
          center window vertically

    ```
    >>> screen.setup (width=200, height=200, startx=0, starty=0)
    >>>              # sets window to 200x200 pixels, in upper left of screen
    >>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
    >>>              # sets window to 75% of screen by 50% of screen and centers
    ```

turtle.title(*titlestring*)[¶](#turtle.title "Link to this definition")
:   Parameters:
    :   **titlestring** – a string that is shown in the titlebar of the turtle
        graphics window

    Set title of turtle window to *titlestring*.

    ```
    >>> screen.title("Welcome to the turtle zoo!")
    ```

## Public classes[¶](#public-classes "Link to this heading")

*class* turtle.RawTurtle(*canvas*)[¶](#turtle.RawTurtle "Link to this definition")

*class* turtle.RawPen(*canvas*)[¶](#turtle.RawPen "Link to this definition")
:   Parameters:
    :   **canvas** – a `tkinter.Canvas`, a [`ScrolledCanvas`](#turtle.ScrolledCanvas "turtle.ScrolledCanvas") or a
        [`TurtleScreen`](#turtle.TurtleScreen "turtle.TurtleScreen")

    Create a turtle. The turtle has all methods described above as “methods of
    Turtle/RawTurtle”.

*class* turtle.Turtle[¶](#turtle.Turtle "Link to this definition")
:   Subclass of RawTurtle, has the same interface but draws on a default
    [`Screen`](#turtle.Screen "turtle.Screen") object created automatically when needed for the first time.

*class* turtle.TurtleScreen(*cv*)[¶](#turtle.TurtleScreen "Link to this definition")
:   Parameters:
    :   **cv** – a `tkinter.Canvas`

    Provides screen oriented methods like [`bgcolor()`](#turtle.bgcolor "turtle.bgcolor") etc. that are described
    above.

*class* turtle.Screen[¶](#turtle.Screen "Link to this definition")
:   Subclass of TurtleScreen, with [four methods added](#screenspecific).

*class* turtle.ScrolledCanvas(*master*)[¶](#turtle.ScrolledCanvas "Link to this definition")
:   Parameters:
    :   **master** – some Tkinter widget to contain the ScrolledCanvas, i.e.
        a Tkinter-canvas with scrollbars added

    Used by class Screen, which thus automatically provides a ScrolledCanvas as
    playground for the turtles.

*class* turtle.Shape(*type\_*, *data*)[¶](#turtle.Shape "Link to this definition")
:   Parameters:
    :   **type\_** – one of the strings “polygon”, “image”, “compound”

    Data structure modeling shapes. The pair `(type_, data)` must follow this
    specification:

    | *type\_* | *data* |
    | --- | --- |
    | “polygon” | a polygon-tuple, i.e. a tuple of pairs of coordinates |
    | “image” | an image (in this form only used internally!) |
    | “compound” | `None` (a compound shape has to be constructed using the [`addcomponent()`](#turtle.Shape.addcomponent "turtle.Shape.addcomponent") method) |

    addcomponent(*poly*, *fill*, *outline=None*)[¶](#turtle.Shape.addcomponent "Link to this definition")
    :   Parameters:
        :   * **poly** – a polygon, i.e. a tuple of pairs of numbers
            * **fill** – a color the *poly* will be filled with
            * **outline** – a color for the poly’s outline (if given)

        Example:

        ```
        >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
        >>> s = Shape("compound")
        >>> s.addcomponent(poly, "red", "blue")
        >>> # ... add more components and then use register_shape()
        ```

        See [Compound shapes](#compoundshapes).

*class* turtle.Vec2D(*x*, *y*)[¶](#turtle.Vec2D "Link to this definition")
:   A two-dimensional vector class, used as a helper class for implementing
    turtle graphics. May be useful for turtle graphics programs too. Derived
    from tuple, so a vector is a tuple!

    Provides (for *a*, *b* vectors, *k* number):

    * `a + b` vector addition
    * `a - b` vector subtraction
    * `a * b` inner product
    * `k * a` and `a * k` multiplication with scalar
    * `abs(a)` absolute value of a
    * `a.rotate(angle)` rotation

## Explanation[¶](#explanation "Link to this heading")

A turtle object draws on a screen object, and there a number of key classes in
the turtle object-oriented interface that can be used to create them and relate
them to each other.

A [`Turtle`](#turtle.Turtle "turtle.Turtle") instance will automatically create a [`Screen`](#turtle.Screen "turtle.Screen")
instance if one is not already present.

`Turtle` is a subclass of [`RawTurtle`](#turtle.RawTurtle "turtle.RawTurtle"), which *doesn’t* automatically
create a drawing surface - a *canvas* will need to be provided or created for
it. The *canvas* can be a `tkinter.Canvas`, [`ScrolledCanvas`](#turtle.ScrolledCanvas "turtle.ScrolledCanvas")
or [`TurtleScreen`](#turtle.TurtleScreen "turtle.TurtleScreen").

[`TurtleScreen`](#turtle.TurtleScreen "turtle.TurtleScreen") is the basic drawing surface for a
turtle. [`Screen`](#turtle.Screen "turtle.Screen") is a subclass of `TurtleScreen`, and
includes [some additional methods](#screenspecific) for managing its
appearance (including size and title) and behaviour. `TurtleScreen`’s
constructor needs a `tkinter.Canvas` or a
[`ScrolledCanvas`](#turtle.ScrolledCanvas "turtle.ScrolledCanvas") as an argument.

The functional interface for turtle graphics uses the various methods of
`Turtle` and `TurtleScreen`/`Screen`. Behind the scenes, a screen
object is automatically created whenever a function derived from a `Screen`
method is called. Similarly, a turtle object is automatically created
whenever any of the functions derived from a Turtle method is called.

To use multiple turtles on a screen, the object-oriented interface must be
used.

## Help and configuration[¶](#help-and-configuration "Link to this heading")

### How to use help[¶](#how-to-use-help "Link to this heading")

The public methods of the Screen and Turtle classes are documented extensively
via docstrings. So these can be used as online-help via the Python help
facilities:

* When using IDLE, tooltips show the signatures and first lines of the
  docstrings of typed in function-/method calls.
* Calling [`help()`](functions.html#help "help") on methods or functions displays the docstrings:

  ```
  >>> help(Screen.bgcolor)
  Help on method bgcolor in module turtle:

  bgcolor(self, *args) unbound turtle.Screen method
      Set or return backgroundcolor of the TurtleScreen.

      Arguments (if given): a color string or three numbers
      in the range 0..colormode or a 3-tuple of such numbers.


      >>> screen.bgcolor("orange")
      >>> screen.bgcolor()
      "orange"
      >>> screen.bgcolor(0.5,0,0.5)
      >>> screen.bgcolor()
      "#800080"

  >>> help(Turtle.penup)
  Help on method penup in module turtle:

  penup(self) unbound turtle.Turtle method
      Pull the pen up -- no drawing when moving.

      Aliases: penup | pu | up

      No argument

      >>> turtle.penup()
  ```
* The docstrings of the functions which are derived from methods have a modified
  form:

  ```
  >>> help(bgcolor)
  Help on function bgcolor in module turtle:

  bgcolor(*args)
      Set or return backgroundcolor of the TurtleScreen.

      Arguments (if given): a color string or three numbers
      in the range 0..colormode or a 3-tuple of such numbers.

      Example::

        >>> bgcolor("orange")
        >>> bgcolor()
        "orange"
        >>> bgcolor(0.5,0,0.5)
        >>> bgcolor()
        "#800080"

  >>> help(penup)
  Help on function penup in module turtle:

  penup()
      Pull the pen up -- no drawing when moving.

      Aliases: penup | pu | up

      No argument

      Example:
      >>> penup()
  ```

These modified docstrings are created automatically together with the function
definitions that are derived from the methods at import time.

### Translation of docstrings into different languages[¶](#translation-of-docstrings-into-different-languages "Link to this heading")

There is a utility to create a dictionary the keys of which are the method names
and the values of which are the docstrings of the public methods of the classes
Screen and Turtle.

turtle.write\_docstringdict(*filename='turtle\_docstringdict'*)[¶](#turtle.write_docstringdict "Link to this definition")
:   Parameters:
    :   **filename** – a string, used as filename

    Create and write docstring-dictionary to a Python script with the given
    filename. This function has to be called explicitly (it is not used by the
    turtle graphics classes). The docstring dictionary will be written to the
    Python script `filename.py`. It is intended to serve as a template
    for translation of the docstrings into different languages.

If you (or your students) want to use `turtle` with online help in your
native language, you have to translate the docstrings and save the resulting
file as e.g. `turtle_docstringdict_german.py`.

If you have an appropriate entry in your `turtle.cfg` file this dictionary
will be read in at import time and will replace the original English docstrings.

At the time of this writing there are docstring dictionaries in German and in
Italian. (Requests please to [glingl@aon.at](mailto:glingl%40aon.at).)

### How to configure Screen and Turtles[¶](#how-to-configure-screen-and-turtles "Link to this heading")

The built-in default configuration mimics the appearance and behaviour of the
old turtle module in order to retain best possible compatibility with it.

If you want to use a different configuration which better reflects the features
of this module or which better fits to your needs, e.g. for use in a classroom,
you can prepare a configuration file `turtle.cfg` which will be read at import
time and modify the configuration according to its settings.

The built in configuration would correspond to the following `turtle.cfg`:

```
width = 0.5
height = 0.75
leftright = None
topbottom = None
canvwidth = 400
canvheight = 300
mode = standard
colormode = 1.0
delay = 10
undobuffersize = 1000
shape = classic
pencolor = black
fillcolor = black
resizemode = noresize
visible = True
language = english
exampleturtle = turtle
examplescreen = screen
title = Python Turtle Graphics
using_IDLE = False
```

Short explanation of selected entries:

* The first four lines correspond to the arguments of the [`Screen.setup`](#turtle.setup "turtle.setup")
  method.
* Line 5 and 6 correspond to the arguments of the method
  [`Screen.screensize`](#turtle.screensize "turtle.screensize").
* *shape* can be any of the built-in shapes, e.g: arrow, turtle, etc. For more
  info try `help(shape)`.
* If you want to use no fill color (i.e. make the turtle transparent), you have
  to write `fillcolor = ""` (but all nonempty strings must not have quotes in
  the cfg file).
* If you want to reflect the turtle its state, you have to use `resizemode =
  auto`.
* If you set e.g. `language = italian` the docstringdict
  `turtle_docstringdict_italian.py` will be loaded at import time (if
  present on the import path, e.g. in the same directory as `turtle`).
* The entries *exampleturtle* and *examplescreen* define the names of these
  objects as they occur in the docstrings. The transformation of
  method-docstrings to function-docstrings will delete these names from the
  docstrings.
* *using\_IDLE*: Set this to `True` if you regularly work with IDLE and its `-n`
  switch (“no subprocess”). This will prevent [`exitonclick()`](#turtle.exitonclick "turtle.exitonclick") to enter the
  mainloop.

There can be a `turtle.cfg` file in the directory where `turtle` is
stored and an additional one in the current working directory. The latter will
override the settings of the first one.

The `Lib/turtledemo` directory contains a `turtle.cfg` file. You can
study it as an example and see its effects when running the demos (preferably
not from within the demo-viewer).

## `turtledemo` — Demo scripts[¶](#module-turtledemo "Link to this heading")

The `turtledemo` package includes a set of demo scripts. These
scripts can be run and viewed using the supplied demo viewer as follows:

```
python -m turtledemo
```

Alternatively, you can run the demo scripts individually. For example,

```
python -m turtledemo.bytedesign
```

The `turtledemo` package directory contains:

* A demo viewer `__main__.py` which can be used to view the sourcecode
  of the scripts and run them at the same time.
* Multiple scripts demonstrating different features of the `turtle`
  module. Examples can be accessed via the Examples menu. They can also
  be run standalone.
* A `turtle.cfg` file which serves as an example of how to write
  and use such files.

The demo scripts are:

| Name | Description | Features |
| --- | --- | --- |
| `bytedesign` | complex classical turtle graphics pattern | [`tracer()`](#turtle.tracer "turtle.tracer"), [`delay()`](#turtle.delay "turtle.delay"), [`update()`](#turtle.update "turtle.update") |
| `chaos` | graphs Verhulst dynamics, shows that computer’s computations can generate results sometimes against the common sense expectations | world coordinates |
| `clock` | analog clock showing time of your computer | turtles as clock’s hands, [`ontimer()`](#turtle.ontimer "turtle.ontimer") |
| `colormixer` | experiment with r, g, b | [`ondrag()`](#turtle.ondrag "turtle.ondrag") |
| `forest` | 3 breadth-first trees | randomization |
| `fractalcurves` | Hilbert & Koch curves | recursion |
| `lindenmayer` | ethnomathematics (indian kolams) | L-System |
| `minimal_hanoi` | Towers of Hanoi | Rectangular Turtles as Hanoi discs ([`shape()`](#turtle.shape "turtle.shape"), [`shapesize()`](#turtle.shapesize "turtle.shapesize")) |
| `nim` | play the classical nim game with three heaps of sticks against the computer. | turtles as nimsticks, event driven (mouse, keyboard) |
| `paint` | super minimalistic drawing program | [`onclick()`](#turtle.onclick "turtle.onclick") |
| `peace` | elementary | turtle: appearance and animation |
| `penrose` | aperiodic tiling with kites and darts | [`stamp()`](#turtle.stamp "turtle.stamp") |
| `planet_and_moon` | simulation of gravitational system | compound shapes, [`Vec2D`](#turtle.Vec2D "turtle.Vec2D") |
| `rosette` | a pattern from the wikipedia article on turtle graphics | [`clone()`](#turtle.clone "turtle.clone"), [`undo()`](#turtle.undo "turtle.undo") |
| `round_dance` | dancing turtles rotating pairwise in opposite direction | compound shapes, [`clone()`](#turtle.clone "turtle.clone") [`shapesize()`](#turtle.shapesize "turtle.shapesize"), [`tilt()`](#turtle.tilt "turtle.tilt"), [`get_shapepoly()`](#turtle.get_shapepoly "turtle.get_shapepoly"), [`update()`](#turtle.update "turtle.update") |
| `sorting_animate` | visual demonstration of different sorting methods | simple alignment, randomization |
| `tree` | a (graphical) breadth first tree (using generators) | [`clone()`](#turtle.clone "turtle.clone") |
| `two_canvases` | simple design | turtles on two canvases |
| `yinyang` | another elementary example | [`circle()`](#turtle.circle "turtle.circle") |

Have fun!

## Changes since Python 2.6[¶](#changes-since-python-2-6 "Link to this heading")

* The methods [`Turtle.tracer`](#turtle.tracer "turtle.tracer"), [`Turtle.window_width`](#turtle.window_width "turtle.window_width") and
  [`Turtle.window_height`](#turtle.window_height "turtle.window_height") have been eliminated.
  Methods with these names and functionality are now available only
  as methods of [`Screen`](#turtle.Screen "turtle.Screen"). The functions derived from these remain
  available. (In fact already in Python 2.6 these methods were merely
  duplications of the corresponding
  [`TurtleScreen`](#turtle.TurtleScreen "turtle.TurtleScreen")/[`Screen`](#turtle.Screen "turtle.Screen") methods.)
* The method `Turtle.fill()` has been eliminated.
  The behaviour of [`begin_fill()`](#turtle.begin_fill "turtle.begin_fill") and [`end_fill()`](#turtle.end_fill "turtle.end_fill")
  have changed slightly: now every filling process must be completed with an
  `end_fill()` call.
* A method [`Turtle.filling`](#turtle.filling "turtle.filling") has been added. It returns a boolean
  value: `True` if a filling process is under way, `False` otherwise.
  This behaviour corresponds to a `fill()` call without arguments in
  Python 2.6.

## Changes since Python 3.0[¶](#changes-since-python-3-0 "Link to this heading")

* The [`Turtle`](#turtle.Turtle "turtle.Turtle") methods [`shearfactor()`](#turtle.shearfactor "turtle.shearfactor"), [`shapetransform()`](#turtle.shapetransform "turtle.shapetransform") and
  [`get_shapepoly()`](#turtle.get_shapepoly "turtle.get_shapepoly") have been added. Thus the full range of
  regular linear transforms is now available for transforming turtle shapes.
  [`tiltangle()`](#turtle.tiltangle "turtle.tiltangle") has been enhanced in functionality: it now can
  be used to get or set the tilt angle.
* The [`Screen`](#turtle.Screen "turtle.Screen") method [`onkeypress()`](#turtle.onkeypress "turtle.onkeypress") has been added as a complement to
  [`onkey()`](#turtle.onkey "turtle.onkey"). As the latter binds actions to the key release event,
  an alias: [`onkeyrelease()`](#turtle.onkeyrelease "turtle.onkeyrelease") was also added for it.
* The method [`Screen.mainloop`](#turtle.mainloop "turtle.mainloop") has been added,
  so there is no longer a need to use the standalone [`mainloop()`](#turtle.mainloop "turtle.mainloop") function
  when working with [`Screen`](#turtle.Screen "turtle.Screen") and [`Turtle`](#turtle.Turtle "turtle.Turtle") objects.
* Two input methods have been added: [`Screen.textinput`](#turtle.textinput "turtle.textinput") and
  [`Screen.numinput`](#turtle.numinput "turtle.numinput"). These pop up input dialogs and return
  strings and numbers respectively.

### [Table of Contents](../contents.html)

* [`turtle` — Turtle graphics](#)
  + [Introduction](#introduction)
  + [Get started](#get-started)
  + [Tutorial](#tutorial)
    - [Starting a turtle environment](#starting-a-turtle-environment)
    - [Basic drawing](#basic-drawing)
      * [Pen control](#pen-control)
      * [The turtle’s position](#the-turtle-s-position)
    - [Making algorithmic patterns](#making-algorithmic-patterns)
  + [How to…](#how-to)
    - [Get started as quickly as possible](#get-started-as-quickly-as-possible)
    - [Automatically begin and end filling](#automatically-begin-and-end-filling)
    - [Use the `turtle` module namespace](#use-the-turtle-module-namespace)
    - [Use turtle graphics in a script](#use-turtle-graphics-in-a-script)
    - [Use object-oriented turtle graphics](#use-object-oriented-turtle-graphics)
  + [Turtle graphics reference](#turtle-graphics-reference)
    - [Turtle methods](#turtle-methods)
    - [Methods of TurtleScreen/Screen](#methods-of-turtlescreen-screen)
  + [Methods of RawTurtle/Turtle and corresponding functions](#methods-of-rawturtle-turtle-and-corresponding-functions)
    - [Turtle motion](#turtle-motion)
    - [Tell Turtle’s state](#tell-turtle-s-state)
    - [Settings for measurement](#settings-for-measurement)
    - [Pen control](#id1)
      * [Drawing state](#drawing-state)
      * [Color control](#color-control)
      * [Filling](#filling)
      * [More drawing control](#more-drawing-control)
    - [Turtle state](#turtle-state)
      * [Visibility](#visibility)
      * [Appearance](#appearance)
    - [Using events](#using-events)
    - [Special Turtle methods](#special-turtle-methods)
    - [Compound shapes](#compound-shapes)
  + [Methods of TurtleScreen/Screen and corresponding functions](#methods-of-turtlescreen-screen-and-corresponding-functions)
    - [Window control](#window-control)
    - [Animation control](#animation-control)
    - [Using screen events](#using-screen-events)
    - [Input methods](#input-methods)
    - [Settings and special methods](#settings-and-special-methods)
    - [Methods specific to Screen, not inherited from TurtleScreen](#methods-specific-to-screen-not-inherited-from-turtlescreen)
  + [Public classes](#public-classes)
  + [Explanation](#explanation)
  + [Help and configuration](#help-and-configuration)
    - [How to use help](#how-to-use-help)
    - [Translation of docstrings into different languages](#translation-of-docstrings-into-different-languages)
    - [How to configure Screen and Turtles](#how-to-configure-screen-and-turtles)
  + [`turtledemo` — Demo scripts](#module-turtledemo)
  + [Changes since Python 2.6](#changes-since-python-2-6)
  + [Changes since Python 3.0](#changes-since-python-3-0)

#### Previous topic

[IDLE — Python editor and shell](idle.html "previous chapter")

#### Next topic

[Development Tools](development.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/turtle.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](development.html "Development Tools") |
* [previous](idle.html "IDLE — Python editor and shell") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `turtle` — Turtle graphics
* |
* Theme
  Auto
  Light
  Dark
   |

© [Copyright](../copyright.html) 2001 Python Software Foundation.
  
This page is licensed under the Python Software Foundation License Version 2.
  
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
  
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation.
[Please donate.](https://www.python.org/psf/donations/)
  
  
Last updated on Feb 22, 2026 (06:32 UTC).
[Found a bug](/bugs.html)?
  
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.