# базовый класс с кастомными методами для поиска

from selenium.webdriver.common.by import By   # в 4м селениуме теперь есть класс By, удобный для использования
from selenium.webdriver.support import expected_conditions as ec   # тут импортирую expected_conditions и обзываю сокращенно ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str) -> dict:   # переопределение имп.класса By   find_by: str - аргумент принимает тип данных строку.  -> dict - означает создание словаря. Два нижних подчеркивания вначале названия функции делают функцию приватной (доступной только для этого класса)
        find_by = find_by.lower()  # перевод в нижний регистр, чтобы значение всегда находилось в словаре
        locating = {'css': By.CSS_SELECTOR,   # это словарь.
             'xpath': By.XPATH,
             'class_name': By.CLASS_NAME,
             'id': By.ID,
             'link_text': By.LINK_TEXT,
             'name': By.NAME,
             'partial': By.PARTIAL_LINK_TEXT,
             'tag_name': By.TAG_NAME}
        return locating[find_by]

    def if_visible(self, find_by, locator: str, locator_name: str = None) -> WebElement:  # метод видимости объекта
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)  # функция возвращается вэбэлемент

    def is_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:  # проверка на наличие элемента на странице
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:  # проверка на отсутствие элемента на странице
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by, locator: str, locator_name: str = None) -> List[WebElement]:  # на видимость нескольких элементов на странице
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by, locator: str, locator_name: str = None) -> List[WebElement]:  # на наличие нескольких элементов на странице
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)  # функция возвращается вэбэлемент

    def get_text_from_webelements (self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]