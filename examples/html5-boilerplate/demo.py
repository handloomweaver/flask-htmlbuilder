from flask import Flask

from flaskext.htmlbuilder import init_htmlbuilder, html, render_template, \
     render, Attr, root_block, block

from html5boilerplate import html5_boilerplate


app = Flask(__name__)
init_htmlbuilder(app)


@app.route('/')
def index():
    html.block('title')(
        'Element Consistency Tests'
    )
    return render_template()


@root_block()
def html5_root():
    return html5_boilerplate()


@block('main', html5_root)
def body_main():
    return [
        html.comment("""
            demo content lovingly lifted from the azbuka project 
            http://code.google.com/p/azbuka/ 
                 
            and the bluetrip project
            http://bluetrip.org/  
                 
            and peter beverloo
            http://peter.sh/examples/?/html/meter-progress.html
        """),
        html.h1('Title 01 Heading'),
        html.hr,
        html.h2('Level 02 Heading'),
        html.join(
            html.p(
                'Lorem ipsum ', html.em('emphasised text'), ' dolor sit amet, ',
                html.strong('strong text'), ' consectetur adipisicing elit, ',
                html.abbr(title='')('abbreviated text'),
                ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut ',
                html.q('quoted text'),
                ' enim ad minim veniam, quis nostrud exercitation ',
                html.a(href='/')('link text'),
                ' ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute ',
                html.ins('inserted text'),
                ' irure dolor in reprehenderit in voluptate velit esse cillum' \
                ' dolore eu fugiat nulla pariatur. Excepteur sint occaecat ',
                html.code('code text'),
                ' cupidatat non proident, sunt in culpa qui officia deserunt' \
                'mollit anim id est laborum.'
            )
        ),
        html.p(
            html.join(
                'Suspendisse rhoncus, est ac sollicitudin viverra, leo orci sagittis massa, sed condimentum ',
                html.acronym(title='')('acronym text'),
                ' est tortor a lectus. Curabitur porta feugiat ullamcorper. Integer ' \
                'lacinia mi id odio faucibus eget tincidunt nisl iaculis. Nam ' \
                'adipiscing hendrerit turpis, et porttitor felis sollicitudin et. ' \
                'Donec dictum massa ac neque accumsan tempor. Cras aliquam, ipsum ' \
                'sit amet laoreet hendrerit, purus ', html.del_('deleted text'),
                ' sapien convallis dui, et porta leo ipsum ac nunc. Nullam ' \
                'ornare porta dui ac semper. Cras aliquam laoreet hendrerit. ' \
                'Quisque vulputate dolor eget mi porta vel porta nisl pretium. ' \
                'Vivamus non leo magna, quis imperdiet risus. Morbi tempor ' \
                'risus placerat tellus imperdiet fringilla.'
            )
        ),

        html.blockquote(
            html.join(
                html.p(
                    'I am not one who was born in the possession of knowledge; ' \
                    'I am one who is fond of antiquity, and earnest in seeking it there.'
                )
            )
        ),
        
        html.join(
            html.p(
                html.cite(
                    html.a(href='/')(
                        'Confucius, The Confucian Analects'
                    )
                ),
                ',  (551 BC - 479 BC)'
            )
        ),
        
        html.h3('Level 03 Heading'),
        
        html.join(
            html.p(
                'Extended paragraph. ', html.a(href='')('Lorem ipsum'),
                ' dolor sit amet, consectetur adipisicing elit, sed do eiusmod ' \
                'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad ' \
                'minim veniam, quis nostrud exercitation ullamco laboris nisi ' \
                'ut aliquip ex ea commodo consequat. Duis aute irure dolor in ' \
                'reprehenderit in voluptate velit esse cillum dolore eu fugiat ' \
                'nulla pariatur. Excepteur sint occaecat cupidatat non ' \
                'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
            )
        ),
        
        html.ol(
            html.li('Unus'),
            html.li('Duo'),
            html.li('Tres'),
            html.li('Quattuor')
        ),

        html.p(
            'Duis aute irure dolor in reprehenderit in voluptate velit esse ' \
            'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat ' \
            'cupidatat non proident, sunt in culpa qui officia deserunt ' \
            'mollit anim id est laborum.'
        ),
        
        html.h3('Header 3'),
        
        html.p(
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed ' \
            'do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        ),

        html.h4('Unordered lists'),
        html.ul(
            html.li('Lorem ipsum dolor sit amet'),
            html.li('Consectetur adipisicing elit'),
            html.li('Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'),
            html.li('Ut enim ad minim veniam'),
        ),
        html.p(
            'Lorem ipsum dolor sit amet,consectetur adipisicing elit, sed ' \
            'do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        ),
    
        html.pre(
            html.code("""
                body { font:0.8125em/1.618 Arial, sans-serif; 
                background-color:#fff;  
                color:#111; }
            """)
        ),

        html.p(
            """Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
            anim id est laborum."""
        ),
        
        html.h4('Header 4'),
        
        html.p("""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt 
            ut labore et dolore magna aliqua.
        """),

        html.dl(
            html.dt('Definition list'),
            html.dd("""
                Consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
                aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
                commodo consequat.
            """),
            html.dt('Lorem ipsum dolor sit amet'),
            html.dd("""
                Consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
                aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
                commodo consequat.
            """),
        ),

        html.p("""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt 
            ut labore et dolore magna aliqua.
        """),

        html.h4('Ordered list'),
        html.ol(
            html.li('List item'),
            html.li('List item'),
            html.li(
                'List item', 
                html.ol(
                    html.li('List item level 2'),
                    html.li(
                        'List item level 2',
                        html.ol(
                            html.li('List item level 3'),
                            html.li('List item level 3')
                        )
                    )
                )
            )
        ),
        html.h4('Unordered list'),
        html.ul(
            html.li('List item 01'),
            html.li('List item 02'),
            html.li(
                'List item 03',
                html.ul(
                    html.li('List item level 2'),
                    html.li(
                        'List item level 2',
                        html.ul(
                            html.li('List item level 3'),
                            html.li('List item level 3')
                        )
                    )
                )
            )
        ),
 
        html.p("""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt 
            ut labore et dolore magna aliqua.
        """),

        html.h4('Tables'),
        html.table(summary='Jimi Hendrix albums')(
            html.caption('Jimi Hendrix - albums'),
            html.thead(
                html.tr(
                    html.th('Album'),
                    html.th('Year'),
                    html.th('Price')
                )
            ),
            html.tfoot(
                html.tr(
                    html.td('Album'),
                    html.td('Year'),
                    html.td('Price')
                )
            ),
            html.tbody(
                html.tr(
                    html.td('Are You Experienced '),
                    html.td('1967'),
                    html.td('$10.00')
                ),
                html.tr(
                    html.td('Axis: Bold as Love'),
                    html.td('1967'),
                    html.td('$12.00')
                ),
                html.tr(
                    html.td('Electric Ladyland'),
                    html.td('1968'),
                    html.td('$10.00')
                ),
                html.tr(
                    html.td('Band of Gypsys'),
                    html.td('1970'),
                    html.td('$12.00')
                )
            )
        ),
        
        html.p(
            html.join('I am ', html.a(href='http://devkick.com/lab/tripoli/sample.php?abc123')('the a tag'), ' example', html.br),
            
            html.join('I am ', html.abbr(title='test')('the abbr tag'), ' example', html.br),
            
            html.join('I am ', html.acronym('the acronym tag'), ' example', html.br),
            html.join('I am ', html.b('the b tag'), ' example', html.br),
            html.join('I am ', html.big('the big tag'), ' example', html.br),
            
            html.join('I am ', html.cite('the cite tag'), ' example', html.br),
            
            html.join('I am ', html.code('the code tag'), ' example', html.br),
            html.join('I am ', html.del_('the del tag'), ' example', html.br),
            html.join('I am ', html.dfn('the dfn tag'), ' example', html.br),
            
            html.join('I am ', html.em('the em tag'), ' example', html.br),
            
            html.join('I am ', html.font(face='verdana')('the font tag'), ' example', html.br),
            html.join('I am ', html.i('the i tag'), ' example', html.br),
            html.join('I am ', html.ins('the ins tag'), ' example', html.br),
            
            html.join('I am ', html.kbd('the kbd tag'), ' example', html.br),
            
            html.join('I am ', html.q('the q tag ', html.q('inside'), ' a q tag'), ' example', html.br),
            html.join('I am ', html.s('the s tag'), ' example', html.br),
            html.join('I am ', html.samp('the samp tag'), ' example', html.br),
            
            html.join('I am ', html.small('the small tag'), ' example', html.br),
            html.join('I am ', html.span('the span tag'), ' example', html.br),
            html.join('I am ', html.strike('the strike tag'), ' example', html.br),
            html.join('I am ', html.strong('the strong tag'), ' example', html.br),
            
            html.join('I am ', html.sub('the sub tag'), ' example', html.br),
            html.join('I am ', html.sup('the sup tag'), ' example', html.br),
            html.join('I am ', html.tt('the tt tag'), ' example', html.br),
            html.join('I am ', html.var('the var tag'), ' example', html.br),
            
            html.join('I am ', html.u('the u tag'), ' example')
        ),
        
        html.join(html.p('This is a <p> with some ', html.code('code'), ' inside.')),
        
        html.h3('What is Lorem Ipsum?'),
        
        html.join(
            html.p(
                html.b('Lorem Ipsum'), ' is simply dummy text of the printing ' \
                'and typesetting industry. Lorem Ipsum has been the industry\'s ' \
                'standard dummy text ever since the 1500s, when an unknown ' \
                'printer took a galley of type and scrambled it to make a type ' \
                'specimen book. It has survived not only five centuries, but ' \
                'also the leap into electronic typesetting, remaining ' \
                'essentially unchanged. It was popularised in the 1960s with ' \
                'the release of Letraset sheets containing Lorem Ipsum ' \
                'passages, and more recently with desktop publishing software ' \
                'like Aldus PageMaker including versions of Lorem Ipsum.'
            )
        ),
        
        html.join(
            html.p(
                html.strong('This'), ' Lorem Ipsum HTML example is created ' \
                'from the parts of Placeholder Markup with Lorem Ipsum - ' \
                'Jon Tan, Emastic CSS Framework, Tripoli CSS Framework and ' \
                'Baseline CSS Framework .'
            )
        ),
        html.address('Address: somewhere, World'),
        
        html.p(
            html.a(href='#')('Link'), html.br,
            html.strong('<strong'), html.br,
            html.del_('<del> deleted'), html.br,
            html.dfn('<dfn> dfn'), html.br,
            html.em('<em> emphasis'), html.br
        ),
    
        html.pre(
            html.code('<html>'),
            html.code('<head>'),
            html.code('</head>'),
            html.code('<body>'),
            html.code('<div class = "main"> <div>'),
            html.code('</body>'),
            html.code('</html>')
        ),
        
        html.tt('<tt> Pellentesque tempor, dui ut ultrices viverra, neque urna blandit nisi, id accumsan dolor est vitae risus.'),
        
        html.hr,
        
        html.comment(' this following markup from http://bluetrip.org/ '),
        html.dl(
            html.dt('Description list title 01'),
            
            html.dd('Description list description 01'),
            html.dt('Description list title 02'),
            html.dd('Description list description 02'),
            html.dd('Description list description 03'),
        ),
        
        html.table(
            html.caption('Table Caption'),
        
            html.thead(
                html.tr(
                    html.th('Table head th'),
                    html.td('Table head td')
                )
            ),
            
            html.tfoot(
                html.tr(
                    html.th('Table foot th'),
                    html.td('Table foot td')
                )
            ),
            
            html.tbody(
                html.tr(
                    html.th('Table body th'),
                    html.td('Table body td')
                ),
                html.tr(
                    html.td('Table body td'),
                    html.td('Table body td')
                )
            )
        
        ),
        
        html.hr,

        html.form(action='#')(
            html.fieldset(
                html.legend('Form legend'),
                
                html.join(
                    html.div(
                        html.label(for_='f1')('Optional Text input:'),
                        html.input(type='text', id='f1', value='input text')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='rt1')('Required Text input:'),
                        html.input(type='text', id='rt1', required='required')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='twp1')('Text input with pattern requirement and placeholder:'),
                        html.input(
                            type='text',
                            pattern='\d{5}(-\d{4})?',
                            title='a US Zip code, with or without the +4 exension',
                            placeholder='12345-6789'
                        )
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='s1')('Search input:'),
                        html.input(type='search', id='s1')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='e1')('Email input:'),
                        html.input(type='email', id='e1')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='u1')('URL input:'),
                        html.input(type='url', id='u1')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='pw')('Password input:'),
                        html.input(type='password', id='pw', value='password')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='f2')('Radio input:'),
                        html.input(type='radio', id='f2')
                    )
                ),
                
                html.join(
                    html.div(
                        html.label(for_='f3')('Checkbox input:'),
                        html.input(type='checkbox', id='f3')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='f4')('Select field:'),
                        html.select(id='f4')(
                            html.option('Option 01'),
                            html.option('Option 02')
                        )
                    )
                ),
                
                html.join(
                    html.div(
                        html.label(for_='f5')('Textarea:'),
                        html.textarea(id='f5', cols='30', rows='5')('Textarea text')
                    )
                ),
                html.join(
                    html.div(
                        html.label(for_='f6')('Input Button:'),
                        html.input(type='button', id='f6', value='button text')
                    )
                ),
                
                html.join(
                    html.div(
                        html.label(for_='f7')('Submit Button:'),
                        html.input(type='submit', id='f7', value='button text')
                    )
                )
            )
        ),
        
        html.comment(' thx peter beverloo: http://peter.sh/examples/?/html/meter-progress.html '),
        
        
        html.p(id='no-support', style='color: red; margin-bottom: 12px;')(
            html.join(
                'Your browser does not support these elements yet! Consider downloading a ',
                html.a(href='http://tools.peter.sh/download-latest-chromium.php')('Chromium Nightly'), '.', html.br
            )
        ),
        
        html.h3('<progress>'),
        html.p(
            html.join(
                'The progress element (spec: ',
                html.a(href='http://www.whatwg.org/specs/web-apps/current-work/multipage/the-button-element.html#the-progress-element')('4.10.16'),
                ') represents the completion progress of a task and can be both indeterminate as determinate.'
            )
        ),
        html.ul(class_='compact')(
            html.li(
                html.label('Indeterminate'),
                html.progress(max='100')(),
            ),
            html.li(
                html.label('Progress: 0%'),
                html.progress(max='10', value='0')()
            ),
            html.li(
                html.label('Progress: 100%'), 
                html.progress(max='3254', value='3254')()
            ),
            html.li(
                html.label('Progress: 57%'),
                html.progress(max='0.7', value='0.4')()
            ),
            html.li(
                html.label('Javascript'),
                html.progress(id='progress-javascript-example')()
            )
        ),
        
        html.h3('<meter>'),
        html.p(
            html.join(
                'Displaying a scalar measurement within a known range, like hard drive ' \
                'usage, can be done using the meter element (spec: ',
                html.a(href='http://www.whatwg.org/specs/web-apps/current-work/multipage/the-button-element.html#the-meter-element')('4.10.17'),
                ')'
            )
        ),
        
        html.ul(class_='compact')(
            html.li(
                html.label('Meter: empty'),
                html.meter(value='0')()
            ),
            html.li(
                html.label('Meter: full'),
                html.meter(value='1')()
            ),
            html.li(
                html.label('Meter: "a bit"'),
                html.meter(min='.34', max='.41', value='.36')()
            ),
            html.li(
                html.label('Preferred usage'),
                html.meter(min='50', max='250', low='100', high='200', value='120')()
            ),
            html.li(
                html.label('Too much traffic'),
                html.meter(min='1024', max='10240', low='2048', high='8192', value='9216')()
            ),
            html.li(
                html.label('Optimum value'),
                html.meter(value='.5', optimum='.8')()
            ),
            html.li(
                html.label('Javascript'),
                html.meter(id='meter-javascript-example', value='0')()
            )
        ),
        
        html.script(html.safe("""
          (function () {
              if (! ('position' in document.createElement ('progress'))) {
                  var elements = document.querySelectorAll ('meter, progress');
                  for (var i = 0, j = elements.length; i < j; i++) {
                    elements [i].style.border = "1px solid red";
                    elements [i].style.height = "12px";
                    elements [i].style.display = "inline-block";
                    elements [i].style.webkitAppearance = "none";
                  }
                  
                  return ;
              }
              
              document.getElementById ('no-support').style.display = 'none';
              
              /** Setup the <progress> JavaScript example **/
              var progressExample = document.getElementById ('progress-javascript-example');
              progressExample.min = 50;
              progressExample.max = 122;
                  
              setInterval (function ()
              {
                  progressExample.value = progressExample.min + Math.random () * (progressExample.max - progressExample.min);
              
              }, 1000);
              
              /** We'd like some fancy <meter> examples too **/
              var meterExample = document.getElementById ('meter-javascript-example');
              meterExample.min = 0;
              meterExample.max = 100;
              meterExample.value = 50;
              meterExample.low  = 20;
              meterExample.high = 80;
              meterExample.optimum = 65;
                  
              setInterval (function ()
              {
                  meterExample.value   = meterExample.min + Math.random () * (meterExample.max - meterExample.min);
                  meterExample.optimum = 65 + (5 - Math.random () * 10);
              
              }, 1000);
              
          })();
        """))
    
    ]

if __name__ == '__main__':
    app.run(debug=True)

