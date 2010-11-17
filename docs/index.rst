Flask-HTMLBuilder
=================

.. module:: flaskext.htmlbuilder

Flask-HTMLBuilder is a `Flask`_ extension that allows **flexible** and 
**easy** Python-only generation of HTML snippets and full HTML documents using
a robust syntax.  For more advanced usage it provides a lean template
inheritance system that is intertwined with the Flask/Werkzeug endpoint
mechanisms.


Installation
------------

Install with **pip**::

    $ pip install Flask-HTMLBuilder

Or **easy_install**::

    $ easy_install Flask-HTMLBuilder
    
    
A Simple Example
----------------

Nothing should be more simple than a `Hello World!` example::

    from flask import Flask
    from flaskext.htmlbuilder import html, render
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('Hello')
                ),
                html.body(
                    'Hello World!'
                )
            )
        ])
    
    if __name__ == '__main__':
        app.run()


The resulting response of the `hello` view will correspondingly be:

.. code-block:: html

    <!doctype html>
    <html lang="en">
      <head>
        <title>Hello</title>
      </head>
      <body>Hello World!</body>
    </html>


Detailed explanation on how the :data:`flaskext.htmlbuilder.html` instance is
used can be found in the API reference below.


Template Inheritance
--------------------

The most distinctive feature of Flask-HTMLBuilder to other libraries with a
similar approach is that it targets full HTML document generation through
a template inheritance system.  To use it you need to initialize the
extension and import the template rendering function and the necessary
decorators for creating the template block hierarchy::

    from flask import Flask, g
    from flaskext.htmlbuilder import html, init_htmlbuilder, root_block, block, \
         render_template
    
    app = Flask(__name__)
    init_htmlbuilder(app)

The :func:`flaskext.htmlbuilder.init_htmlbuilder` function creates for each
request the `g.blocks` and `g.attrs` variables, which are dictionary instances.
The `g.blocks` dictionary is populated with different HTML blocks that are
created using the :data:`flaskext.htmlbuilder.html` instance during the
template HTML block assembling process.  The `g.attrs` dictionary is used for
populating the attributes of different HTML elements with data passed from the
view functions, e.g. the description of a document defined as a `meta` element.

The template rendering process is divided into two parts -- HTML block
assembling and rendering the resulting tree structure to indented
HTML code.

Let's continue the example::
    
    @app.route('/logo')
    def logo():
        g.blocks['title'] = 'Flask Logo'
        return render_template()
    
    @app.route('/intro')
    def intro():
        g.blocks['title'] = 'Flask Introduction'
        return render_template()

Two views are defined above.  The document title is explicitly stored in the
`g.blocks` dictionary -- the simplest block form is a string representing
HTML text.

.. code-block:: python

    @root_block()
    def html_base():
        return [
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title(
                        g.blocks.get('title', 'Default Title')
                    )
                ),
                html.body(
                    g.blocks.get('body')
                )
            )
        ]


The :func:`flaskext.htmlbuilder.root_block` decorator is used to define the base
HTML block function, which returns the HTML skeleton of the document.  In the
above example the root block function uses two variables from the `g.blocks`
dictionary -- the `title` which is set explicitly in the view functions, and
the `body` which will be defined by the child block functions below::

    @block('body', html_base)
    def logo_body():
        return html.img(src='http://flask.pocoo.org/static/logo.png')


The :func:`flaskext.htmlbuilder.block` decorator is used to define the
descendant blocks of the root block inside the hierarchy.  The first parameter
defines in which context variable in the `g.blocks` dictionary the resulting
block will be stored for usage by the parent block function -- in the case
above the `body` content.  The direct parent function in the template hierarchy
is defined by the second parameter -- in the case above the root block function.
The third parameter defines the view function in which execution context the
block will take an effect. It is omitted in the case above, which means that
the block function will be used as a default block function for the context name
specified in the first parameter.  The view function parameter is used in the
block definition below::

    @block('body', html_base, intro)
    def intro_body():
        return html.blockquote(
            html.p(
                html.join(
                    'Flask is a microframework for Python based on Werkzeug, ' \
                    'Jinja 2 and good intentions. And before you ask: It\'s ',
                    html.a(href='http://flask.pocoo.org/doc/license/')(
                        'BSD licensed'
                    ), '!'
                )
            )
        )


The :func:`flaskext.htmlbuilder.html` instance provides a few specialized
helper methods like `html.join` and `html.doctype` which are described in the
API reference section.

Finally, the two views will produce the following results:

.. code-block:: html

    <!doctype html>
    <html lang="en" class="no-js">
      <head>
        <title>Flask Logo</title>
      </head>
      <body>
        <img src="http://flask.pocoo.org/static/logo.png">
      </body>
    </html>


.. code-block:: html

    <!doctype html> 
    <html lang="en">
      <head>
        <title>Flask Introduction</title>
      </head>
      <body>
        <blockquote>
          <p>
            Flask is a microframework for Python based on Werkzeug, Jinja 2 and
            good intentions. And before you ask: It's
            <a href="http://flask.pocoo.org/doc/license/">BSD licensed</a>!
          </p>
        </blockquote>
      </body>
    </html>


API Reference
-------------

This section documents each public function or class from the extension.


Configuration
`````````````

.. autofunction:: flaskext.htmlbuilder.init_htmlbuilder


HTML Generation
```````````````

.. autodata:: flaskext.htmlbuilder.html

The :data:`flaskext.htmlbuilder.html` instance has some special methods that
are internally dispatched to the following classes:


General
'''''''

.. autoclass:: Doctype

.. autoclass:: Comment

.. autoclass:: Safe

.. autoclass:: Join

.. autoclass:: NewLine


Template Inheritance Related
''''''''''''''''''''''''''''

.. autoclass:: HasBlock

.. autoclass:: BlockElement

.. autoclass:: HasAttr


Rendering
`````````

.. autofunction:: flaskext.htmlbuilder.render


Template Inheritance
````````````````````

.. autofunction:: flaskext.htmlbuilder.render_template

.. autofunction:: flaskext.htmlbuilder.root_block

.. autofunction:: flaskext.htmlbuilder.block

.. autoclass:: flaskext.htmlbuilder.RootBlock

.. autoclass:: flaskext.htmlbuilder.Block

.. autoclass:: flaskext.htmlbuilder.Context

.. autoclass:: flaskext.htmlbuilder.Attr


.. _Flask: http://flask.pocoo.org/

