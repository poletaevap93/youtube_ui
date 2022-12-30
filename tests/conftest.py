# в этом файле будут располагаться fixtures (декораторы), которые помогают сетапиться с тестами в других классах, которыми буду пользоваться

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options  # импорт опций браузера

@pytest.fixture
def get_chrome_options():                             # фикстура для установления опций хрома
    options = chrome_options()
    options.add_argument('chrome')                    # вместо chrome можно использовать headless если не нужен UI браузера (чтобы просто на бэке происходили процессы, а окно браузера не открывалось само)
    options.add_argument('--start-maximized')         # чтобы окно открывалось на всю поверхность дисплея
    options.add_argument('--window-size=800,600')     # чтобы окно становилось размером 800х600
    return options

@pytest.fixture                                       # фикстура для инициализации драйвера
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='D:\pythonProject\ChromeDriver\chromedriver.exe', options=options)    # указываю путь до драйвера и стандартному аргументу options из Chrome присваиваю свои options
    return driver

@pytest.fixture(scope='function')          #scope - это то, как тесты будут реагировать на эту фикстуру. function - значит, что если используется эта фикстура, то она будет использоваться при каждом тесте отдельно, т.е. каждый тест будет запускаться как чистый браузер и в нем будет все это исполняться
def setup(request, get_webdriver):        # request - стандартный
    driver = get_webdriver
    url = 'https://www.macys.com/'        # url который будем тестировать
    if request.cls is not None:           # проверка,  не находятся ли разрабатываемые тесты в классе каком либо. Если будут, то...
        request.cls.driver = driver       #...то используем драйвер, чтоб он работал в классе с тестами
    else:                                 # если тесты не находятся в классе, то
        driver.get(url)
    yield driver                          # возвращает драйвер
    driver.quit()                         # полностью закроет браузер, а не одну только страничку
