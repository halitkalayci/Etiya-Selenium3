from project.pages.inv_page import InventoryPage
from project.utils.image_helper import save_screenshot
import time
class TestInvPage():
    def test_product_count(self,driver,waiter):
        inv_page = InventoryPage(driver,waiter)
        inv_page.load()
        assert len(inv_page.get_products()) == 6

    def test_add_to_cart(self,driver,waiter):
        inv_page = InventoryPage(driver,waiter)
        inv_page.load()
        inv_page.add_to_cart("sauce-labs-bike-light")
        inv_page.add_to_cart("sauce-labs-backpack")
        assert inv_page.get_cart_badge_text() == "2"

    def test_sort_z_a(self,driver, waiter):
        inv_page = InventoryPage(driver,waiter)
        inv_page.load()
        inv_page.select_sort(1)
        assert True #Sonradan sıralamanın gerçekten z-a olduğunu doğrula.