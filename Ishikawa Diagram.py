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
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
COLOR = 'C0'


def problems(data: list,
             problem_x: float, problem_y: float,
             prob_angle_x: float, prob_angle_y: float):
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
                fontsize='10',
                color='white',
                weight='bold',
                xycoords='data',
                verticalalignment="center",
                horizontalalignment="center",
                textcoords='offset fontsize',
                arrowprops=dict(arrowstyle="->", facecolor='black'),
                bbox=dict(boxstyle='square',
                          facecolor=COLOR,
                          pad=0.8))


def causes(data: list, cause_x: float, cause_y: float,
           cause_xytext=(-9, -0.3), top: bool = True):
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
        Adjust to set the distance of the cause text from the problem
        arrow in fontsize units.
    top : bool

    Returns
    -------
    None.

    """
    for index, cause in enumerate(data[1]):
        # First cause annotation is placed in the middle of the problems arrow
        # and each subsequent cause is plotted above or below it in succession.

        # [<x pos>, [<y pos top>, <y pos bottom>]]
        coords = [[0, [0, 0]],
                  [0.28, [0.5, -0.5]],
                  [-0.56, [-1, 1]],
                  [0.84, [1.5, -1.5]],
                  [-1.1, [-2, 2]],
                  [1.38, [2.5, -2.5]]]
        if top:
            cause_x -= coords[index][0]
            cause_y += coords[index][1][0]
        else:
            cause_x -= coords[index][0]
            cause_y += coords[index][1][1]

        ax.annotate(cause, xy=(cause_x, cause_y),
                    horizontalalignment='center',
                    xytext=cause_xytext,
                    fontsize='9',
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
    second_sections = []
    third_sections = []
    # Resize diagram to automatically scale in response to the number
    # of problems in the input data.
    if len(args) == 1 or len(args) == 2:
        spine_length = (-2.1, 2)
        head_pos = (2, 0)
        tail_pos = ((-2.8, 0.8), (-2.8, -0.8), (-2.0, -0.01))
        first_section = [1.6, 0.6]
    elif len(args) == 3 or len(args) == 4:
        spine_length = (-3.1, 3)
        head_pos = (3, 0)
        tail_pos = ((-3.8, 0.8), (-3.8, -0.8), (-3.0, -0.01))
        first_section = [2.6, 1.6]
        second_sections = [-0.4, -1.4]
    else:  # num == 5 or 6
        spine_length = (-4.1, 4)
        head_pos = (4, 0)
        tail_pos = ((-4.8, 0.8), (-4.8, -0.8), (-4.0, -0.01))
        first_section = [3.5, 2.5]
        second_sections = [1, 0]
        third_sections = [-1.5, -2.5]

    # Change the coordinates of the annotations on each loop.
    for index, problem in enumerate(args):
        top_row = True
        cause_arrow_y = 1.7
        if index % 2 != 0:  # Plot problems below the spine.
            top_row = False
            y_prob_angle = -16
            cause_arrow_y = -1.7
        else:  # Plot problems above the spine.
            y_prob_angle = 16
        # Plot the 3 sections in pairs along the main spine.
        if index in (0, 1):
            prob_arrow_x = first_section[0]
            cause_arrow_x = first_section[1]
        elif index in (2, 3):
            prob_arrow_x = second_sections[0]
            cause_arrow_x = second_sections[1]
        else:
            prob_arrow_x = third_sections[0]
            cause_arrow_x = third_sections[1]
        if index > 5:
            raise ValueError(f'Maximum number of problems is 6, you have entered '
                             f'{len(args)}')

        # draw main spine
        ax.plot(spine_length, [0, 0], color=COLOR, linewidth=2)
        # draw fish head
        ax.text(head_pos[0] + 0.1, head_pos[1] - 0.05, 'PROBLEM', fontsize=10,
                color='white', weight='bold')
        semicircle = Wedge(head_pos, 1, 270, 90, fc=COLOR)
        ax.add_patch(semicircle)
        # draw fishtail
        triangle = Polygon(tail_pos, fc=COLOR)
        ax.add_patch(triangle)

        problems(problem, prob_arrow_x, 0, -15, y_prob_angle)
        causes(problem, cause_arrow_x, cause_arrow_y, top=top_row)


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
