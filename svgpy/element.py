import re

PA = 'pres_atts'
SA = 'style_atts'

class Element:
    def __init__(self, elem):
        self._elem = elem
        self._style_type = style_type(elem)

    def set_id(self, id):
        self._elem.set('id', id)
    
    def get_id(self):
        return self._elem.get('id')
    
    def remove(self):
        return self._elem.getparent().remove(self._elem)

class G(Element):
    def __init__(self, elem):
        super().__init__(elem)


class SVG(Element):
    def __init__(self, elem):
        super().__init__(elem)

class Text(Element):
    def __init__(self, elem):
        super().__init__(elem)
    
    def set_x_or_y(self, x=None, y=None):
        if x:
            self._elem.set('x', x)
        if y:
            self._elem.set('y', y)

    def set_text(self, value):
        self._elem.text = value

class SVGShape(Element):
    def __init__(self, elem):
        super().__init__(elem)

    def set_fill_color(self, hex):
        if self._style_type == PA:
            self._elem.set('fill', hex)
        else:
            style = self._elem.get('style')
            regx = re.sub("(fill:#?)[a-fA-f0-9]{6}", hex, style)
            self._elem.set('style', regx)
    
    def set_stroke_color(self, hex):
        if self._style_type == PA:
            self._elem.set('stroke', hex)
        else:
            style = self.elem.get('style')
            regx = re.sub("(stroke:#?)[a-fA-f0-9]{6}", hex, style)
            self._elem.set('style', regx)
    
    def set_stroke_width(self, points):
        if self._style_type == PA:
            self._elem.set('stroke-width', points)
        else:
            style = self._elem.get('style')
            regx = re.sub("(stroke-width:?)[0-9]+", points, style)
            self._elem.set('style', regx)

class Rect(SVGShape):
    def __init__(self, elem):
        super().__init__(elem)
  
    def set_x_or_y(self, x=None, y=None):
        if x:
            self._elem.set('x', x)
        if y:
            self._elem.set('y', y)

    def set_width_or_height(self, width=None, height=None):
        if width:
            self._elem.set('width', width)
        if height:
            self._elem.set('height', height)
    
    def get_x(self):
        return self._elem.get('x')
    
    def get_y(self):
        return self._elem.get('y')


class Circle(SVGShape):
    def __init__(self, elem):
        super().__init__(elem)

    def set_cx_or_cy(self, cx=None, cy=None):
        if cx:
            self._elem.set('cx', cx)
        if cy:
            self._elem.set('cy', cy)

    def set_radius(self, r):
        self._elem.set('r', r)


def style_type(elem):
    style = elem.get('style')
    if style == None:
        return PA
    return SA

class Image(Rect):
    def __init__(self, elem):
        super().__init__(elem)
    
    def set_href(self, file_path):
        self._elem.set('href', file_path)

    def set_aspect_ratio(self, value):
        self._elem.set('preserveAspectRatio', value)