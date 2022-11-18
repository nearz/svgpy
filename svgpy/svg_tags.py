class SVGTag:
    def __init__(self):
        self.SVG_NS = 'http://www.w3.org/2000/svg'
        self.G_TAG = '{http://www.w3.org/2000/svg}g'
        self.RECT_TAG = '{http://www.w3.org/2000/svg}rect'
        self.CIRCLE_TAG = '{http://www.w3.org/2000/svg}circle'
        self.GROUP_TAG = '{http://www.w3.org/2000/svg}g'
        self.TSPAN_TAG = '{http://www.w3.org/2000/svg}tspan'
        self.TEXT_TAG = '{http://www.w3.org/2000/svg}text'
        self.FLOWPARA_TAG = '{http://www.w3.org/2000/svg}flowPara'
        self.IMAGE_TAG = '{http://www.w3.org/2000/svg}image'
        self.USE_TAG = '{http://www.w3.org/2000/svg}use'
        self.HREF_ATTR = '{http://www.w3.org/1999/xlink}href'

    def short_tag(self, long_tag):
        if long_tag == self.RECT_TAG:
            return 'rect'
        elif long_tag == self.CIRCLE_TAG:
            return 'circle'