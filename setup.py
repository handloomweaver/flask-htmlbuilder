"""
Flask-HTMLBuilder
-----------------

Flask-HTMLBuilder is an extension to `Flask`_ that allows flexible Python-only
generation of HTML snippets and full HTML documents using a flexible syntax.
For more advanced usage it provides a lean template inheritance system that
is intertwined with the Flask/Werkzeug endpoint mechanisms.

Links
`````

* `documentation <http://packages.python.org/Flask-HTMLBuilder>`_
* `development version
  <http://github.com/majorz/flask-htmlbuilder/zipball/master#egg=Flask-HTMLBuilder-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-HTMLBuilder',
    version='0.3',
    url='http://github.com/majorz/flask-htmlbuilder',
    license='MIT',
    author='Zahari Petkov',
    author_email='zarchaoz@gmail.com',
    description='Flexible Python-only HTML generation for Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    tests_require=[
        'nose'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
