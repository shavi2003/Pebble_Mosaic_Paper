# importing packages we need
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt

# by means of "hard coding" skipping parsing because working in an environment
# making a dictionary so it is possible to call args by using keys
arguments = {
	"image": "Lenna.png"
}

# alternative variant using parsing for the command line usage:
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#arguments = vars(ap.parse_args())   


# loading image to a file and then converting image to a floating point number
img = img_as_float(io.imread(arguments["image"]))

# looping over number of segments and using slic function to get segments
for num_of_segments in (100, 200, 500, 1000):
	segments = slic(img, n_segments = num_of_segments, sigma = 5)
# plotting the figure with subplots and returning the image with boundaries 
	fig = plt.figure("Superpixels -- %d segments" % (num_of_segments))
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(mark_boundaries(img, segments))
	plt.axis("off")

# showing plots off
plt.show()
