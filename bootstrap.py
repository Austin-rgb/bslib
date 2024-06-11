from html import *
from typing import *


def bootstrap(boot, widget=None, render=''):
    if render != '':
        boot += '-' + render

    widget.set('class', boot)
    return widget


def boot_king(target) -> Callable[[Element|None,str],Element]:
    def method(widget: Element = None, render='') -> Element:
        if not widget:
            widget = Div()
        return bootstrap(target, widget, render)

    return method


accordion = boot_king('accordion')
active = boot_king('active')
affix = boot_king('affix')
alert = boot_king('alert')
badge = boot_king('badge')
bg = boot_king('bg')
breadcrumb = boot_king('breadcrumb')
btn = boot_king('btn')
caption = boot_king('caption')
card = boot_king('card')
caret = boot_king('caret')
carousel = boot_king('carousel')
center = boot_king('center')
checkbox = boot_king('checkbox')
clearfix = boot_king('clearfix')
close = boot_king('close')
col = boot_king('col')
collapse = boot_king('collapse')
container = boot_king('container')
danger = boot_king('danger')
disabled = boot_king('disabled')
divider = boot_king('divider')
dl = boot_king('dl')
dropdown = boot_king('dropdown')
dropup = boot_king('dropup')
embed = boot_king('embed')
fade = boot_king('fade')
form = boot_king('form')
glyphicon = boot_king('glyphicon')
has = boot_king('has')
hidden = boot_king('hidden')
hide = boot_king('hide')
icon = boot_king('icon')
img = boot_king('img')
info = boot_king('info')
initialism = boot_king('initialism')
label = boot_king('label')
List = boot_king('list')
lead = boot_king('lead')
mark = boot_king('mark')
media = boot_king('media')
modal = boot_king('modal')
nav = boot_king('nav')
navbar = boot_king('navbar')
page = boot_king('page')
pagination = boot_king('pagination')
panel = boot_king('panel')
popover = boot_king('popover')
pre = boot_king('pre')
prev = boot_king('prev')
previous = boot_king('previous')
progress = boot_king('progress')
pull = boot_king('pull')
right = boot_king('right')
row = boot_king('row')
show = boot_king('show')
small = boot_king('small')
spinner = boot_king('spinner')
sr = boot_king('sr')
toast = boot_king('toast')


