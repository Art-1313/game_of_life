import numpy as np

glider = np.zeros(shape=(10, 15))

glider[0][1] = glider[1][2] = glider[2][0] = glider[2][1] = glider[2][2] = 1

spider = np.zeros(shape=(49, 49))

spider[41][21] = spider[41][20] = spider[41][27] = spider[41][28] = 1
spider[42][19] = spider[42][21] = spider[42][27] = spider[42][29] = spider[42][12] = spider[42][13] = spider[42][14] = spider[42][15] = spider[42][17] = spider[42][31] = spider[42][33] = spider[42][34] = spider[42][35] = spider[42][36] = 1
spider[43][22] = spider[43][26] = spider[43][20] = spider[43][19] = spider[43][28] = spider[43][29] = spider[43][11] = spider[43][12] = spider[43][13] = spider[43][15] = spider[43][17] = spider[43][31] = spider[43][33] = spider[43][37] = spider[43][35] = spider[43][36] = 1
spider[44][11] = spider[44][15] = spider[44][17] = spider[42][15] = spider[44][37] = spider[44][33] = spider[44][31] = 1
spider[45][23] = spider[45][25] = spider[45][22] = spider[45][26] = spider[45][12] = spider[45][16] = spider[45][14] = spider[45][15] = spider[45][32] = spider[45][33] = spider[45][34] = spider[45][36] = 1
spider[46][12] = spider[46][13] = spider[46][36] = spider[46][35] = 1
spider[47][12] = spider[47][13] = spider[47][14] = spider[47][15] = spider[47][16] = spider[47][32] = spider[47][33] = spider[47][34] = spider[47][35] = spider[47][36] = 1
spider[48][15] = spider[48][16] = spider[48][33] = spider[48][32] = 1