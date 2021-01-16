# AI-Object-Search-Image-Repository

An image repository capable of processing AI search requests for targets in images using OpenCV, NumPy, and Python.

This repository is a backend program to store all images that are in a folder and display them to the user in a collage. 

Object detection and vision technology are implemented using OpenCV. The program analyzes all images for a target specified by the user. This is currently implemented through the console, it can be expanded to have a front end.

All images that happen to have the target given by the user are then displayed. The target is boxed in green for the user to see and the program outputs a percentage value to convey its confidence.

The data set used for this program is the Coco dataset.

Here is a walkthrough for the application.

# Images to Add
![All Images](./screenshots/all_images.PNG?raw=true "All Images")

The above images are to be added to the repository. For demonstration purposes, I have selected 4 images that are saved as png files.

# Collage to Display Repository Images
![Repository](./screenshots/repository_collage.PNG?raw=true "Repository")

The program concatenates all repository images and displays them to the user. This serves the purpose of making that initial collage whee the user is able to see all their images.

# AI Search Function: Target for Object Detection in Images
![AI Search Function](./screenshots/search_target.PNG?raw=true "AI Search Function")

OpenCV and the Coco dataset are used to implement vision technology and object detection. After obtaining the target from the user, the program searches all images.

For example, I entered "dog" as the target after I was prompted by the console. Using this target, the program can perform its search. It goes through each image in the repository to check if the given target is detected.

# Results: Display Images Containing the Target
![Results](./screenshots/results.PNG?raw=true "Results")

All images that happen to have the target given by the user are displayed. The target is boxed in green for the user to see and the program outputs a percentage value to convey its confidence.

From the example above, we can see that two images contain dogs (given target was "dog"). This tool is especially useful when scanning many images and makes the process a lot faster than searching for targets/objects yourself when looking at a large dataset/repository. I also added the index of the image in the repository in case the user would like to directly access the image and carry out any actions.