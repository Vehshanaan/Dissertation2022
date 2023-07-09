import cv2



map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_0_256.png"

img = cv2.imread(map_path,0)

img = cv2.resize(img,(50,51))



_,binary = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(binary[10,0])
cv2.imshow(")",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


