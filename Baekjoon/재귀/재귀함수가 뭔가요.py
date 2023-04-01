'''
평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.
매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.
중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.
떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.

입력
교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

출력
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.

예제 입력 1
2
예제 출력 1
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
____"재귀함수가 뭔가요?"
____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
________"재귀함수가 뭔가요?"
________"재귀함수는 자기 자신을 호출하는 함수라네"
________라고 답변하였지.
____라고 답변하였지.
라고 답변하였지.
예제 입력 2
4
예제 출력 2
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
____"재귀함수가 뭔가요?"
____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
________"재귀함수가 뭔가요?"
________"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
________마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
________그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
____________"재귀함수가 뭔가요?"
____________"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
____________마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
____________그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
________________"재귀함수가 뭔가요?"
________________"재귀함수는 자기 자신을 호출하는 함수라네"
________________라고 답변하였지.
____________라고 답변하였지.
________라고 답변하였지.
____라고 답변하였지.
라고 답변하였지.
'''


def what(i, n):
    if i != n:
        print('____' * i + '"재귀함수가 뭔가요?"')
        print('____' * i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    elif i == n:
        print('____' * i + '"재귀함수가 뭔가요?"')
        print('____' * i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * i + '라고 답변하였지.')
        return
    what(i + 1, n)
    print('____' * i + '라고 답변하였지.')
    returnxw


n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
what(0, n)
