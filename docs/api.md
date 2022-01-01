# API

This is the front page for the API documentation. It uses a modified
version ("MyST-summary") of the built-in Sphinx extension [Autosummary],
which creates an overview page that links to individual pages created by
a modified [Autodoc] extension ("MyST-docstring").

```{currentmodule} package
```

```{autosummary}
:toctree: api
:nosignatures:

action
actions
classes
```

[Autodoc]:     https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[Autosummary]: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
