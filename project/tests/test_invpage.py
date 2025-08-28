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
    
    def test_product_titles(self, driver, waiter):
        """Tüm ürün title'larının doğru olduğunu kontrol eder"""
        inv_page = InventoryPage(driver, waiter)
        inv_page.load()
        
        # Beklenen ürün title'ları
        expected_titles = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light", 
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]
        
        # Gerçek ürün title'larını al
        actual_titles = inv_page.get_product_titles()
        
        # Title sayısını kontrol et
        assert len(actual_titles) == 6, f"Beklenen 6 ürün, bulunan: {len(actual_titles)}"
        
        # Her title'ın doğru olduğunu kontrol et
        for i, (expected, actual) in enumerate(zip(expected_titles, actual_titles)):
            assert expected == actual, f"Urun {i+1}: Beklenen '{expected}', Gercek '{actual}'"