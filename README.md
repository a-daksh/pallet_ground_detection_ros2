# **Pallet and Ground Detection-Segmentation in ROS2**

## **Objective**
This project implements a **pallet and ground detection-segmentation application** in ROS2, designed for manufacturing or warehousing environments. 

## **Prerequisites**
Before running this project, ensure you have the following installed:
1. **ROS2 Humble** (on Ubuntu 22.04).
2. Python libraries:
```pip install ultralytics opencv-python numpy torch torchvision cv_bridge matplotlib```

---

## **Installation Instructions**

### **Step 1: Clone the Repository**
Create a ROS2 workspace and clone this repository:
```
mkdir -p ~/ros2_ws/
cd ~/ros2_ws/
git clone git@github.com:a-daksh/pallet_ground_detection_ros2.git
```

### **Step 2: Download Required Files**
Download the required files from [Drive link](https://drive.google.com/drive/folders/1_GLXqJJsnF-4wum1YWaBZejN_cHSzImh?usp=sharing)

- `db3_files` folder (containing `camera_data.db3`).
- `best.pt` (trained YOLO model weights).

Place them in the following locations:
- `db3_files/` folder should be placed inside `ros2_ws/`.
- `best.pt` should be placed in `ros2_ws/src/yolo_inference/yolo_inference/` (next to `yolo_node.py`).

### **Step 3: Build the Workspace**
Build the ROS2 workspace:
```
cd ~/ros2_ws
colcon build --packages-select yolo_inference
source install/setup.bash
```
---

## **Usage Instructions**

### **Step 1: Run the YOLO Inference Node**
On the first terminal, run the YOLO inference node:
```
cd ~/ros2_ws
ros2 run yolo_inference yolo_node
```
### **Step 2: Replay Camera Data**
On the second terminal, replay the `.db3` bag file to simulate camera data:
```
ros2 bag play ~/ros2_ws/db3_files/camera_data.db3 --loop
```

### **Step 3: Visualize Outputs**
On the third terminal, visualize raw and annotated images using `rqt_image_view`:
```
ros2 run rqt_image_view rqt_image_view
```
