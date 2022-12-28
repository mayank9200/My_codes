class Solution:
    def build_expression(self,nums, target, i, cur_sum, cur_expression,memo):
          # Base case: if we have reached the end of the list, check if the sum
          # of the numbers in the expression is equal to the target
          if i == len(nums):
            if cur_sum == target:
              #print(cur_expression)
              return 1
            else:
              return 0
          if (i, cur_sum) in memo:
            return memo[(i, cur_sum)]
  
          # Try adding the current number to the expression with a '+' symbol
          count = self.build_expression(nums, target, i + 1, cur_sum + nums[i], cur_expression + '+' + str(nums[i]),memo)
          # Try adding the current number to the expression with a '-' symbol
          count += self.build_expression(nums, target, i + 1, cur_sum - nums[i], cur_expression + '-' + str(nums[i]),memo)
          memo[(i, cur_sum)] = count
          return count

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        memo={}
        return self.build_expression(nums, target, 0, 0, '',memo)
        #return self.dp(nums, target, index, curr_sum)