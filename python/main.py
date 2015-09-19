import cv2 as cv
import numpy as np
import argparse
import time
import scipy as sp
import scipy.ndimage

from sensor import Sensor

def normalize(a, min, max):
    if(max == min):
        max = 0.5;
        min = 0.0;
    return float(a - min)/float(max - min)

def main():
    global sensor
    sensor = Sensor()
    try:
        sensor.connect()
    except:
        print("Error connecting to sensor")
        raise
        return

    cv.namedWindow("ImageWindow", cv.WINDOW_AUTOSIZE);
    nfunc = np.vectorize(normalize)
    images = get_next_image()
    baseline_frame = images[-1]
    baseline = baseline_frame['image']
    width = baseline_frame['cols']
    height = baseline_frame['rows']
    while 1:
        images = get_next_image();
        frame = images[-1]
        pixels = np.array(frame['image'])
        pixels_zeroed = np.subtract(baseline, pixels);
        min = np.amin(pixels_zeroed)
        max = np.amax(pixels_zeroed)
        pixels_normalized = nfunc(pixels_zeroed, min, max)
        large = sp.ndimage.zoom(pixels_normalized, 10, order=1)
        detector = cv.SimpleBlobDetector()
        keypoints = detector.detect(large)
        im_with_keypoints = cv.drawKeypoints(large, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv.imshow("ImageWindow",im_with_keypoints);
        cv.waitKey(1)

    sensor.close()
    print "Done. Everything cleaned up."

def get_next_image():
    images = sensor.getAllImages()
    while(len(images) == 0):
        images = sensor.getAllImages()
        time.sleep(0.2)
    return images

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Big Ass Touch Portal')
    print "Starting..."
    main()
