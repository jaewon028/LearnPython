# 완전검색(Exhaustive Search)
'''
문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
 1) Brute-force 혹은 Generate-and-Test 기법이라고도 불림
 2) 모든 경우의 수를 테스트한 후, 최종 해법을 도출함
 3) 일반적으로 경우의 수가 상대적으로 작을 때 유용
 4) 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못 할 확률이 적음
 5) 주어진 문제를 풀 때, 우선은 완전 검색으로 접근하여 해답을 도출한 후,
    성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직.

예) Baby-gin 게임
 0~9 중에 6장 ==> 3장 연속번호 : run, 3장 동일 번호 : triplete
 6장 카드가 run과 triplete으로 구성된 경우 ==> Baby-gin
   ex1) 667767 두개의 triplete ==> 666, 777
   ex2) 054060 한개 run, 한개 triplete ==> 456, 000
   ex3) 101123 한개 triplete, 023은 run이 아님 ==> 123, 011

 1) 고려할 수 있는 모든 경우의 수 생성.
    2,3,5,7,7,7 으로 모든 경우 나열.
 2) 해답 테스트.
    여부 확인: 235, 777 ==> Baby-gin 아님..

순열
nPr = n*(n-1)*(n-2)* ...... *(n-r+1)
nPn = n! = n*(n-1)*(n-2)* ..... *2*1

'''
# {1,2,3}을 포함하는 모든 순열을 생성하는 함수
def permutation():
    for i1 in range(1,4):
        for i2 in range(1,4):
            if i2 != i1:
                for i3 in range(1,4):
                    if i3 != i1 and i3 != i2:
                        print(i1,i2,i3)

permutation()





# Greedy Algorithm
'''
최적 해를 구하는데 사용되는 근시안적인 방법
 1. 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을
    선택해 나가는 방식으로 진행하여 최종적인 해답에 도달함
 2. 각 선택 시점에서 이루어지는 결정은 지역적으로 최적이지만, 그것들을 계속 수집하여
    최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없음.
 3. 일반적으로, 머리속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 됨.
 
탐욕 알고리즘의 수행 과정
 1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한뒤, 이를 부분 해 집합(Solution Set)에 추가.
 2. 실행 가능성 검사 : 새로운 부분 해 집합이 실행 가능한지를 확인.
                    곧, 문제의 제약 조건을 위반하지 않는지를 검사함.
 3. 해 검사 : 새로운 부분 해 집합이 문제의 해가 되는지를 확인.
            아직 전체 문제의 해가 완성되지 않았다면 해 선택부터 다시 시작함.

예) 거스름돈 줄이기
    해 선택 : 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가.
    실행 가능성 검사 : 액수 초과하는지 확인.
                초과한다면, 한 단계 작은 단위 동전 추가.
    해 검사 : 드려야 하는 액수와 일치하는지 확인.
            모자란다면 다시 해 선택으로 돌아가서 거스름돈에 추가할 동전을 고름.

예) 완전 검색이 아닌 Baby-gin 방법으로 풀기.
 1. 6개의 숫자는 6자리 정수 값으로 입력됨.
 2. COUNTS 리스트의 각 원소를 체크하여 run과 triplete 및 Baby-gin 여부 판단.
    - 탐욕 알고리즘을 적용
    - COUNTS 리스트에서 run과 triplete 중에 가능한 것을 조사
    - 조사에 사용한 데이터 삭제.
    - 남은 데이터를 다시 run과 triplete 중에 가능한지 조사.
    
탐욕 알고리즘 접근 경우, 해답 찾지 못할 때
 : 입력 받은 숫자를 정렬한 후, 앞뒤 3자리씩 끊어서 run 및 triplete을 확인하는 방법 고려.
 
'''



# Sort
'''
2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값, 혹은 그 반대 순서대로 재배열 하는 것.
 키 : 자료를 정렬하는 기준이 되는 특정 값

대표적인 정렬 방식의 종류
 - 버블 정렬
 - 카운팅 정렬
 - 선택 정렬
 - 퀵 정렬
 - 삽입 정렬
 - 병합 정렬
 
 1. 버블 정렬 : 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식 ( O(n2) )
 
 2. 카운팅 정렬 : 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
                선형시간에 정렬하는 효율적인 알고리즘 ( O(n+k) ) : n 리스트갯수, k 정수최대값 )
 

'''

