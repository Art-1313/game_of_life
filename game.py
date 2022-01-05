import sys
import numpy as np

sys.path.append('src/')

import field
import render

A = 10
B = 15

start = np.zeros(shape=(A, B))

start[0][1] = start[1][2] = start[2][0] = start[2][1] =  start[2][2] = 1

f = field.Field(start.shape, start)

r = render.Render(f, 2000)

r.Play()