import allure
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selene import browser, by

def test_github():
    with allure.step('Открываем главную страницу'):
        browser.open("/")

    with allure.step('Находим репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').type("matygullinruslan/qa_guru_python_9.7").press_enter()

    with allure.step('Переходим по ссылке'):
        s(by.link_text("matygullinruslan/qa_guru_python_9.7")).click()

        s('#issues-tab').click()
        s(by.partial_text('#1')).should(be.visible)
        ...

