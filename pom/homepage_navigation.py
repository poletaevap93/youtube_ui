# здесь будут храниться локаторы и функции, которые будут отвечать за тестирование навигации
from base.selenium_base import SeleniumBase  # для наследования всех методов, которые есть в SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

#from base.utils import Utils


class HomepageNavigation(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)  # init наследует все от супер класса. Инициализация
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'  # Сохраняю в переменную self.nav_links  css локатор, который нашел на сайте macys, это все 13 подразделов сайта. :str - это подсказка типизации. Два нижних подчеркивания в названии - это инкапсуляция, приватная функция

    def get_nav_links(self) -> List[WebElement]:  # функция для поиска всех элементов. -> WebElement - говорим что тут будут возвращены список вебэлементов
        return self.are_visible('css', self.__nav_links, 'Navigation Links')

    def get_nav_links_text(self) -> str:  # отдельный метод для вывода текста найденных выше элементов, т.к. будет список элементов, и нужен особый вывод
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ",".join(nav_links_text)