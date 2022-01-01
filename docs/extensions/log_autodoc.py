"""Logs the output of the Autodoc extension to a file."""
__version__ = '1.0.0'


import logging


def setup(app):
    """Sets up the extension."""
    logger    = logging.getLogger('sphinx.sphinx.ext.autodoc')
    handler   = logging.FileHandler('autodoc.txt', mode='w', encoding='UTF-8')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return {'version': __version__, 'parallel_read_safe': True}
