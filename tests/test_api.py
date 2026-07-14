import requests


def test_get_post():
    # 这是一个免费的公开测试接口，会返回一条假数据
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 发送 GET 请求
    response = requests.get(url)

    # 验证返回的状态码是 200（代表成功）
    assert response.status_code == 200

    # 验证返回的数据里包含 'id' 这个字段
    data = response.json()
    assert "id" in data

    # 验证返回的 id 是不是 1
    assert data["id"] == 1