# AI-Object-Search-Image-Repository

An image repository capable of processing AI search requests for targets in images using OpenCV, NumPy, and Python.

This repository is a backend program to store all images that are in a folder and display them to the user in a collage. 

Object detection and vision technology are implemented using OpenCV. The program analyzes all images for a target specified by the user. This is currently implemented through the console, it can be expanded to have a front end.

All images that happen to have the target given by the user are then displayed. The target is boxed in green for the user to see and the program outputs a percentage value to convey its confidence.

The data set used for this program is the Coco data set.

Here is a walkthrough for the application.

# Images to Add
![All Images](./screenshots/all_images.PNG?raw=true "All Images")

The above images are to be added to the repository.

# Collage to Display Repository Images
![Repository](./screenshots/repository_collage.PNG?raw=true "Repository")

The program concatenates all repository images and displays them to the user.

# AI Search Function: Target for Object Detection in Images
![AI Search Function](./screenshots/search_target.PNG?raw=true "AI Search Function")

OpenCV and the Coco data set are used to implement vision technology and object detection. After obtaining the target from the user, the program searches all images.

# Results: Display Images Containing the Target
![Results](./screenshots/results.PNG?raw=true "Results")

All images that happen to have the target given by the user are then displayed. The target is boxed in green for the user to see and the program outputs a percentage value to convey its confidence.