a=[1,2,3,4]
import numpy as np
a={'1':3,'2':4,'9':2}
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[0])
print(pairs)
