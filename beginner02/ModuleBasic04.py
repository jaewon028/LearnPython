# 4. datetime : 날짜와 시간 정보를 확인하고 조작하는 클래스, 함수 제공
from  datetime import  datetime, timezone, timedelta

now = datetime.now() # 현재 지역의 날짜와 시각 정보를 가진 date time 객체를 얻음
print("{0}={1:02}-{2:02} {3:02}:{4:02}:{5:02}"
      .format(now.year, now.month, now.date(), now.hour, now.minute, now.second))

fmt = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}"
# 각각 네자리 연도정보, 월 정보, 일 정보, 24시간 체계 시간 정보, 분 정보, 초 정보
print(now.strftime(fmt.format(*"년월일시분초")))