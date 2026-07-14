import pytest
from playwright.sync_api import Page


def test_saucedemo_login(page: Page):
    # 1. 打开浏览器，访问目标网站
    page.goto("https://www.saucedemo.com")

    # 2. 定位用户名输入框（通过HTML属性 id），并输入用户名
    page.fill("#user-name", "standard_user")

    # 3. 定位密码输入框（通过HTML属性 id），并输入密码
    page.fill("#password", "secret_sauce")

    # 4. 定位登录按钮（通过HTML属性 id），并点击
    page.click("#login-button")

    # 5. 验证登录成功后，页面上是否存在指定文本的链接
    # 这里使用文本定位器，更贴近真实用户行为
    assert page.locator("text=Sauce Labs Backpack").is_visible()