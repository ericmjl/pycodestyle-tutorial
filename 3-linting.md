# How to lint your code to find code style issues

For a data scientist, there are a few ways to do this. Let's examine the following use cases.

## A. Live while writing your script.

The most efficient way to check for coding errors is to use a code linter while writing your `.py` file. Atom's code linter will automatically find errors that are cropping up.

## B. Through the terminal.

A less efficient way to do this is through the terminal.

You have a project set up as such:

```
- project/
    |- data/
        |- table1.csv
    |- script1.py
    |- script2.py
    |- notebook1.ipynb
```

If you're using the terminal, assuming you have `flake8` installed in your current Python environment, you can run the following command in the `project/` directory:

```bash
$ flake8 .
```

In your terminal, you will get back a list of issues that are cropping up. You can kill those bugs one by one.

## C. Jupyter notebooks

There are Jupyter notebook extensions available to do code linting! Install `jupyter-contrib-nbextensions`:

```bash
$ conda install -c conda-forge jupyter_contrib_nbextensions
```

Then, run the following command to install the notebook extensions in your user path, which will make it available to all `conda` environments that you're using:

```bash
jupyter contrib nbextension install --user
```

Now, run a notebook session, find the `Nbextensions` tab, and enable the following for code linting:

- Autopep8 (be sure to `conda install autopep8` in your environment)
- Ruler (adds a vertical red line at the 79 character mark)

Feel free to also enable more extensions!
