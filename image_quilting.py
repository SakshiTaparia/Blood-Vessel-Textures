import matplotlib

from matplotlib import pyplot as plt

import numpy as np

def texture_rand(texture, block_size):

    h, w = texture.shape
    
    y_max = h - block_size
    x_max = w - block_size

# desired size of new image is twice original one

    dimension = max(h, w)

    new_h = new_w = dimension*2

# assume complete division

    blocks_1D = new_h // block_size

    output = np.zeros((new_h, new_w), dtype=texture.dtype)

# Choose random blocks and fill the output image

    for x in range(blocks_1D):
      
      for y in range(blocks_1D):

        x1 = x * block_size
        y1 = y * block_size

        x2 = x1 + block_size
        y2 = y1 + block_size

        x_rand = np.random.randint(0, x_max)
        y_rand = np.random.randint(0, y_max)

        block = texture[x_rand:x_rand+block_size , y_rand:y_rand+block_size]
        output[x1:x2, y1:y2] = block
  
    return output

def texture_neighbourhood(texture, block_size, overlap):

  patch_size = block_size + 2*overlap
  h, w = texture.shape

  y_max = h - patch_size
  x_max = w - patch_size

  dimension = max(h, w)
  new_h = new_w = dimension*2

  blocks_1D = new_h // block_size
  output = np.zeros((new_h, new_w), dtype=texture.dtype)

  for x in range(blocks_1D):
    for y in range(blocks_1D):

      if (x == 0 and y == 0):

        x_rand = np.random.randint(0, x_max)
        y_rand = np.random.randint(0, y_max)

        output[0:block_size, 0:block_size] = texture[x_rand:x_rand+block_size , y_rand:y_rand+block_size]

      elif (x == 0):

        min_x = 0
        min_y = 0

        min_error = sys.maxsize

        for temp_x in range (0,x_max):
          
          for temp_y in range (0,y_max):

            patch = texture[temp_x:temp_x+block_size, temp_y:temp_y+patch_size]

            left = output[0:block_size, y*block_size-overlap : y*block_size]
            right = patch[0:block_size, temp_y: temp_y + patch_size]

            error = np.power((left - right),2)
            error = np.sum(error)

            if(error < min_error):
              min_x = temp_x
              min_y = temp_y

        block = texture[min_x:min_x+block_size, min_y:min_y+block_size]

        output[x*block_size : x*block_size + block_size, y*block_size : y*block_size + block_size] = block

      elif (y == 0):

        min_x = 0
        min_y = 0

        min_error = sys.maxsize

        for temp_x in range (0,x_max):
          
          for temp_y in range (0,y_max):

            patch = texture[temp_x:temp_x+patch_size, temp_y:temp_y+block_size]

            top = output[x*block_size-overlap : x*block_size, 0:block_size]
            bottom = patch[temp_y: temp_y + patch_size, 0:block_size]

            error = np.power((top - bottom),2)
            error = np.sum(error)

            if(error < min_error):
              min_x = temp_x
              min_y = temp_y

        block = texture[min_x:min_x+block_size, min_y:min_y+block_size]

        output[x*block_size : x*block_size + block_size, y*block_size : y*block_size + block_size] = block

      else:

        min_x = 0
        min_y = 0

        min_error = sys.maxsize

        for temp_x in range (0,x_max):
          
          for temp_y in range (0,y_max):

            patch = texture[temp_x:temp_x+patch_size, temp_y:temp_y+patch_size]

            left = output[temp_x+overlap:temp_x+block_size+overlap, y*block_size-overlap : y*block_size]
            right = patch[temp_x+overlap:temp_x+block_size+overlap, temp_y: temp_y + patch_size]

            top = output[x*block_size-overlap : x*block_size, temp_y+overlap:temp_y+block_size+overlap]
            bottom = patch[temp_y: temp_y + patch_size, temp_y+overlap:temp_y+block_size+overlap]

            error_1 = np.power((left - right),2)
            error_2 = np.power((top - bottom),2)

            error = np.sum(error_1) + np.sum(error_2)

            if(error < min_error):
              min_x = temp_x
              min_y = temp_y

        block = texture[min_x:min_x+block_size, min_y:min_y+block_size]

        output[x*block_size : x*block_size + block_size, y*block_size : y*block_size + block_size] = block

    return output


image = plt.imread('D1.gif')
image.shape

plt.title('Input texture')
plt.imshow(image)
plt.show()

block_size = 50

overlap = int(block_size // 6)

fig2a = texture_rand(image, block_size)

plt.title('Random texture')
plt.imshow(fig2a)
plt.show()

fig2b = texture_neighbourhood(image, block_size, overlap)

plt.title('Minimized L2 error')
plt.imshow(fig2b)
plt.show()