import pytest
import requests
import json

def test_post_data():
    # 1. 准备要发送的 Python 数据（字典）
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # 2. 将 Python 字典序列化为 JSON 字符串
    json_data = json.dumps(new_post)

    # 3. 发送 POST 请求（带上 JSON 数据）
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

    # 4. 验证返回的状态码是 201（创建成功）
    assert response.status_code == 201

    # 5. 把返回的 JSON 反序列化为 Python 字典
    response_data = response.json()

    # 6. 验证服务器返回的 ID 存在（说明真的存进去了）
    assert "id" in response_data
    assert response_data["title"] == "foo"