# bdc-readthedocs-theme

Brazil Data Cube Theme for Sphinx readthedocs.

## Installation

Clone `bdc-readthedocs-theme` repository:

```bash
git clone https://github.com/brazil-data-cube/bdc-readthedocs-theme.git
cd bdc-readthedocs-theme
```

Install to Python library:

```bash
python setup.py install
```

## Configuration

Add the following code to your `conf.py`:

```python
import bdc_theme

html_theme_path = bdc_theme.html_theme_path()
html_theme = 'bdc_theme'

extensions.append("bdc_theme")

html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "Name of the project",
}
```
