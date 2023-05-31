"""
================
Ishikawa Diagram
================

Ishikawa Diagrams, fishbone diagrams, herringbone diagrams, or cause-and-effect
diagrams are used to identify problems in a system by showing how causes and
effects are linked.
Source: https://en.wikipedia.org/wiki/Ishikawa_diagram

"""
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Polygon

# Create the fishbone diagram
fig, ax = plt.subplots(figsize=(12, 6), layout='constrained')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

COLOR = 'C0'
# Main spine
ax.plot([-4.01, 4.03], [0, 0], color=COLOR, linewidth=2, alpha=0.5)


def section(data: list,
            category_x: float, category_y: float,
            cat_angle_x: float, cat_angle_y: float):
    """
    Draw each section of the Ishikawa plot.

    Parameters
    ----------
    data : indexable object
        The input data (can be list or tuple).
    category_x, category_y : float, optional
        The `X` and `Y` positions of the category arrows (`Y` defaults to zero).
    cat_angle_x, cat_angle_y : float, optional
        The angle of the category annotations (default is -15, 15. Annotations
         are angled towards rear of plot).

    Returns
    -------
    None.

    """
    ax.annotate(data[0], xy=(category_x, category_y),
                xytext=(cat_angle_x, cat_angle_y),
                fontsize='11',
                xycoords='data',
                textcoords='offset fontsize',
                arrowprops=dict(arrowstyle="->",
                                facecolor='black'),
                bbox=dict(boxstyle='square',
                          facecolor=COLOR,
                          pad=0.8,
                          alpha=0.4))


def causes(data: list,
           cause_x: float, cause_y: float,
           single_cause: tuple = (2.5, 2), cause_xytext=(-14, -0.3)):
    """
    Recursively place each cause to a position relative to
    the category annotations.

    Parameters
    ----------
    data : indexable object
        The input data (can be list or tuple).
    cause_x, cause_y : float
        The `X` and `Y` position of the cause annotation arrows.
    single_cause : tuple, optional
        The position of the cause if it is the only one there
        (the default is (2.5, 2)).
    cause_xytext : tuple, optional
        The distance of the cause text from the category arrow in Fontsize units.

    Returns
    -------
    None.

    """
    for problem in data[1]:
        if len(data[1]) == 1:
            # Put annotations with 1 single cause in the middle of the arrow
            cause_x, cause_y = single_cause
        else:
            if single_cause[1] > 0:
                # if section on top (cause_y is positive, 2nd single_cause
                # num is positive), move each cause to the left and up
                # by these amounts
                cause_x -= 0.22
                cause_y += 0.5

            else:
                # if section on bottom (cause_y is negative, 2nd single_cause
                # num is negative), move each cause to the left and down
                # by these amounts
                cause_x -= 0.22
                cause_y -= 0.5

        ax.annotate(problem, xy=(cause_x, cause_y),
                    xytext=cause_xytext,
                    fontsize='10',
                    xycoords='data',
                    textcoords='offset fontsize',
                    arrowprops=dict(arrowstyle="->",
                                    facecolor='black'))


def draw_body(*args):
    """
    Place each section in its correct place by changing
    the coordinates on each loop.

    Parameters
    ----------
    *args : indexable object
        The input data (can be list or tuple).

    Returns
    -------
    None.

    """
    for index, problem in enumerate(args):
        cause_angle_y = 15
        cat_y = 0.5  # Move the upper cause lists up or down
        if index % 2 != 0:
            cause_angle_y = -15.5
            cat_y = -0.5  # Move the lower cause lists up or down
            cause_y = -2
        else:
            cause_y = 2
        if str(index) in '23':
            cat_arrow_x = 1
            cat_x = 0.8  # Move the middle pair of cause lists left or right
            cause_x = 0.0
        else:
            cat_arrow_x = 3.5
            cat_x = 3.2  # Move the first pair of cause lists left or right
            cause_x = 2.5
        if str(index) in '45':
            cat_arrow_x = -1.6
            cat_x = -1.9  # Move the rear pair of cause lists left or right
            cause_x = -2.5

        section(problem, cat_arrow_x, 0, -15, cause_angle_y)
        causes(problem, cat_x, cat_y, (cause_x, cause_y))


# draw fish head
ax.text(4.15, -0.06, 'Problem', fontsize=12)
semicircle = Wedge((4.05, 0), 0.8, 270, 90, fc=COLOR, alpha=0.5)
ax.add_patch(semicircle)

# draw fishtail
edges = ((-4.8, 0.8), (-4.8, -0.8), (-4.0, -0.01))
triangle = Polygon(edges, closed=True, fc=COLOR, alpha=0.5)
ax.add_patch(triangle)

# Input data
method = ['Method', ['Time consumption', 'Cost', 'Procedures',
                     'Inefficient process']]
machine = ['Machine', ['Faulty equipment', 'Compatibility', ]]
material = ['Material', ['Poor-quality input', 'Raw materials', 'Supplier',
                         'Shortage']]
measure = ['Measurement', ['Calibration', 'Performance', 'Wrong measurements']]
env = ['Environment', ['Bad conditions']]
people = ['People', ['Lack of training', 'Managers', 'Labor shortage',
                     'Procedures', 'Skills']]

# Generate plot
draw_body(method, machine, material, measure, env, people)
plt.show()
