# SimGAN
Based on the discussion with Josh yesterday I have adapted the current model to account for identity (shape), pose and color.
This is leaves lighting, which is now exaplained by the noise vector.

## First 5 principal components of the shape (for fixed pose and color)
![](traversals/traversal_face_01.gif)
![](traversals/traversal_face_1.gif)
![](traversals/traversal_face_2.gif)
![](traversals/traversal_face_3.gif)
![](traversals/traversal_face_4.gif)

## Pose Variations (for fixed shape and color)
![](traversals/traversal_face_5.gif)
![](traversals/traversal_face_6.gif)
![](traversals/traversal_face_7.gif)
![](traversals/traversal_face_8.gif)
![](traversals/traversal_face_9.gif)

## Color Variation (For the first principal direction for both fixed and varying shape and poses to clearly show that we can control all these factors independently and are not merely taking averages.)
![](traversals/traversal_face_random_color.gif) (Fixed shape and pose)
![](traversals/color_small.gif) (Fixed (but different) shape and (but different) pose)
![](traversals/color_pose.gif) (Fixed (but different) shape and (but different) pose)
![](traversals/color_shape.gif) (Fixed pose but changing shape)
![](traversals/color_left.gif) 

![](traversals/color_pose1.gif)

