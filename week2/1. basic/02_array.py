"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    """
    예시)
        [1,2,3]

        1 - 0,0 -> 0,2
        2 - 0,1 -> 1,2
        3 - 0,2 -> 2,2

        [4,5,6]

        4 - 1,0 -> 0,1
        5 - 1,1 -> 1,1
        6 - 1,2 -> 2,1

        [7,8,9]

        7 - 2,0 -> 0,0
        8 - 2,1 -> 1,0
        9 - 2,2 -> 2,0
    예시 끝)
    """
    #이중 루프문을 사용하여 새로운 2차원 배열에 데이터 할당
    for i in range(0,n):
        tmp_in_matrix = []
        for j in range(0,n):
            tmp_in_matrix.append(matrix[n-1-j][i])
        out_matrix.append(tmp_in_matrix)
    return out_matrix

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


