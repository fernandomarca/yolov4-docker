#!/bin/bash

if [ ! -d "darknet" ]; then
git clone https://github.com/AlexeyAB/darknet 
fi
cd darknet || exit
##remove comments for use GPU
#sed -i 's/GPU=.*/GPU=1/' Makefile 
#sed -i 's/CUDNN=.*/CUDNN=1/' Makefile
#sed -i 's/OPENCV=.*/OPENCV=1/' Makefile
make

cd ..

if [ ! -f "weights/yolov4.weights" ]; then  
  # wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights /home/weights
  # https://drive.google.com/file/d/1-Kp87F9EQ1hqiFCwh2Y6lMho5XIA5vIO/view?usp=sharing
  gdown --id 1-Kp87F9EQ1hqiFCwh2Y6lMho5XIA5vIO -O weights/yolov4.weights
fi

tail -f /dev/null