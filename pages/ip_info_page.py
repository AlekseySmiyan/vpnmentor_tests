from .base_page import BasePage


class IpInfoPage(BasePage):
    TITLE = 'What Is My IP Address – 100% Accuracy Free IP Lookup Tool'

    def __init__(self, driver):
        super().__init__(driver)

    def get_view_ip(self):
        view_ip = self.driver.find_element_by_class_name('ip')
        return super().get_text(view_ip)

    def get_view_location(self):
        view_location = self.driver.find_element_by_id('dCountry')
        return super().get_text(view_location)

    def lookup_ip(self, text):
        lookup_field = self.driver.find_element_by_id('iplookup')
        super().input_text(lookup_field, text)
        self.driver.find_element_by_id('cmdSubmit').click()
