from src.features.card_features import CardFeatures
from test.base_test import BaseTest


class TestCard(BaseTest):

    def setup_method(self):
        self.__card_features = CardFeatures()

    def test_item_in_card(self):
        card_page = self.__card_features.add_item_to_card(self.driver)
        card_page.open_page()
        assert (card_page.is_card_visible(), "card is not visible")
