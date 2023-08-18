import cv2
import numpy as np

def otsu_binarization(image_path, output_path):
    # 读取本地彩色图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 应用Otsu阈值法将图像转换为二值图像
    ret, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 保存二值图像
    cv2.imwrite(output_path, bin_img)
    print(f'Binarized image saved to {output_path}')

    # 显示二值图像
    cv2.imshow('Binarized Image', bin_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数
image_path = '/mnt/a/OneDrive/MScRobotics/Dissertation2022/thesis/v0.2/figures/map(color).png'  # 替换为你的图片路径
output_path = image_path  # 替换为你希望保存的图片路径
otsu_binarization(image_path, output_path)
