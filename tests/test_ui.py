import pytest
from playwright.sync_api import Page


def test_baidu_title(page: Page):
    # 打开百度
    page.goto("https://www.baidu.com")

    # 验证页面标题是否包含 "百度"
    assert "百度" in page.title()