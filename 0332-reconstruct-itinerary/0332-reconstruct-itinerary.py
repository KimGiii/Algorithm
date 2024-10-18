class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # pop()은 O(1)이지만 pop(0)는 O(n)
        # 좀 더 효율적인 구현을 위해, pop() 즉 스택의 연산으로 처리
        # 그래프를 역순으로 구성
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        result = route[::-1]

        return result