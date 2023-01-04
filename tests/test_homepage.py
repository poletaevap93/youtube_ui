import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By   # в 4м селениуме теперь есть класс By, удобный для использования
from selenium.webdriver.support import expected_conditions as ec   # тут импортирую expected_conditions и обзываю сокращенно ec
from selenium.webdriver.support.ui import WebDriverWait   # тут импортирую само ожидание

from pom.homepage_navigation import HomepageNavigation


@pytest.mark.usefixtures('setup')  # указываю, какую фикстуру планирую использовать здесь
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNavigation(self.driver) # импортирую cозданный класс HomepageNavigation. Теперь есть объект класса HomepageNavigation
        print(homepage_nav.get_nav_links_text)


     #------------------------------------------
       # driver = webdriver.Chrome()

        # ---- не совсем популярный вариант поиска, но рабочий
       # driver.implicitly_wait(10)   # указываем ожидание в секундах. Но это не лучший вариант, лучше вэбдрайвервэйт
       # driver.find_element(By.CSS_SELECTOR, '#id123')

        #----- этот вариант лучше использовать, т.к. тут используется ec, поэтому есть намного больше вариаций ожиданий
        # wait = WebDriverWait(driver, 15, 0.3)   # тут указываю сначала мой драйвер, потом время в секундах, сколько буду ждать элемент. потом можно указать частоту(через сколько будет проверка автоматическая, стандарт стоит - 0.5 сек)
        #  element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id123')))     #until - подожди до момента, пока что-то не исполнится. Вставляю импортированный ec (ожидаемое условие и вызываю нужынй метод ),   . В итоге вернется вэбэлемент

        #----- второй вариант использовать лучше, т.к. , т.к. find_element - просто говорит, присутствует ЛИ эл-т на странцие, а expected_conditions можно проверять на видимость и тд, спектр намного шире


