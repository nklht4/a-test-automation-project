import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_saucedemo_login(page: Page):
    # 1. 创建 LoginPage 实例
    login_page = LoginPage(page)

    # 2. 打开登录页面
    login_page.navigate()

    # 3. 执行登录操作
    login_page.login("standard_user", "secret_sauce")

    # 4. 使用 page object 获取商品并断言
    item = login_page.get_inventory_item("Sauce Labs Backpack")
    assert item.is_visible()