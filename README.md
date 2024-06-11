### Usage
```python
from html import Img, P
from bslib import Carousel 
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
```
