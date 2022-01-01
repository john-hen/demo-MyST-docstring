# Overview

Pretend this is the tutorial that gives a general introduction to the
library, providing usage examples and all that.

This is a stand-alone document, in this case a file named `overview.md`
inside the project's `docs` folder. So it is separate from the actual
Python library in the, unimaginatively named, `package` folder. Both
folders are right underneath the project's root in the repo.

We have set up the [](api.md) documentation as a different chapter. It
is also a stand-alone document, named `api.md`, and is linked in the
side bar on the left. Readers can go there to understand how the library
is to be used in application code. That is, it documents the *public*
API. Not every doc-string defined in `package` needs to show up there,
only the ones that are important. So we kick things off with a general
summary of the top-level objects, courtesy of a modified version of
Sphinx's [Autosummary] extension, which links to in-depth API documentation
provided by the a modified [Autodoc] extension.

We can then link to objects from the API documentation, such as
{any}`Class1` or {any}`action <package.action>`. The syntax is
`` {any}`Class1` `` and `` {any}`action <package.action>` `` (as the
latter reference happens to be ambiguous). This is the MyST-Markdown way
of referring to the Sphinx role `any`, which then basically looks in
*any* place to resolve the reference. [Alternatively][myst_autodoc], we
can write ``[`Class1`](Class1)`` and ``[`action`](Class2.action)`` to
create links to [`Class1`](Class1) and [`action`](Class2.action) with
a more Markdown-y syntax.

Some people like to document the API within the hand-written general
documentation as they go along. So instead of just referring to
{any}`Class1`, they pull in its doc-string somewhere in the text:

```{autoclass} package.classes.Class1
    :noindex:
```

[Intersphinx] is configured just like it is without MyST, so that we
get short-hand link targets to external documentation, like to Python's
[`pathlib`](python:pathlib) module with ``[`pathlib`](python:pathlib)``.

As opposed to reST, we can nest mark-up inside link text, like [a
`literal`](https://example.org). No Markdown parser has ever had a
problem with that.


(first-steps)=
## First steps

This is a section inside the Overview chapter. We have marked it as
a possible link target by putting `(first-steps)=` right above the
section header. Though MyST would also [generate anchors][autoanchors]
automatically, for sections up to a given level, if we specify e.g.
`myst_heading_anchors = 2` in `conf.py`.

Maybe it's time for a code example:
```python
from package.classes import Class1

class1 = Class1()
class1.action()
```

We used triple back-ticks (` ``` `) to mark the code block. We could
also use triple colons (`:::`) if we add `myst_enable_extensions =
['colon_fence']` to the configuration.

MyST has nothing to do with the syntax highlighting. It works just like
with Sphinx alone, and as such is defined by the theme, here [Furo].
Click the icon at the top right of the page to switch between dark and
light mode and notice how the highlighting changes along with it. We
could easily replace Furo with any of a number of [Sphinx themes][themes].

[Autodoc]:      https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[Autosummary]:  https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[myst_autodoc]: https://myst-parser.readthedocs.io/en/latest/sphinx/use.html#use-sphinx-ext-autodoc-in-markdown-files
[Intersphinx]:  https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
[autoanchors]:  https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#auto-generated-header-anchors
[Furo]:         https://pradyunsg.me/furo
[themes]:       https://sphinx-themes.org
