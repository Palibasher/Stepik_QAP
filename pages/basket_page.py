from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_correct_title()


    def should_be_basket_url(self):
        # Проверка на корректный url адрес
        assert self.browser.current_url == BasketPageLocators.PAGE_URL, "Incorrect Basket Page url"

    def should_be_correct_title(self):
        assert self.is_element_present(*BasketPageLocators.PAGE_TITLE), "Basket title missing"
        assert self.browser.find_element(*BasketPageLocators.PAGE_TITLE).text == "Basket", "Basket title incorrect"

    def should_be_basket_empty(self):
        self.should_be_basket_with_no_items()
        self.should_be_message_if_basket_empty()

    def should_be_message_if_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text == "Your basket is empty. Continue shopping", \
            "Incorrect text in empty basket"

    def should_be_basket_with_no_items(self):
        assert self.is_not_all_elements_present(*BasketPageLocators.ITEMS_FOR_PURCHASE), \
            "Items are presented, but should not be"