# Automated-Inventory-Management (AIM)
### Overview
 Automated inventory management is a system that leverages technology to streamline the process of tracking and managing inventory levels. It involves the use of various technologies such as software applications to automate inventory tracking, reordering, and supply chain management. The goal of automated inventory management is to increase efficiency, accuracy, and speed while reducing costs and errors associated with manual inventory management. Some benefits of automated inventory management include better inventory accuracy, reduced stockouts and overstocking, improved productivity, and faster order fulfillment. However, implementing automated inventory management also comes with its own set of challenges, including the initial investment in technology, staff training, and system integration with existing processes. Overall, automated inventory management can significantly improve business operations and help companies remain competitive in today's fast-paced business environment.

### Objective: The project's main goal is to develop an automated inventory management system that leverages computer vision to track and manage products within a retail or storage environment.

 *********************************************************

 ### Data collection
 Collecting data for this project presented a significant challenge, as it required a substantial amount of visual content for the model to learn effectively. In this endeavor, approximately 1,300 images were gathered, focusing on specific products.

This dataset encompasses a wide variety of images. Some of them depict the products mixed together in different arrangements, while others feature only a portion of the products. Furthermore, images were captured from various angles for each individual product.

To sum up, the data collection process involved a considerable number of images, thoughtfully chosen to facilitate effective learning and generalization by the model.

 <div align="center">
<img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/IMG_2597_jpeg.rf.e99e40e6e5307277bd28855097c744d0.jpg" width="300" height="200"> <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/IMG_2547_jpeg.rf.5ab8af8b42afb469354a928bd8c99cb2.jpg" width="300" height="200"><img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/IMG_2524_jpeg.rf.2cb2757c7994dccc8171226057075e1e.jpg" width="300" height="200"><img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/20230511_143118_012_saved-1-_jpg.rf.47467953f79f5ffcee36147e3471e181.jpg" width="300" height="200"><img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/20230511_160206_029_saved_jpg.rf.2bba018e384277e4bda28df8ccc44ecc.jpg" width="300" height="200"> <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/20230511_141637_jpg.rf.2af141d47c318a551a3db4e43d6d04ee.jpg" width="300" height="200">
 </div>

 *******************************

 ### Architecture and Design
<div align="center">
 <img src="https://i.ytimg.com/vi/Ixt7YpMRg5I/maxresdefault.jpg" width="300" height="200">
 <img src="https://www.blacksintechnology.net/wp-content/uploads/job-manager-uploads/company_logo/2021/04/roboflow_full_logo_default-2.png" width="500" height="200" >
 </div>

#### Data Collection
As mentioned earlier, a substantial dataset of images was collected. These images should encompass various aspects of the products, including different orientations and configurations.

#### Data Preprocessing with Roboflow
Roboflow is used to preprocess and prepare the collected image dataset. It provides features like resizing, augmenting, and normalizing the images to make them suitable for training deep learning models. It helps in creating a clean and organized dataset that can be used effectively.
 ##### The augmentations applied in this project are:
* Brightness: between -32% and +32%*
* Exposure: between -20% and +20%
* Blur: up to 1px
  
 #### YOLOv8 Model:
* YOLO (You Only Look Once) is a popular object detection algorithm. YOLOv8 is the latest version of this model. It's known for its real-time object detection capabilities and is widely used for various computer vision tasks.
* YOLOv8 is integrated into the project to train the model on the preprocessed image dataset. The model is trained to detect and localize specific products within the images.

 #### Training and Fine-Tuning:
The YOLOv8 model goes through a training process where it learns to recognize the target products. Training typically involves optimizing the model's parameters and weights to achieve high accuracy.

#### Deployment:
Once the model is trained, it can be deployed in the inventory management system. The deployment can be on various platforms, such as on-site servers or cloud infrastructure, depending on the project's requirements.

#### Real-time Object Detection:
The deployed model is used to perform real-time object detection on incoming images or video streams. It identifies the products and their locations within the frame.

#### Inventory Management:
The results of object detection are integrated into the inventory management system. The system keeps track of the products, their quantities, and their locations in the storage environment.

### Design Considerations:
* Scalability: The system should be designed to scale with the growth of the inventory and the number of products to be tracked.
* Accuracy and Precision: Design considerations should include strategies to improve the model's accuracy and precision in product detection.
* Real-time Performance: The system should be optimized for real-time or near-real-time performance to provide timely inventory updates.
* User Interface: A user-friendly interface may be designed to visualize inventory data, monitor the system, and manage exceptions or errors.
* Robustness: The system should be designed to handle various lighting conditions, product orientations, and potential challenges such as occlusions or overlapping products.
* Security and Privacy: If the system is used in a retail environment, security and privacy concerns should be addressed to protect sensitive data.
* Maintenance and Updates: A plan for ongoing maintenance and model updates to adapt to changing inventory and environmental conditions is essential.

This is a high-level overview of the architecture and design considerations for a project that employs Roboflow and YOLOv8 for automated inventory management. The specific implementation details and fine-tuning will depend on your project's requirements and constraints.
 *********************************************************
 
 ### Results
 <div align="center">
 <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/confusion_matrix.png" width="500" height="350">
 <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/results.png" width="500" height="350" >
 </div>
 
 ### Test samples
  <div align="center">
 <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/AIM1.jpeg" width="500" height="350">
 <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/AIM5.jpeg" width="500" height="350" >
 </div>
 
*************************************
The following video shows how the system works.

 <img src="https://github.com/salehalkhalafat/Automated-Inventory-Management/blob/main/Sample-Data/Test-Sample.gif">

 **********************************************
 ## Conclusion and Results
 In conclusion, the development this project marks a significant step towards streamlining inventory control processes. While the system shows promise in improving efficiency and accuracy, it is important to acknowledge that it is not yet a finished product. There is still much work to be done to fully realize its potential.

The system, in its current state, addresses many key aspects of inventory management, but there are areas that require further development and refinement. Future work should focus on enhancing user interface design for better usability, optimizing algorithms for more precise forecasting, and expanding its compatibility with various hardware and software platforms.

