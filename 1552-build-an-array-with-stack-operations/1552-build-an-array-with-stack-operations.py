class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        liste_str = []
        Push = "Push"
        Pop = "Pop"

        for i in range(1, n + 1):
            if i == target[-1]:
                liste_str.append(Push)
                return liste_str
                break
            if i in target:
                liste_str.append(Push)
            else:
                liste_str.append(Push)
                liste_str.append(Pop)
        return liste_str


            


        