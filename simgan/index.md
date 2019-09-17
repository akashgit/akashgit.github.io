# SimGAN

Based on Josh's email here is a first attempt on transfer (without any tuning or adaptation)

## Faces to CelebA
![](traversals/swim/traversal_face.gif)
![](traversals/swim/traversal_face_1.gif)
![](traversals/swim/traversal_face_2.gif)


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
![](traversals/traversal_face_10.gif)
![](traversals/traversal_face_7.gif)
![](traversals/traversal_face_8.gif)
![](traversals/traversal_face_9.gif)

## Color Variation (For the first principal direction of color) 
#### Varying color for fixed shape and pose
![](traversals/traversal_face_random_color.gif) 
![](traversals/color_small.gif) 
![](traversals/color_left.gif)
### Varying pose and color together
![](traversals/color_pose.gif) 
### Varying shape and color together 
![](traversals/color_shape.gif) 

# SWIM
![](traversals/swim/pred_only_1.gif)
![](traversals/swim/pred_only_3.gif)
![](traversals/swim/pred_only_16.gif)
![](traversals/swim/pred_only_27.gif)

