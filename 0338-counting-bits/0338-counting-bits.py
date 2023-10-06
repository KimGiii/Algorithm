class Solution:
    def countBits(self, n: int) -> List[int]:
        # 결과값을 저장할 list를 미리 선언해준다.
        results = [0]

        # 1부터 n까지의 반복횟수를 지정해준다.
        for i in range(1, n+1):
            # i와 i-1의 비트 AND연산을 수행& +1하여 가장 오른쪽 비트를 제거 -> 1의 개수를 센다.
            results.append(results[i & i-1] + 1)
        return results