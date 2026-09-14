class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            parties = log.split(":")
            id = int(parties[0])
            etat = parties[1]
            time = int(parties[2])
            if etat == "start":
                if stack:
                    output[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                output[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return output

        