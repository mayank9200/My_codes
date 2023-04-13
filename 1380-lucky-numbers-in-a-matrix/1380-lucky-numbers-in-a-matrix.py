class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
#         [3,7,8]
#         [9,11,13]
#         [15,16,17]
        min_list = []
        for row in matrix:
            min_list.append(min(row))
        
        result = []
        for col in zip(*matrix):
            max_num = max(col)
            if max_num in min_list:
                result.append(max_num)
            
        return result