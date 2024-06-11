from random import randint

class Element:
    def __init__(self, *elements, attributes=None, symbol='div'):
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
        self.symbol = symbol

    def _update_hierarchy_level(self, level):
        if self._updating_hierarchy:
            raise Exception('Circular hierarchy detected')
        self._hierarchy_level += level
        self._updating_hierarchy = True
        for elem in self.elements:
            elem._update_hierarchy_level(level + 1)

        self._updating_hierarchy = False


    def insert(self, *args):
        """
        Insert html element into the tree of this element 
        """
        new = list(args)
        for n in new:
            n._update_hierarchy_level(self._hierarchy_level + 1)
            
        self.elements.extend(new)
        self._changed = True

    def set(self, name: str, value: str):
        """
        Set value of an attribute in this html element 
        """
        self.history.append(f'setting {self}: {name}="{value}"')
        if name == 'class' and 'class' in self.attributes.keys():
            if value in self.attributes[name]:
                return
            self.attributes[name] = self.attributes[name] + ' ' + value
            self._changed = True
        else:
            self.attributes[name] = value

    def _generate_attributes(self):
        """
        Generate the string for setting the attributes of this element in html
        """
        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def generate(self):
        """
        Generate the html of this element 
        """
        if not self._changed:
            return self._html
            
        html = '<'
        html += self.symbol
        html += ' ' + self._generate_attributes()
        
        html += '/>'
            
        self._changed = False 
        if self.symbol == 'html':
            html = '<!doctype html >' + html
        self._html = html
        return html
        
    def save_html(self,filename):
        """
        Save the html code of this element to a file
        """
        new_file = open(filename,'x+')
        new_file.write(self.generate())
        
    def __repr__(self):
        return self.symbol + f' object id={self._id}: '

class Container(Element):
    def __init__(self, *elements, attributes=None, symbol='div'):
        super().__init__(*elements, attributes=attributes,symbol=symbol)
    def generate(self):
        """
        Generate the html of this element 
        """
        if not self._changed:
            return self._html
            
        html = '<'
        html += self.symbol
        html += ' ' + self._generate_attributes()
        
        html += '>' + self.inner_html
        for elem in self.elements:
            html += '\n'

            html += elem.generate()

        html += '</' + self.symbol + '>'

            
        self._changed = False 
        if self.symbol == 'html':
            html = '<!doctype html >' + html
        self._html = html
        return html



class A(Container):
    def __init__(self, *elements, attributes=None, symbol='a'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Body(Container):
    def __init__(self, *elements, attributes=None, symbol='body'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Div(Container):
    def __init__(self, *elements, **kwargs):
        super().__init__(*elements, **kwargs)

class Button(Container):
    def __init__(self, *elements, attributes=None, symbol='button'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class B(Element):
    def __init__(self, *elements, attributes=None, symbol='b'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Fieldset(Container):
    def __init__(self, *elements, attributes=None, symbol='fieldset'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Form(Container):
    def __init__(self, *elements, attributes=None, symbol='form'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Head(Container):
    def __init__(self, *elements, attributes=None, symbol='head'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Html(Container):
    def __init__(self, *elements, attributes=None, symbol='html'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Img(Container):
    def __init__(self, *elements, attributes=None, symbol='img'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Input(Element):
    def __init__(self, *elements, attributes=None, symbol='input'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Label(Container):
    def __init__(self, *elements, attributes=None, symbol='label'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Li(Container):
    def __init__(self, *elements, attributes=None, symbol='li'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Meta(Container):
    def __init__(self, *elements, attributes=None, symbol='meta'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Option(Container):
    def __init__(self, *elements, attributes=None, symbol='option'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class P(Container):
    def __init__(self, *elements, attributes=None, symbol='p'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Script(Container):
    def __init__(self, *elements, attributes=None, symbol='script'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Select(Container):
    def __init__(self, *elements, attributes=None, symbol='select'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Span(Container):
    def __init__(self, *elements, attributes=None, symbol='span'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Strong(Container):
    def __init__(self, *elements, attributes=None, symbol='strong'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Table(Container):
    def __init__(self, *elements, attributes=None, symbol='table'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Td(Container):
    def __init__(self, *elements, attributes=None, symbol='td'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Th(Container):
    def __init__(self, *elements, attributes=None, symbol='th'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Title(Container):
    def __init__(self, *elements, attributes=None, symbol='title'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Tr(Container):
    def __init__(self, *elements, attributes=None, symbol='tr'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Ul(Container):
    def __init__(self, *elements, attributes=None, symbol='ul'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Link(Container):
    def __init__(self, *elements, attributes=None, symbol='link'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H1(Container):
    def __init__(self, *elements, attributes=None, symbol='h1'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H2(Container):
    def __init__(self, *elements, attributes=None, symbol='h2'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H3(Container):
    def __init__(self, *elements, attributes=None, symbol='h3'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H4(Container):
    def __init__(self, *elements, attributes=None, symbol='h4'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H5(Container):
    def __init__(self, *elements, attributes=None, symbol='h5'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class H6(Container):
    def __init__(self, *elements, attributes=None, symbol='h6'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)

class Legend(Container):
    def __init__(self, *elements, attributes=None, symbol='legend'):
        super().__init__(*elements, attributes=attributes, symbol=symbol)