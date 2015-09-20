import cv2 as cv
import numpy as np
import argparse
import time
import scipy as sp
import scipy.ndimage
import requests
import json

from sensor import Sensor

root_url = "http://localhost:3000"

def normalize(a, min, max):
    if(max == min):
        max = 0.5;
        min = 0.0;
    return int((float(a - min)/float(max - min)) * 255.0)

def main():
    global sensor
    sensor = Sensor()
    try:
        sensor.connect()
    except:
        print("Error connecting to sensor")
        raise
        return

    #cv.namedWindow("Threshold", cv.WINDOW_AUTOSIZE);
    cv.namedWindow("Contours", cv.WINDOW_AUTOSIZE);
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
        large = large.astype(np.uint8);
        large = cv.medianBlur(large,7)
        #large = cv.GaussianBlur(large,(7,7),0)
        #stuff, blobs = cv.threshold(large,150,255,cv.THRESH_BINARY)
        stuff, blobs = cv.threshold(large,160,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        contours, hierarchy = cv.findContours(blobs, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        out = np.zeros((height*10,width*10,3), np.uint8)
        cv.drawContours(out,contours,-1,(255,255,0),3)

        regions_found = len(contours)

        contours = np.vstack(contours).squeeze()
        rect = cv.minAreaRect(contours)
        box = cv.cv.BoxPoints(rect)
        box = np.int0(box)
        cv.drawContours(out,[box],0,(0,255,255),2)

        #cv.imshow("Threshold", blobs);
        cv.imshow("Contours", out)
        cv.waitKey(1)

        x = rect[0][0]
        y = rect[0][1]
        angle = rect[2];

        if(regions_found < 10):
            send(x, y, angle)

        time.sleep(0.4)

    sensor.close()
    print "Done. Everything cleaned up."

def send(x, y, theta):
    root_url = "http://screen20.meteor.com"#"http://localhost:3000"
    payload = {'x': x, 'y': y, 'theta': theta}
    r = requests.post(root_url+"/data/", data=payload)
    if r.json()['code'] == 200:
    	print "Sent."
    else:
    	print r.json()

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
