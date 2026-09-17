class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        solution  = prices.copy()
        for index in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[index]:
                index_en_attente = stack.pop()
                solution[index_en_attente] -= prices[index]
            stack.append(index)

                
        return solution


            
        