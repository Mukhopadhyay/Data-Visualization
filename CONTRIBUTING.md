# Contributing


[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

Contributions are welcome, and they are greatly appreciated! Every bit helps, and credit will always be given. You can contribute in many ways.

# Types of Contributions

## Contributing code

If you want to add a new category of plots, which is missing in the `visualizations` directory, all you'd have to do is create a new folder with the name of the plot, e.g., **visualiazations/Piechart**

Afterwards add your notebook inside the directory with the following naming conventions,

`{Type_Of_Chart}s.ipynb`

For example, for **visualizations/Piechart** it would simply be `Piecharts.ipynb`. The first cell of your notebook should be the following code block

```python
import sys; sys.path.append('../../utils')
import utils

# Your dependencies goes here
```

## Report errors / deprecated info in project

# Write Documentation

**Working on your first Pull request?** You can learn how from this _free_ series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)