import cv2
import numpy as np

# Загрузка изображений
image1 = cv2.imread('img_1.png')
image2 = cv2.imread('img_2.png')
image3 = cv2.imread('img_3.png')

max_height = max(image1.shape[0], image2.shape[0], image3.shape[0])
max_width = max(image1.shape[1], image2.shape[1], image3.shape[1])

image1_resized = cv2.resize(image1, (max_width, max_height))
image2_resized = cv2.resize(image2, (max_width, max_height))
image3_resized = cv2.resize(image3, (max_width, max_height))

# Создание пустого холста
canvas = np.zeros((max_height, max_width * 3, 3), dtype=np.uint8)

# Вставка изображений на холст
canvas[:, :max_width, :] = image1_resized
canvas[:, max_width:max_width*2, :] = image2_resized
canvas[:, max_width*2:max_width*3, :] = image3_resized

# Отображение результата
cv2.imshow('Result', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()