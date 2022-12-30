import pytest

@pytest.mark.usefixtures('setup')  # указываю, какую фикстуру планирую использовать здесь
class TestHomepage:

    def test_homepage(self):
        pass
