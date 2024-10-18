class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 중복된 일정의 경우 어휘순으로 방문
        # 그래프 구성
        # sorted() 함수로 정렬
        # 이후 pop()으로 재귀 호출하면서 모두 꺼내 결과에 추가

        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # 어휘 순으로 결과 출력
        result = route[::-1]

        return result