# annowork-api-python-client
AnnoWork Python Client


# Requirements
* Python 3.8+ 

# Install

```
$ pip install annoworkapi
```

# Usage

## 認証情報の設定方法

### `$HOME/.netrc`

```
machine annofab.com
login ${user_id}
password ${password}
```

### 環境変数に設定する場合
環境変数`ANNOWORK_USER_ID`にユーザID, `ANNOWORK_PASSWORD` にパスワードを設定する。



## 基本的な使い方

```python
import annoworkapi
service = annoworkapi.build()

result = service.api.get_my_account()
print(result)
# {'account_id': 'xxx', ... }
```


## 応用的な使い方

### ログの出力

```python
import logging
logging_formatter = '%(levelname)-8s : %(asctime)s : %(filename)s : %(name)s : %(funcName)s : %(message)s'
logging.basicConfig(format=logging_formatter)
logging.getLogger("annoworkapi").setLevel(level=logging.DEBUG)
```


```
In [1]: c = s.api.get_actual_working_times_by_organization_member("a9956d30-b201-418a-a03b-b9b8b55b2e3d", "204bf4d9-4569-4b7b-89b9-84f089201247")
DEBUG    : 2022-01-11 17:36:04,354 : api.py : annoworkapi.api : _request_wrapper : Sent a request :: {'request': {'http_method': 'get', 'url': 'https://annowork.com/api/v1/organizations/a9956d30-b201-418a-a03b-b9b8b55b2e3d/members/204bf4d9-4569-4b7b-89b9-84f089201247/actual-working-times', 'query_params': None, 'header_params': None, 'request_body': None}, 'response': {'status_code': 200, 'content_length': 209988}}
```


# 開発者用ドキュメント
[README_for_developer.md](README_for_developer.md) 参照
