#Handle Presentation Attributes, Inline Styles and class based styles

from base64 import b64encode
from uuid import uuid4
import re

from lxml import etree

from .element_factory import ElementFactory
from .svg_tags import SVGTag

class SVGFile(object):
    @classmethod
    def load(cls, src=None, file=None):
        if not (src == None) ^ (file == None):
            raise RuntimeError('Must specify exactly one of src or file argument')
        if src:
            return cls(standardize(src=src))
        return cls(standardize(file=file))

    @classmethod
    def new_svg_file(cls, width, height):
        src = '<?xml version="1.0" standalone="no"?> <svg version="1.1" id="' + str(uuid4()) + '" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="' + width + 'px" height="' + height + 'px" viewBox="0 0 ' + width + ' ' + height + '" enable-background="new 0 0 ' + width + ' ' + height + '" xml:space="preserve"></svg>'
        
        return cls(etree.fromstring(src))

    def __init__(self, doc):
        self._doc = doc
        self._efactory = ElementFactory()
        
    def get_root(self):
        return self._doc.getroot()

    def get_element_by_id(self, id):
        return self._efactory.factory(self._get_by_id(id))
    
    def get_elements_by_tag(self, tag):
        final = []
        elems = self._doc.findall('//svg:'+ SVGTag.short_tag(tag), namespaces={'svg': SVGTag.SVG_NS})
        for elem in elems:
            final.append(self._efactory.factory((elem)))
        return final

    def add_element(self, type, parent_id):
        parent = self._get_by_id(parent_id)
        elem = etree.SubElement(parent, type)
        return self._efactory.factory(elem)

    def rect_place_image(self, rect, mimetype=None, src=None, file=None):
        pass

    def place_svg(self, svg, box):
        pass

    def save_svg_file(self, filename):
        f = open(filename, "w")
        f.write(self.__str__())
        f.close()


#Private Functions
    def _get_by_id(self, id):
        elem = self._doc.xpath('//*[@id="' + id + '"]')
        return elem[0]

    def __str__(self):
        return etree.tostring(self._doc, encoding='utf8', method='xml').decode('utf8')
        


#Utils
def style_type(doc):
    pass

def standardize(src=None, file=None):
    if src:
        tree = etree.fromstring(src)
    if file:
        tree = etree.parse(file)

    defs = tree.xpath('/svg:svg/svg:defs', namespaces={'svg': SVGTag().SVG_NS})
    if not defs:
        tree.getroot().insert(0, etree.Element('{%s}defs' % SVGTag().SVG_NS))
    svgelem = tree.getroot()
    stdize = ['x', 'y', 'width', 'height']

    for att in stdize:
        chng = svgelem.get(att)
        x = re.sub('x', 't', chng)
        svgelem.set(att, x)
    
    return tree