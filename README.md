# GRIP Raspberry Pi 3
GRIP generated code to track the 2016 FRC tower on a Raspberry Pi using an ip camera 

##Set up the raspberry pi 

There are two options

1. Follow [this] (http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/) tutorial
  * Skip everything inside step 4 related to virtual environments
  * Change openCV version from 3.1.0 to whatever the latest version is (Currently using 3.2.0)
  * Install pynetworktables

    ```bash
    $ pip3 install pynetworktables
    ```
2. Download and flash the image on GitHub


##Generating and editing your code 

1. Write your GRIP pipeline to process the image
2. Export the code in Python
  * ```tools -> Generate Code```
3. Edit the exported code
  * Change class name to "GripPipeline"
  
    ```python
    class GripPipeline:
    ```
  
  * Add a second parameter "source0" to the process function
    
    ```python
    def process(self, source0):
    ```
    
  * Remove "self.__" from input of first step in the pipeline in process function (in this case resize)
  
    ```python
    #Step Resize_Image0:
    self.__resize_image_input = source0
    ```
    
##Modifying sample_vision.py
1. Make sure the import statement is correct for your generated pipeline
  
  ```python
  from "PIPELINE_FILE_NAME" import "CLASS_NAME"
  ```
2. Change NetworkTables IP address to that of the roboRIO
    
    ```python
    NetworkTable.setIPAddress("10.TE.AM.XX") 
    ```
3. Pick video input method
  * If using an IP camera change address of the camera 
    
    ```python
    cap = cv2.VideoCapture("http://10.TE.AM.3/mjpg/video.mjpg")
    ```
  
##References 

1. https://github.com/WPIRoboticsProjects/GRIP-code-generation/tree/master/python
2. https://github.com/Frc2481/paul-bunyan/blob/master/Camera/main.py
3. https://github.com/robotpy/pynetworktables
4. https://github.com/WPIRoboticsProjects/GRIP/wiki/Running-GRIP-on-a-Raspberry-Pi-2
