class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        return self.driver.get(url)

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_text(self, element):
        return element.text
