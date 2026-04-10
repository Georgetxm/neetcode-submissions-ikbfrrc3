class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        degrees = [0] * numCourses

        for item in prerequisites:
            course, pre = item

            adj_list[pre].append(course)
            degrees[course] += 1

        q = deque()

        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        taken = 0

        while q:
            node = q.popleft()

            taken += 1

            for nei in adj_list[node]:
                degrees[nei] -= 1

                if degrees[nei] == 0:
                    q.append(nei)

        return taken == numCourses

        