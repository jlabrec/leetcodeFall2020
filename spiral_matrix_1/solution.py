class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        try:
            while matrix:
                res.extend(matrix.pop(0))
                print(res)
                for i in range(len(matrix)):
                    res.append(matrix[i].pop(len(matrix[i])-1))
                    print(res)
                temp = matrix.pop(len(matrix)-1)
                temp.reverse()
                res.extend(temp)
                for i in range(len(matrix)-1,-1,-1):
                    res.append(matrix[i].pop(0))
            return res
        except IndexError as e: 
            return res
