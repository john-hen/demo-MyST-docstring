"""Sphinx configuration for rendering the documentation"""

from pathlib import Path
import sys
import logging

# Module search path
here = Path(__file__).absolute().parent
sys.path.insert(0, str(here.parent))
sys.path.insert(0, str(here/'extensions'))

# Sphinx extensions
extensions = [
    'myst_parser',                     # Accept Markdown as input.
    'myst_docstring',                  # Get documentation from doc-strings.
    'myst_summary',                    # Create summaries automatically.
    'sphinx.ext.viewcode',             # Include highlighted source code.
    'sphinx.ext.intersphinx',          # Support short-hand web links.
    'log_autodoc',                     # Save Autodoc log.
]

# Meta information
project    = 'demo-MyST-docstring'
html_title = project

# Source parsing
root_doc = 'index'                     # start page
nitpicky = True                        # Warn about missing references?

# Short-hand web links
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Code documentation
autodoc_default_options = {
    'members':       True,             # Include module/class members.
    'member-order': 'bysource',        # Order members as in source file.
}
autosummary_generate = False           # Stub files are created by hand.
add_module_names = False               # Don't prefix members with module name.

# Rendering options
html_show_copyright = False            # Show copyright notice in footer?
html_show_sphinx    = True             # Show Sphinx blurb in footer?
html_copy_source    = True             # Copy documentation source files?
html_theme          = 'furo'           # custom theme with light and dark mode
pygments_style      = 'friendly'       # syntax highlight style in light mode
pygments_dark_style = 'stata-dark'     # syntax highlight style in dark mode
