class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        # 순환 구조인지를 판단하기 위한 traced
        # 한번 방문했던 노드를 저장하기 위한 visited
        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            
            # 이미 방문했던 노드라면 True
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True
        
        # 슨환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True