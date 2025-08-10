import allure

from src.pages.card_page import CardPage


class CardFeatures:

    @allure.step("Open Card page, click add item button,add item")
    def add_item_to_card(self, driver) -> "CardPage":
        return (CardPage(driver)
                .open_page()
                .click_to_here_btn()
                .click_add_to_card_button()
                .click_continue_shop_btn())
