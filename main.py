from svgpy import SVGFile
from svgpy.svg_tags import SVGTag

temp = SVGFile.load(file='./svg_examples/SVGTemplate.svg')

txt = temp.get_element_by_id('AE.Test')

txt.set_text('Changed')

# rects = temp.get_elements_by_tag(RECT_TAG)

# for r in rects:
#     r.remove()

# temp = SVGFile.new_svg_file('1000', '1000')

# g = temp.add_element(svg_tags.G_TAG, temp.get_base().get('id'))
# g.set_id('DYNO')

# cir = temp.add_element(svg_tags.CIRCLE_TAG, g.get_id())
# cir.set_id(str('mycircle'))
# cir.set_cx_or_cy(cx='100', cy='100')
# cir.set_radius('50')
# cir.set_fill_color('#4287f5')


temp.save_svg_file('./svg_examples/colorchange.svg')

# print(SVGTag().short_tag(SVGTag().RECT_TAG))