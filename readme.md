## Coin counter 

<img src="https://th.bing.com/th/id/R.0526a847f3a55e47aa9e92b586144792?rik=FixiFtl12mgyag&riu=http%3a%2f%2f3.bp.blogspot.com%2f_5xkDx_-kv3I%2fTUO634r5FzI%2fAAAAAAAABWA%2fq6cbL2za3yI%2fs1600%2fcoins%2bmixed1.jpg&ehk=enFOPfeP64eI5logqggIbkND0dAr%2bgUY9pOwOp3EIbU%3d&risl=&pid=ImgRaw&r=0)" width=100% height=50%>
It's a small project using opencv and python for counting coin value and returning the total amount. <br>
The size and color of coins are the key component to differentiate between them.


## Drawbacks
➡️ Camera should be set to a certain angle for the whole time

➡️ Lighting conditions might affect in detection of coins

➡️ If coins are overlapped or in contact might change the expected result

➡️ We need to edit the code again, whenever coins sizes are getting changed (usually when releasing new coins by the authorities).

<details>
   <summary>
      
## Steps 
      
   </summary>

1. Creating video
2. Pre-processing the image.
   1. Convert to greyscale image [[1]](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)

      <img src="images/grey.png" width=50% height=50%>

   2. Gaussian Blur to smoothen the image [[2]](https://docs.opencv.org/3.4/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html)

      <img src="images/blur.png" width=50% height=50%>      

   3. Canny Edge detection to detect the edges [[3]](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)

      <img src="images/canny.png" width=50% height=50%>

   4. Dilation to thicken the edges [[4]](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
   5. Morphological operation to close the discontinuity [[5]](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)

      <img src="images/preprocess2.png" width=50% height=50%>

3. Finding Contours [[6]](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html).
4. Differentiating coins by size[[7]](https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html) and color[[8]](https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html).

      under high light condition
   
      <img src="images/all.png" width=50% height=50% >
      
      under low light condition
      
      <img src="images/all low light.png" width=50% height=50%>

      
6. Counting the values of the coin and displaying it[[9]](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html).

     <img src="images/out.png" width=50% height=50%>
  
</details >

### Note 
Thresholds in Canny, HSV values, contour area etc are tunable parmaetrs. Some `helper functions` are provided to find these values, please tune those according to the situations
