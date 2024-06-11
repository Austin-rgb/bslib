from bootstrap import *


def variable(string):
    return '_'.join(string.split())


def Accordion(contents: dict):
    root = accordion()
    random_id = str(randint(1000, 10000))
    root.set('id', random_id)
    for key, value in contents.items():
        item = accordion(render='item')
        header = H3()
        header = accordion(header, 'header')
        button = Button(key)
        button.set('data-bs-toggle', 'collapse')
        button.set('data-bs-target', f'#collapse{variable(key)}')
        button.set('aria-expanded', 'true')
        button.set('aria-controls', f'collapse{variable(key)}')
        button = accordion(button, 'button')
        header.insert(button)
        collapse_ = accordion(render='collapse')
        collapse_.set('id', f'collapse{variable(key)}')
        collapse_.set('class', 'collapse show')
        body = accordion(render='body')
        body.insert(value)
        collapse_.insert(body)
        item.insert(header, collapse_)
        root.insert(item)
        
    return root

def Alert(element, render: str = 'secondary', dismissible=False):
    root = Div(element)
    root.set('class', 'alert')
    root = alert(root, render=render)
    root.set('role', 'alert')
    if dismissible:
        root = alert(root, render='dismissible')
    return root


def Card(title=H5('Card title'), body=Div(P('Some quick example text to build on the card'))):
    root = card()
    card_body = card(render='body')
    title = card(title, render='title')
    text = card(body, render='text')
    card_body.insert(title, text)
    root.insert(card_body)
    return root


def Carousel(elements: list, captions_: list):
    if captions_:
        assert len(elements) == len(captions_), 'length of captions should be equal to length of elements '

    root = carousel()
    random_id = str(randint(1000, 10000))
    root.set('id',random_id)
    root.set('data-bs-ride', 'carousel')
    root.set('class', 'slide')
    div = Div()
    indicators = carousel(div, render='indicators')
    
    for i in range(len(elements)):
        button = Button()
        button.set('type','button')
        button.set('data-bs-target', f'#{random_id}')
        button.set('data-bs-slide-to', str(i))
        indicators.insert(button)
        
    root.insert(indicators)
    inner = carousel(render='inner')
    
    for element in elements:
        item = carousel(render='item')
        item.set('class', 'active')
        element.set('class','d-block w-100')
        item.insert(element)
        inner.insert(item)
        
    root.insert(inner)
    previous_ = Button()
    previous_.set('data-bs-target',f'#{random_id}')
    previous_.set('data-bs-slide','prev')
    previous_ = carousel(previous_, render='control-prev')
    prev_label = Span('Previous', attributes={'class': 'visually-hidden'})
    prev_icon = Span(attributes={'class': 'carousel-control-prev-icon', 'aria-hidden': 'true'})
    previous_.insert(prev_icon,prev_label)
    next_ = Button()
    next_.set('data-bs-target',f'#{random_id}')
    next_.set('data-bs-slide','next')
    next_ = carousel (next_,render='control-next')
    next_icon = Span(attributes={'class': 'carousel-control-next-icon', 'aria-hidden': 'true'})
    next_label = Span('Next', attributes={'class': 'visually-hidden'})
    next_.insert(next_icon,next_label)
    root.insert(previous_,next_)
    return root


def NavBar(brand=None, contents: list[Element] = None):
    if not brand:
        brand = A('NavBar', attributes={'href': '#'})

    if not contents:
        contents = [
            A('Link 1',attributes={'href':'#'}),
            A('Link 2',attributes={'href':'#'}),
            A('Link 3',attributes={'href':'#'})
        ]
    root = navbar()
    root = navbar(root, render='expand')
    brand = navbar(brand, render='brand')
    toggle = navbar(render='toggler')
    toggle.set('data-bs-toggle', 'collapse')
    toggle.insert(navbar(Span(), render='toggler-icon'))
    collapse_ = collapse()
    collapse_ = collapse(collapse_, render='collapse')
    collect = navbar(Ul(), render='nav')
    for c in contents:
        item = nav(Li(), render='item')
        c = nav(c, render='link')
        item.insert(c)
        collect.insert(item)

    collapse_.insert(collect)
    root.insert(brand, toggle, collapse_)
    return root


def Toast(header: Element = None, body: Element = None) -> Element:
    if not header:
        header = Strong('Toast')

    root = toast()
    root.set('role', 'alert')
    root.set('aria-live', 'assertive')
    root.set('aria-atomic', 'true')
    header = toast(header, render='header')
    if not body:
        body = P('Hello world! This is a toast message')
    body = toast(body, render='body')
    root.insert(header, body)
    return root
    
def meta():
    meta1 = Meta()
    meta1.set('charset','utf-8')
    meta2 = Meta()
    meta2.set('name','viewport')
    meta2.set('content','width=device-width, initial-scale=1')
    return meta1, meta2


# Example usage

img1 = Img(attributes={'src': '/static/image1.png'})
img2 = Img(attributes={'src': '/static/image2.png'})
img3 = Img(attributes={'src': '/static/image3.png'})

captions = [
    P('First image'),
    P('Second image'),
    P('Third image')
]

test = Carousel ([img1,img2,img3],captions)

