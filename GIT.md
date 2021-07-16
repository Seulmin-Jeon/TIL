### GIT



## Crawling

##### 요청

```bash
import requests
from bs4 import BeautifulSoup
```

##### 요청을 보낼 주소 저장

```bash
url = '주소'
```

##### res(response)변수에 응답을 저장

```bash
res = requests.get(url)
```

##### bs4모듈을 이용하여 가져온 문서를 파싱

```bash
data = BeautifulSoup(res.text, 'html.parser')
```

##### 선택자를 기준으로 필요한 부분을 꺼내옴

> 검사 - copy - copy selector

```bash
result = data.select_one('필요한 부분')
```

##### 결과를 출력

```bash
print(f'~~~ {result.text} ~~~.')
```



### JSON

##### 요청

```bash
import requests
```

