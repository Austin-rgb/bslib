from random import randint

class Element:
    def __init__(self, *elements, attributes=None):
        if attributes is None:
            attributes = {}
        self.elements = []
        self.history = []
        self.inner_html = ''
        self._html = ''
        self._id = randint(1000, 10000)
        self._hierarchy_level = 0
        self._updating_hierarchy = False
        if len(elements) > 0:
            if not isinstance(elements[0], str):
                new = list(elements)
                for n in new:
                    n._update_hierarchy_level(self._hierarchy_level+1)

                self.elements = new

            else:
                self.inner_html = elements[0]
                
        self._changed = True
        self.attributes = attributes
        self.is_container = False
        self.symbol = ''

    def _update_hierarchy_level(self, level):
        if self._updating_hierarchy:
            raise Exception('Circular hierarchy detected')
        self._hierarchy_level += level
        self._updating_hierarchy = True
        for elem in self.elements:
            elem._update_hierarchy_level(level + 1)

        self._updating_hierarchy = False


    def insert(self, *args):
        new = list(args)
        for n in new:
            n._update_hierarchy_level(self._hierarchy_level + 1)
            
        self.elements.extend(new)

    def set(self, name: str, value: str):
        self.history.append(f'setting {self}: {name}="{value}"')
        if name == 'class' and 'class' in self.attributes.keys():
            if value in self.attributes[name]:
                return
            self.attributes[name] = self.attributes[name] + ' ' + value
        else:
            self.attributes[name] = value

    def generate_attributes(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def generate(self):
        if not self._changed:
            return self._html
            
        html = '<'
        html += self.symbol
        html += ' ' + self.generate_attributes()
        
        if self.is_container:
            html += '>' + self.inner_html
            for elem in self.elements:
                html += '\n'

                html += elem.generate()

            html += '</' + self.symbol + '>'
            
        else:
            html += '/>'
            
        self._changed = False 
        if self.symbol == 'html':
            html = '<!doctype html >' + html
        self._html = html
        return html
        
    def save_html(self,filename):
        new_file = open(filename,'x+')
        new_file.write(self.generate())
        
    def __repr__(self):
        return self.symbol + f' object id={self._id}: '


def queen_html(symbol, is_container=False):
    class HtmlElement(Element):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.symbol = symbol
            self.is_container = is_container

    return HtmlElement


A = queen_html('a', True)
Body = queen_html('body', True)
Button = queen_html('button', True)
B = queen_html('b', True)
Div = queen_html('div', True)
Fieldset = queen_html('fieldset', True)
Form = queen_html('form', True)
Head = queen_html('head', True)
Html = queen_html('html', True)
Img = queen_html('img', True)
Input = queen_html('input')
Label = queen_html('label', True)
Li = queen_html('li',True)
Meta = queen_html('meta')
Option = queen_html('option', True)
P = queen_html('p', True)
Script = queen_html('script', True)
Select = queen_html('select', True)
Span = queen_html('span')
Strong = queen_html('strong',True)
Table = queen_html('table', True)
Td = queen_html('td', True)
Th = queen_html('th', True)
Title = queen_html('title', True)
Tr = queen_html('tr', True)
Ul = queen_html('ul',True)
Link = queen_html('link', True)
H1 = queen_html('h1', True)
H2 = queen_html('h2', True)
H3 = queen_html('h3', True)
H4 = queen_html('h4', True)
H5 = queen_html('h5', True)
H6 = queen_html('h5', True)
Legend = queen_html('legend', True)
