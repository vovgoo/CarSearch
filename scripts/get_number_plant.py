import cv2
import matplotlib.pyplot as plt
import easyocr

def open_image(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    
    return carplate_img

def carplate_extract(image, car_cascade):
    carplate_rects = car_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in carplate_rects:
        carplate_img = image[y+15:y+h-10, x+15:x+w-20]

    return carplate_img

def enlarge_image(image, scale_persent):
    width = int(image.shape[1] * scale_persent / 100)
    height = int(image.shape[0] * scale_persent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return resized_image

def search_carplate(image):
    carplate_img_rgb = open_image(img_path=image)
    carplate_hear_cascade = cv2.CascadeClassifier("neural_network/haarcascade.xml")
    carplate_extract_image = carplate_extract(carplate_img_rgb, carplate_hear_cascade)
    carplate_extract_image = enlarge_image(carplate_extract_image, 150)
    carplate_extract_image_gray = cv2.cvtColor(carplate_extract_image, cv2.COLOR_RGB2BGRA)
    thresh = cv2.threshold(carplate_extract_image_gray, 127, 255, cv2.THRESH_BINARY)[1]

    #plt.imshow(thresh)
    #plt.show()
    
    return thresh

def search_text(thresh):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(thresh, allowlist="ABEKMHOPCTYX0123456789", detail=0)
    return result


def get_number_carplate(image):
    thresh = search_carplate(image)
    result = search_text(thresh)

    return result
