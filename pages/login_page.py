from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # 定位器：把所有元素定位集中放在这里
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        """打开登录页面"""
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str):
        """执行登录操作"""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_inventory_item(self, item_name: str):
        """获取商品元素的定位器（用于后续断言）"""
        return self.page.locator(f"text={item_name}")