import sys

sys.path.append('src/')

import field
import render
import examples as ex

f = field.Field(ex.spider.shape, ex.spider)

r = render.Render(f, 2)

r.Play()