# Data Cleaning

This is really just an advertisement for [`pyjanitor`](http://pyjanitor.readthedocs.io), a package that I wrote that enables data cleaning to be made really easy. Check out [the project](http://pyjanitor.readthedocs.io) to learn more!

## Example

```python
import pandas as pd
import janitor  # all you have to do is "import janitor"

df = pd.DataFrame(...)

# Once pyjanitor is imported, its functions are registered onto the pandas
# DataFrame object as class methods. You can then call them as if they were
# part of pandas!
#
# One highlight of pyjanitor is method chaining: as all functions return the
# dataframe that was passed to it, the next data preprocessing method can be
# called directly.
df_clean = (df.clean_names()
            .remove_empty()
            .rename_column('%_allocated', 'percent_allocated')
            .rename_column('full_time?', 'full_time')
            .coalesce(['certification', 'certification.1'], 'certification')
            .convert_excel_date('hire_date'))
```

## Installation

Using the `conda` package manager:

```
$ conda install -c conda-forge pyjanitor
```

Using the `pip` package installer:

```
$ pip install pyjanitor
```
