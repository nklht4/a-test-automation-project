import pytest
from playwright.sync_api import Page, expect


def test_saucedemo_login(page: Page):
    # 1. 打开浏览器，访问目标网站
    page.goto("https://www.saucedemo.com")

    # 2. 使用显式等待：等待用户名输入框可见并输入（最多等待 10 秒）
    page.wait_for_selector("#user-name", state="visible", timeout=10000)
    page.fill("#user-name", "standard_user")

    # 3. 等待密码输入框可见并输入
    page.fill("#password", "secret_sauce")

    # 4. 点击登录按钮
    page.click("#login-button")

    # 5. 等待商品列表加载完成，并验证指定商品可见
    #    使用 expect 配合 to_be_visible() 进行智能等待
    expect(page.locator("text=Sauce Labs Backpack")).to_be_visible(timeout=10000)