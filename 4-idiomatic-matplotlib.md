# How to do `matplotlib` idiomatically.

Plotting is a common data science activity. In this section, you will see how to write matplotlib code idiomatically.

Below is the code demo with annotations on what are important.

```python
# plotting.py
def plot_ts(df: pd.DataFrame, colname: str, ax: mpl.axes):
    """
    Plot the time series data. (Write intent of function!)

    This is an example of code refactoring. We take the repetitive part of the
    code and wrap it inside a function with an API that makes sense.
    (Write additional details below the intent.)

    (Finally, define the parameters. If you do this right, then you will have
    access to the docstrings in Jupyter! `plot_ts??`)
    :param df: A pandas DataFrame
    :param colname: The column of data to plot.
    :param ax: A matplotlib axes object.
    :returns: The matplotlib axes object passed in.
    """
    # Defensive programming checks, also makes handling errors easier for user.
    assert colname in df, f"{colname} not present in dataframe df."
    assert isinstance(ax, mpl.axes)

    # Business logic: about 3-7 lines.
    ax.plot(df.index, df[colname], color='blue')
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    return x
```

```python
# notebook.ipynb
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
from .plotting import plot_ts

df = pd.DataFrame(...)

# Idiomatic matplotlib involves first instantiating the figure.
fig = plt.figure()

# For really sophisticated layouts, use GridSpec. You can slice GridSpec
# objects, btw, to make axes objects span more than one cell in the grid!
# https://matplotlib.org/users/gridspec.html
gs = GridSpec(nrows=2, ncols=2)
columns = ['m1', 'm2', 'm3', 'm4']
axes = dict()
for i, col in enumerate(columns):  # enumerate is a really powerful builtin function.
    # Remember: all plotting happens on the axes object.
    axes[col] = fig.add_subplot(gs[i])
    axes[col] = plot_ts(df, col, axes[col])

plt.show()
```

## References

- [`matplotlib` GridSpec](https://matplotlib.org/users/gridspec.html)
