import cv2
import glob
import numpy as np 

thres = 0.5 # Threshold to detect objects

img = cv2.imread('lena.PNG')
images = [cv2.imread(file) for file in glob.glob("repository/*.png")]

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# concatanate image horizontally 
fullRepository = np.concatenate(images, axis=1)
cv2.imshow('Full Repository', fullRepository)
cv2.waitKey(0)

target_to_search = input("Please enter an object/target to find: \n")
print("Thank you. Searching for target: " + target_to_search)

noMatchingImages = True

for i in range(len(images)):
    classIds, confs, bbox = net.detect(images[i], confThreshold=thres)
    print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(images[i],box,color=(0,255,0),thickness=2)
            cv2.putText(images[i],classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(images[i],str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            if classNames[classId-1] == target_to_search:
                noMatchingImages = False
                print("index " + str(i) + " in the repository matches the target")
                cv2.imshow(str(i), images[i])
                cv2.waitKey(0)

if noMatchingImages:
    print("Sorry, no matching images to target")
