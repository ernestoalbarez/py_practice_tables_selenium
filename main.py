import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate


class Locators:
    london_stock_exchange = 'https://www.londonstockexchange.com/'
    description_cell = '//td[@class="index-description"]/span'
    index_value_cell = '//td[@class="index-value"]/span'
    variation_cell = '//td[@class="index-change"]/span'
    accept_all_button = '//button[@id="ccc-notify-accept"]'


class LondonStockExchange(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(Locators.london_stock_exchange)
        driver.find_element(
            By.XPATH, Locators.accept_all_button
        ).click()   # click on accept all cookies

        description_data = driver.find_elements(
            By.XPATH, Locators.description_cell
        )
        index_value_data = driver.find_elements(
            By.XPATH, Locators.index_value_cell
        )
        variation_data = driver.find_elements(
            By.XPATH, Locators.variation_cell
        )

        head = ["Index", "Value", "Porcentual Change"]
        data = list()   # data will contain linked info from three lists

        for i in range(len(description_data)):
            data = (
                *data,
                (description_data[i].text, index_value_data[i].text, variation_data[i].text)
            )

        print("Original Table")
        print(tabulate(data, headers=head, tablefmt="grid"))

        data_ordered = sorted(
            data,
            key=lambda x: x[1],
            reverse=True
        )

        print("\nTable sorted ascending by value")
        print(tabulate(data_ordered, headers=head, tablefmt="grid"))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
