
from src.pages.card_page import CardPage
from src.pages.products_page import ProductsPage
from test.base_test import BaseTest


class TestCard(BaseTest):

    def test_item_in_card(self):
        card_page = CardPage(self.driver).open_page()
        card_page.click_to_here_btn()
        (ProductsPage(self.driver)
         .click_add_to_card_button()
         .click_continue_shop_btn())
        card_page.open_page()
        assert(card_page.is_card_visible(),"card is not visible")

