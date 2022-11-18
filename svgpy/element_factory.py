#Current support for Presentation Atts. or Style Att on Elem only.
from .svg_tags import SVGTag
from .element import *
class ElementFactory:

    def __init__(self):
        self.svg_tag = SVGTag()

    def factory(self, elem):
        if elem.tag == self.svg_tag.RECT_TAG:
            return Rect(elem)
        elif elem.tag == self.svg_tag.CIRCLE_TAG:
            return Circle(elem)
        elif elem.tag == self.svg_tag.G_TAG:
            return G(elem)
        elif elem.tag == self.svg_tag.TEXT_TAG:
            return Text(elem)
        elif elem.tag == self.svg_tag.IMAGE_TAG:
            return Image(elem)
