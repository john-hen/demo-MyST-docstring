"""
This is the first line in the doc-string of module `actions`.

We can reference other objects, such as {any}`Class1` and [`Class2`](Class2).
We can link back to one of the main documents as a whole, for example
[Overview](../overview.md), or [a specific section](first-steps). We can
create external cross-references like to [`Path`](python:pathlib.Path)
thanks to the [Intersphinx] extension.

And we can have highlighted code examples:
```python
from package import action
from package import Class1

action(do='whatever')
class1 = Class1()
class1.action()
```

Sphinx created this page from a "stub" file named `package.actions.md`
in the `api` folder underneath `docs`. As you can tell from clicking
"Show Source" at the bottom of this very page, it contains very little:
````markdown
# actions

```{automodule} package.actions
```
````

[Autodoc] takes care of the rest and fills in the blanks, pulling in
signatures and doc-strings from the package's source code. [Autosummary]
would even create these stubs automatically, unless we tell it not to.
We can also look at the source code of the `action` function, of this
whole module in fact, if we click on the `[source]` link on the right,
which is there courtesy of the [Viewcode] extension.

[Intersphinx]: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
[Autodoc]:     https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[Autosummary]: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[Viewcode]:    https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
"""


def action(do='something'):
    """
    This is the first line in the doc-string of function `action`.

    It is defined in module [`actions`](actions).
    """
    pass
