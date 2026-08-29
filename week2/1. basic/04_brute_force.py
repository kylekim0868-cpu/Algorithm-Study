"""
[완전 탐색 - 배열에서 두 수의 합 찾기]

문제 설명:
- 정수 배열과 목표 값이 주어졌을 때, 배열에서 두 수를 선택하여 
  그 합이 목표 값과 같아지는 모든 쌍을 찾습니다.
- 완전 탐색(Brute Force) 방식으로 모든 경우를 확인합니다.

입력:
- nums: 정수 배열
- target: 목표 합

출력:
- 합이 target이 되는 (i, j) 인덱스 쌍의 리스트 (i < j)

예제:
입력: nums = [2, 7, 11, 15, 3], target = 9
출력: [(0, 1), (0, 4)]
설명: nums[0] + nums[1] = 2 + 7 = 9
      nums[0] + nums[4] = 2 + 7 = 9 (중복이지만 인덱스가 다름)

실제로는: nums[0] + nums[1] = 2 + 7 = 9만 해당


"""

def find_two_sum_pairs(nums, target):
    """
    배열에서 합이 target이 되는 모든 인덱스 쌍 찾기
    
    Args:
        nums: 정수 배열
        target: 목표 합
    
    Returns:
        list: (i, j) 인덱스 쌍의 리스트
    """
    pairs = []
    n = len(nums)
    """
        1) 아이디어
            이중루프를 활용. 모든 경우의 수를 찾는다.
            첫 번째 루프: nums i
                두 번째 내부 루프: 
                    i를 제외한 나머지 숫자와의 합을 계산.
                    첫 번째 루프의 값과 내부 루프의 합이 같다면 index 추출 후. pairs에 넣기.
    """
    for i in range(0,n-1): #자기 자신(기준 수)을 제외한 수와 합산해야하기 때문에 n이 아닌 n-1
        for j in range(i+1,n): #기준 수와 합산할 대상 수는 포함되야 하기 때문에 n
            if target == nums[i]+nums[j]: 
                tmp = (i,j)
                pairs.append(tmp)         

    return pairs

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_two_sum_pairs(nums1, target1)
    print(f"배열: {nums1}")
    print(f"목표 합: {target1}")
    print(f"결과 쌍: {result1}")
    print()
    
    # 테스트 케이스 2
    nums2 = [1, 3, 4, 2, 5, 6]
    target2 = 7
    result2 = find_two_sum_pairs(nums2, target2)
    print(f"배열: {nums2}")
    print(f"목표 합: {target2}")
    print(f"결과 쌍: {result2}")
    print()
    
    # 테스트 케이스 3
    nums3 = [1, 1, 1, 1]
    target3 = 2
    result3 = find_two_sum_pairs(nums3, target3)
    print(f"배열: {nums3}")
    print(f"목표 합: {target3}")
    print(f"결과 쌍: {result3}")


