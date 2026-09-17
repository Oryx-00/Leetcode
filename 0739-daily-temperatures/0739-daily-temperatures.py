class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        solution = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                indice_en_attente = stack.pop()
                taille = abs(indice_en_attente - index)
                solution[indice_en_attente] = taille
            stack.append(index)
        return solution



        