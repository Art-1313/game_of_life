import sys
import numpy as np

sys.path.append('src/')

import field
import render

A = 49
B = 49

start = np.zeros(shape=(A, B))

start[41][21] = start[41][20] = start[41][27] = start[41][28] = 1
start[42][19] = start[42][21] = start[42][27] = start[42][29] = start[42][12] = start[42][13] = start[42][14] = start[42][15] = start[42][17] = start[42][31] = start[42][33] = start[42][34] = start[42][35] = start[42][36] = 1
start[43][22] = start[43][26] = start[43][20] = start[43][19] = start[43][28] = start[43][29] = start[43][11] = start[43][12] = start[43][13] = start[43][15] = start[43][17] = start[43][31] = start[43][33] = start[43][37] = start[43][35] = start[43][36] = 1
start[44][11] = start[44][15] = start[44][17] = start[42][15] = start[44][37] = start[44][33] = start[44][31] = 1
start[45][23] = start[45][25] = start[45][22] = start[45][26] = start[45][12] = start[45][16] = start[45][14] = start[45][15] = start[45][32] = start[45][33] = start[45][34] = start[45][36] = 1
start[46][12] = start[46][13] = start[46][36] = start[46][35] = 1
start[47][12] = start[47][13] = start[47][14] = start[47][15] = start[47][16] = start[47][32] = start[47][33] = start[47][34] = start[47][35] = start[47][36] = 1
start[48][15] = start[48][16] = start[48][33] = start[48][32] = 1

f = field.Field(start.shape, start)

r = render.Render(f, 40)

r.Play()