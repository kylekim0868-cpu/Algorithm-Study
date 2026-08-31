"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    """
            처음 아이디어
                1) Stack > LIFO(선입선출): 오래된 데이터는 가장 아래에 쌓인다는 개념?
                2) 이 개념을 CS에 대입한다면 어떻게 생각해야 할까?
                    2-1) 문자열을 순회하면서 여는 괄호와 닫는 괄호를 구분하여 각기 다른 2개의 배열에 넣는다?
                3) 괄호의 올바른 짝지음은 어떻게 코드로 구현을 해야할 것에 대한 고민 필요
                    -> 3-1) 2-1)에서 넣었던 2개의 배열의 길이가 다르다면 False
                    -> 3-2) 2개의 배열의 길이가 같다면 True
                    => 이 2가지의 분기처리만으론 짝짓기 검증 오류가 발생.
            AI와 교류한 아이디어
                1) 문자열 순회
                2) 빈 배열에 여는 괄호가 있다면 push
                3) 닫는 괄호가 있다면 pop 
                4) 순회가 끝난 후에 배열이 비어있다면 True / 배열이 비어있지 않다면 False
                    ex) "()()"
                        1) "(" => stack = [(] push
                        2) ")" => stack = [] pop
                        3) "(" => stack = [(]
                        4) ")" => stack = [] pop
                        5) stack = [] 비어있으므로 True 반환
                    ex) "))))" 
                        1) "(" => stack = [] pop -> False 빈 배열에서 pop매서드를 사용하면 에러가 나기 때문에 예외 처리는 필수.
    """
    """
        ************************구현1************************
    """
    stack = []
    for chr in s:
        if(chr == "("):
            stack.append(chr)
        elif(chr == ")"):
            if(len(stack) == 0):
                return False
            else: stack.pop()
    if(len(stack) == 0):
        return True
    else:
        return False
    
    """
        ************************구현1************************
    """    
  

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


