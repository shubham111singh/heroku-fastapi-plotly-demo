from typing import Union, List
import plotly.graph_objects as go


def collatz_sequence(x: int) -> List[int]:
    """Returns the iterates of the Collatz sequence given
    by the following rule:

         x ↦ x / 2  if x is even,
         x ↦ (3 * x + 1) / 2  if x is odd,

    and stopping when x=1.
    """
    if x <= 1:
        return [x]
    elif x % 2 == 0:
        # Note that bitshifting (">> 1") is equivalent to dividing by 2.
        return [x] + collatz_sequence(x >> 1)
    else:
        return [x] + collatz_sequence(3 * x + 1 >> 1)


def collatz_graph(x_list: List[int]) -> str:
    """Given a list of initial values, plot the respective Collatz iterates.
    """
    fig = go.Figure()
    fig.layout.yaxis.type = "log"
    for x in x_list:
        _add_trace_to_fig(fig, x=x)
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn')


# NOTE: Here "*," makes x0 into a required keyword argument,
# i.e. you can't do _add_trace_to_fig(fig, 7), instead you
# must explicitly write _add_trace_to_fig(fig, x0=7).
def _add_trace_to_fig(fig, *, x, name=None):
    if name is None:
        name = str(x)
    y_trace = collatz_sequence(x)
    x_trace = list(range(1, 1 + len(y_trace)))
    fig.add_trace(go.Scatter(x=x_trace, y=y_trace, name=name))
