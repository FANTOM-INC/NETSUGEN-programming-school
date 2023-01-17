import cv2
import numpy

image = cv2.imread("sample_file/apple.jpeg")
template = cv2.imread("sample_file/part.jpg")

result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)

threshold = 0.99
loc = numpy.where(result >= threshold)

th, tw = template.shape[:2]

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + tw, pt[1] + th), 0, 2)

cv2.imwrite("reuslt.png", image)
