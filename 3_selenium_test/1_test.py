def test_start_opencart(browser):
    """
    проферяем запуск для Firefox и Chrome
    :param browser: получаем параметры запуска браузера
    :return:
    """
    # options.headless = True
    driver = browser
    driver.implicitly_wait(20)
    driver.find_element_by_link_text("OpenCart").click()
    url = driver.current_url
    assert url == 'https://www.opencart.com/'
    print(url)
    driver.quit()
