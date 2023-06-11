# Coin counter OpenCV project

## Steps 
1. Creating a video capture object.
2. Pre-processing the image.
   1. Gaussian Blur to smoothen the image
   2. Canny Edge detection to detect the edges
   3. Dilation to thicken the edges
   4. Morphological operation to close the discontinuity
3. Finding Contours.
4. Differentiating coins by size and color.
5. Counting the values of the coin and displaying it.