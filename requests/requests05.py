import requests
from fake_useragent import UserAgent

# 세션 활성화
s = requests.Session()
# 세션을 이용해 요청
# 브라우저가 가지고 있는 cookies 값 붙여서 보내는 예제
r = s.get('https://httpbin.org/cookies', cookies={'name': 'hong'})
# 리턴된 쿠키 출력
print(r.text)

# 쿠키 저장
# httpbin 규칙에 쿠키를 set 하기 위해 아래의 주소로 요청하라고 함
# r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'hong2'})
# print(r2.text)


# User-Agent
url = 'http://httpbin.org/'
userAgent = UserAgent()
# headers = {'user-agent': userAgent.chrome}
headers = {'user-agent': 'hong_win10'}  # 임의 헤더 설정(다음도 실행됨)

# 헤더 정보 전송
r3 = s.get(url, headers=headers)
print("headers {}".format(s.headers))  # 헤더는 내가 설정한 대로 안 나옴
print(r3.text)


# 세션 종료 - 세션 비 활성화
s.close()


# with 문 => 파일, DB, http  이런 요청들은 외부 자원을 사용하는 일이므로 자동으로 반환
# 위의 코드를 with를 사용하는 경우
# with requests.Session() as s:
#     r = s.get('https://daum.net')
#     print(r.text)
#     print(r.ok)
