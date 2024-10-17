class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS로 재귀 호출, 함수의 첫번째 파라미터 = 합을 갱신할 candidate_sum 
        # 두번째 파라미터 = 순서, 세번째 파라미터 = 지금까지의 탐색 경로

        # 종료 조건
        # 1. candidate_sum < 0 : 목표값을 초과한 경우로 탐색 종료
        # 2. candidate_sum == 0 : candidate_sum의 초기값은 target이며, 일치하는     정답이므로 결과리스트에 추가하고 탐색을 종료

        result = []

        def dfs(candidate_sum, index, path):
            if candidate_sum < 0:
                return
            if candidate_sum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(candidate_sum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result