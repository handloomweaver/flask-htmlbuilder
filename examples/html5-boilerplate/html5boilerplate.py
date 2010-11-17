# -*- coding: utf-8 -*-
"""
    Flask-HTMLBuilder HTML5 Boilerplate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BETA
    
    Flask-HTMLBuilder root block based on HTML5 Boilerplate project:
    github.com/paulirish/html5-boilerplate
    
    Check demo.py for example usage.
    
    :copyright: (c) 2010 by Zahari Petkov.
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask, g, url_for, current_app

from flaskext.htmlbuilder import html, Attr

def static(filename):
    return url_for('.static', filename=filename)


# Using HTML5 Boilerplate v.0.9.5

def html5_boilerplate():
    return [
        html.doctype('html'),
        
        html.newline(),
        # paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/
        html.comment('[if lt IE 7 ]> <html lang="en" class="no-js ie6"> <![endif]'),
        html.comment('[if IE 7 ]>    <html lang="en" class="no-js ie7"> <![endif]'),
        html.comment('[if IE 8 ]>    <html lang="en" class="no-js ie8"> <![endif]'),
        html.comment('[if (gte IE 9)|!(IE)]><!'),
        html.html(lang='en', class_='no-js')(
            html.comment('<![endif]'),
            
            head(),
            body()
        )
    ]

def head():
    return html.head(
        html.meta(charset='utf-8'),
        
        html.newline(),
        # Always force latest IE rendering engine (even in intranet) & Chrome Frame
        # Remove this if you use the .htaccess
        html.meta(http_equiv='X-UA-Compatible', content='IE=edge,chrome=1'),
        
        html.newline(),
        html.join(
            html.title(
                html.block('title')
            )
        ),
        
        html.newline(),
        meta_description(),
        meta_author(),
        
        html.newline(),
        # Mobile viewport optimized: j.mp/bplateviewport
        html.meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        
        html.newline(),
        # Place favicon.ico & apple-touch-icon.png in the root of your domain and delete these references
        html.link(rel='shortcut icon', href=static('favicon.ico')),
        html.link(rel='apple-touch-icon', href=static('apple-touch-icon.png')),
        
        html.newline(),
        # CSS : implied media="all"
        html.link(rel='stylesheet', href=static('css/style.css')),
        
        # Uncomment if you are specifically targeting less enabled mobile browsers
        html.link(rel='stylesheet', media='handheld', href=static('css/handheld.css')),
        
        html.newline(),
        # All JavaScript at the bottom, except for Modernizr which enables HTML5 elements & feature detects
        html.script(src=static('js/libs/modernizr-1.6.min.js'))(),
    )


def meta_description():
    return html.has_attr('description')(
        html.meta(name='description', content=Attr('description'))
    )


def meta_author():
    return html.has_attr('author')(
        html.meta(name='author', content=Attr('author'))
    )


def body():
    return html.body(
        html.div(id='container')(
            html.has_block('header')(
                html.header(
                    html.block('header')
                ),
                html.newline()
            ),
            
            html.has_block('main')(
                html.div(id='main')(
                    html.block('main')
                )
            ),
            
            html.has_block('footer')(
                html.newline(),
                html.footer(
                    html.block('footer')
                )
            )
        ),
        
        body_end_scripts(),
    )


def body_end_scripts():
    return [
        jquery_include(),
        application_scripts(),
        dd_belatedpng(),
        yui_profiling(),
        async_analytics()
    ]


def jquery_include():
    return [
        # Javascript at the bottom for fast page loading
        html.newline(),
        # Grab Google CDN\'s jQuery. fall back to local if necessary '),
        html.script(src='//ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.js')(),
        html.script(
            html.safe(
                '''!window.jQuery && document.write(unescape('%3Cscript src="''' \
                + static('js/libs/jquery-1.4.2.js') + '''"%3E%3C/script%3E'))'''
            )
        ),
    ]


def application_scripts():
    """ Scripts concatenated and minified via a build script. """
    return [
        html.newline(),
        html.script(src=static('js/plugins.js'))(),
        html.script(src=static('js/script.js'))(),
    ]


def dd_belatedpng():
    """ Fix any <img> or .png_bg background-images. """
    return [
        html.newline(),
        html.comment('''[if lt IE 7 ]>
      <script src="/static/js/libs/dd_belatedpng.js"></script>
      <script> DD_belatedPNG.fix('img, .png_bg'); </script>
    <![endif]'''
        ),
    ]


def yui_profiling():
    # yui profiler and profileviewer - remove for production
    return [
        html.newline(),
        html.script(src=static('js/profiling/yahoo-profiling.min.js'))(),
        html.script(src=static('js/profiling/config.js'))(),
    ]


def async_analytics():
    """Asynchronous google analytics:
    mathiasbynens.be/notes/async-analytics-snippet
    """
    # ANALYTICS_SITE_ID in UA-XXXXX-X form.
    site_id = current_app.config.get('ANALYTICS_SITE_ID', None)
    
    if site_id is None:
        return None
    
    script = """
        var _gaq = [['_setAccount', '""" + site_id + """'], ['_trackPageview']];
        (function(d, t) {
         var g = d.createElement(t),
             s = d.getElementsByTagName(t)[0];
         g.async = true;
         g.src = ('https:' == location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
         s.parentNode.insertBefore(g, s);
        })(document, 'script');
    """
    
    return [
        html.newline(),
        html.script(html.safe(script))
    ]

