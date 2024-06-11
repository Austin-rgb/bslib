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
output = test.generate()
print(output)
```

Output 
```html
div class="carousel slide" id="8941" data-bs-ride="carousel">\n<div class="carousel-indicators">\n<button type="button" data-bs-target="#8941" data-bs-slide-to="0"></button>\n<button type="button" data-bs-target="#8941" data-bs-slide-to="1"></button>\n<button type="button" data-bs-target="#8941" data-bs-slide-to="2"></button></div>\n<div class="carousel-inner">\n<div class="carousel-item active">\n<img src="/static/image1.png" class="d-block w-100"></img></div>\n<div class="carousel-item active">\n<img src="/static/image2.png" class="d-block w-100"></img></div>\n<div class="carousel-item active">\n<img src="/static/image3.png" class="d-block w-100"></img></div></div>\n<button data-bs-target="#8941" data-bs-slide="prev" class="carousel-control-prev">\n<span class="carousel-control-prev-icon" aria-hidden="true"/>\n<span class="visually-hidden"/></button>\n<button data-bs-target="#8941" data-bs-slide="next" class="carousel-control-next">\n<span class="carousel-control-next-icon" aria-hidden="true"/>\n<span class="visually-hidden"/></button></div>
```
