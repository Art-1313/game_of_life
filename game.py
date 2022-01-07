import sys

sys.path.append('src/')

import field
import render
import examples as ex

f = field.Field(ex.glider_gen.shape, ex.glider_gen)

r = render.Render(f, 25)

r.Play()