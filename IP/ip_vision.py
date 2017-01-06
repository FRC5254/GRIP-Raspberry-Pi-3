#!/usr/bin/python3

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
import urllib
import networktables
from networktables import NetworkTable
from networktables2 import NumberArray
from ip_GRIP import GripPipeline
import datetime
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG)


def extra_processing(pipeline):
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
    print(center_x_positions)
    # Publish to the '/vision' network table
    table = NetworkTable.getTable("/vision")
    table.putValue("centerX", NumberArray.from_list(center_x_positions))
    table.putValue("centerY", NumberArray.from_list(center_y_positions))
    table.putValue("width", NumberArray.from_list(widths))
    table.putValue("height", NumberArray.from_list(heights))


    


def main():
    print('Initializing NetworkTables')
    NetworkTable.setIPAddress("10.52.55.98")
    NetworkTable.setClientMode()
    NetworkTable.initialize()


    print('Creating video capture')
    cap = cv2.VideoCapture("http://10.52.55.3/mjpg/video.mjpg")
    print("here")
   
    bytes = ''
    first = False




    print('Creating pipeline')
    pipeline = GripPipeline()

    print('Running pipeline')

    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            extra_processing(pipeline)


    print('Capture closed')


if __name__ == '__main__':
    main()
