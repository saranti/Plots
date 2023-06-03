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
main_spine = ax.plot([-4.01, 4], [0, 0], color=COLOR, linewidth=2)


def problems(data: list,
             problem_x: float, problem_y: float,
             prob_angle_x: float, prob_angle_y: float,):
    """
    Draw each problem section of the Ishikawa plot.

    Parameters
    ----------
    data : indexable object
        The input data (can be list or tuple).
    problem_x, problem_y : float, optional
        The `X` and `Y` positions of the problem arrows (`Y` defaults to zero).
    prob_angle_x, prob_angle_y : float, optional
        The angle of the problem annotations. They are angled towards
        the tail of the plot.

    Returns
    -------
    None.

    """
    ax.annotate(str.upper(data[0]), xy=(problem_x, problem_y),
                xytext=(prob_angle_x, prob_angle_y),
                fontsize='11',
                color='white',
                weight='bold',
                xycoords='data',
                textcoords='offset fontsize',
                arrowprops=dict(arrowstyle="->", facecolor='black'),
                bbox=dict(boxstyle='square',
                          facecolor=COLOR,
                          pad=0.8))


def causes(data: list, cause_x: float, cause_y: float,
           cause_xytext=(-14, -0.3), top: bool = True):
    """
    Place each cause to a position relative to the problems
    annotations.

    Parameters
    ----------
    data : indexible object
        The input data (can be list or tuple). IndexError is
        raised if more than six arguments are passed.
    cause_x, cause_y : float
        The `X` and `Y` position of the cause annotations.
    cause_xytext : tuple, optional
        The distance of the cause text from the problem arrow in
        fontsize units.
    top : bool

    Returns
    -------
    None.

    """
    for index, cause in enumerate(data[1]):
        # First cause annotation is placed in the middle of the problems arrow
        # and each subsequent cause is plotted above or below it.
        coords = [[0, [0, 0]],
                  [0.2, [0.5, -0.5]],
                  [-0.4, [-1, 1]],
                  [0.6, [1.5, -1.5]],
                  [-0.8, [-2, 2]],
                  [1, [2.5, -2.5]]]
        if top:
            cause_x -= coords[index][0]
            cause_y += coords[index][1][0]
        else:
            cause_x -= coords[index][0]
            cause_y += coords[index][1][1]

        ax.annotate(cause, xy=(cause_x, cause_y),
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
        The input data (can be list or tuple). ValueError is
        raised if more than six arguments are passed.

    Returns
    -------
    None.

    """
    for index, problem in enumerate(args):
        top_row = True
        cause_arrow_y = 1.8
        if index % 2 != 0:
            top_row = False  # Plot problems below the spine
            y_prob_angle = -15.5
            cause_arrow_y = -1.8
        else:
            y_prob_angle = 15  # Plot problems above the spine
        if str(index) in '01':
            prob_arrow_x = 3.5
            cause_arrow_x = 2.7
        elif str(index) in '23':
            prob_arrow_x = 1
            cause_arrow_x = 0.2
        else:
            prob_arrow_x = -1.6
            cause_arrow_x = -2.4
        if index > 5:
            raise ValueError(f'Maximum number of problems is 6, you have entered '
                             f'{len(args)}')

        problems(problem, prob_arrow_x, 0, -15, y_prob_angle)
        causes(problem, cause_arrow_x, cause_arrow_y, top=top_row)


# draw fish head
ax.text(4.07, -0.08, 'PROBLEM', fontsize=12, color='white', weight='bold')
semicircle = Wedge((4.01, 0), 0.9, 270, 90, fc=COLOR)
ax.add_patch(semicircle)

# draw fishtail
edges = ((-4.8, 0.8), (-4.8, -0.8), (-4.0, -0.01))
triangle = Polygon(edges, fc=COLOR)
ax.add_patch(triangle)


# Input data
method = ['Method', ['Time consumption', 'Cost', 'Procedures',
                     'Inefficient process']]
machine = ['Machine', ['Faulty equipment', 'Compatibility']]
material = ['Material', ['Poor-quality input', 'Raw materials', 'Supplier',
                         'Shortage']]
measure = ['Measurement', ['Calibration', 'Performance', 'Wrong measurements']]
env = ['Environment', ['Bad conditions']]
people = ['People', ['Lack of training', 'Managers', 'Labor shortage',
                     'Procedures', 'Skills']]

draw_body(method, machine, material, measure, env, people)
plt.show()
