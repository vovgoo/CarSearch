from scripts.get_number_plant import get_number_carplate
from scripts.get_number_car import get_number_car
from scripts.get_info_car import get_car_name
from scripts.get_google_search import link_with_information

#Рабочие изображние на вывод: test15.jpg, image1.jpg, test15.jpeg, test21.jpg

def main(image):
    resultation = []
    try:
        result = get_number_carplate(image)
        print(result)
        result = get_number_car(result)
        resultation.append(result)
        if result != False:
            result = get_car_name(result)
            resultation.append(result)
            result = link_with_information(result)
            for item in result:
                resultation.append(item)
        else:
            return None
    except:
        return None
    return resultation


# version 1.0
# 1. Новая нейросеть определения текста, более быстрая, и качественная (Был Pytesseract - стал EasyOCR), cужение спектра значений
# 2. Добавление проверок, на качество фото и на проверку верного считывания с номера
# 3. Пробив и вывод всех характеристик о авто
# 4. Создание интерфейса приложения