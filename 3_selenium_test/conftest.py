import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOp
from selenium.webdriver.firefox.options import Options as FoxOp


@pytest.fixture(scope="class")
def open_chrome(request):
    """
    открываем chrome
    :param request:
    :return:
    """
    webdriver.Chrome()
    yield


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        "-B",
        action="store",
        default="chrome",
        help="choose your browser"
    )
    parser.addoption(
        "--url",
        "-U",
        action="store",
        default="http://localhost",
        help="choose your url"
    )
    # parser.addoption(
    #     "--headless",
    #     "-H",
    #     action="store",
    #     default=True,
    #     help="headless option"
    # )


@pytest.fixture
def browser(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')

    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        chrome_options = ChromeOp()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_param == "firefox":
        firefox_options = FoxOp()
        firefox_options.add_argument('-headless')
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.get(request.config.getoption("--url"))
    return driver


# @pytest.fixture(params=["chrome", "safari", "firefox"])
# def parametrize_browser(request):
#     browser_param = request.param
#     if browser_param == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_param == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise Exception(f"{request.param} is not supported!")
#
#     driver.implicitly_wait(20)
#     request.addfinalizer(driver.quit)
#     driver.get(request.config.getoption("--url"))
#     return driver
