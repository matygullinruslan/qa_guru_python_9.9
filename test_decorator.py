import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene import browser, by, be


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Находим репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type('repo').press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text('repo')).click()


@ allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issues с номером 1{number}')
def should_see_issue_with_number(number):
    s(by.partial_text('number')).should(be.visible)


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')


@allure.feature('Задачи в репозитории')
@allure.severity(Severity.CRITICAL)
@allure.tag('web')
@allure.label('owner', 'matygullin')
@allure.link('https://github.com', name='Testing')


def test_decorator_steps():
    open_main_page()
    search_for_repository('matygullinruslan/qa_guru_python_9.7')
    go_to_repository('matygullinruslan/qa_guru_python_9.7')
    open_issue_tab()
    should_see_issue_with_number('#1')


# @allure.feature('Задачи в репозитории')
# @allure.severity(Severity.CRITICAL)
# @allure.tag('web')
# @allure.label('owner', 'matygullin')
# @allure.link('https://github.com', name='Testing')
