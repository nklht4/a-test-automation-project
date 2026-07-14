import pytest
import requests

# 用 @pytest.mark.parametrize 装饰器实现参数化
# 这个测试会运行 3 次，每次传入不同的 (post_id, expected_title)
@pytest.mark.parametrize("post_id, expected_title", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
    (2, "qui est esse"),
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),
])
def test_post_title(post_id, expected_title):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == expected_title