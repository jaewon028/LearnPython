# 2. sys 모듈
# 시스템과 관련된 정보에 접근하거나 명령행 매개변수로부터 인자 값을 읽어올 때 활용됨
import sys

print("sys.argv => {0} {1}".format(type(sys.argv), sys.argv))
# sys.argv : 리스트 타입. 명령행에서 python 명령에 전달된 인자들의 정보를 담고 있음.

for i, val in enumerate(sys.argv): # enumerate 객체로 변환 및 반복 실시
    print("sys.argv[{0}] => {1}".format(i, val)) # 인덱스는 변수 i에, 인자 내용은 val에 담겨 출력


