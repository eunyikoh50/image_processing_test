import numpy as np
import matplotlib.pyplot as plt

import httplib2
import io
http = httplib2.Http('.cache')
resp, content = http.request('https://homepages.cae.wisc.edu/~ece533/images/baboon.png', 'GET')
resp, content = http.request('https://homepages.cae.wisc.edu/~ece533/images/monarch.png', 'GET')
if resp['content-type'] == 'image/png':
  stream = io.BytesIO(content)
  img = plt.imread(stream)
else:
  print('Result is not a PNG image: got', resp['content-type'])
  print(resp)
  print(content)
  
plt.imshow(img, vmin=0, vmax=1)
plt.plot()
