import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('img_4.png')

# Преобразование в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение адаптивного порогового значения
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Уменьшение шума с помощью медианного фильтра
binary_image = cv2.medianBlur(binary_image, 5)

# Применение морфологической операции расширения
kernel = np.ones((5, 5), np.uint8)
binary_image = cv2.dilate(binary_image, kernel, iterations=1)

# Нахождение контуров
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Фильтрация контуров по размеру
min_contour_area = 1000  # Минимальная площадь для учета контура
large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Создание маски для отображения только больших черно-серых областей
mask = np.zeros_like(gray_image)
cv2.drawContours(mask, large_contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Применение маски к исходному изображению
result_image = cv2.bitwise_and(image, image, mask=mask)

# Отображение результата
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
