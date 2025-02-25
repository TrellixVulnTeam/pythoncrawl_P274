# requests 사용 스크랩핑
# REST API : GET, POST, PUT : UPDATE, REPLACE(FETCH :UPDATE, MODIFY), DELETE
# 중요 : url 을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# https://jsonplaceholder.typicode.com/ 사용

import requests
import json

# 세션 활성화 및 json 데이터 요청 / 인코딩 확인 후 set하기
with requests.Session() as s: 
    # 쿠키 설정(쿠키 정보를 자세히 설정할 수 있음 )
    jar = requests.cookies.RequestsCookieJar()
    # 쿠키 삽입
    jar.set('name','test',domain="httpbin.org",path="/cookies")

    # 요청
    r = s.get('http://httpbin.org/cookies',cookies=jar)
    
     # 수신 상태 체크
    r.raise_for_status()  # 이 함수를 쓰면 상태 체크를 한 후 이상이 발생하면 다음 문장을 처리 안함

    # 출력
    print(r.text)