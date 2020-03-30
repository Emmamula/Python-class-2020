#Matplotlib requires the following dependencies:
python -m pip install -U matplotlib
#Python (>= 3.6)
#FreeType (>= 2.3)
#libpng (>= 1.2)
#NumPy (>= 1.11)
#setuptools
#cycler (>= 0.10.0)
#dateutil (>= 2.1)
#kiwisolver (>= 1.0.0)
#pyparsing

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(14)
y = np.sin(x / 2)

plt.step(x, y + 2, label='pre (default)')
plt.plot(x, y + 2, 'C0o', alpha=0.5)

plt.step(x, y + 1, where='mid', label='mid')
plt.plot(x, y + 1, 'C1o', alpha=0.5)

plt.step(x, y, where='post', label='post')
plt.plot(x, y, 'C2o', alpha=0.5)

plt.legend(title='Parameter where:')
plt.show()