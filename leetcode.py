class Solution:
    def fun(self, nums: list[int]) -> int:

        num = len(nums)
        key_a = nums.copy()
        key_b = nums.copy()
        key_a.sort()
        key_b.sort(reverse=True)
        p1, p2 = 0, num
        for i in range(num):
            if nums[p1:p2] == key_a:
                break
            if nums[p1:p2] == key_b:
                p1+=1
                break
            nums.append(nums[p1])
            p1 += 1
            p2 += 1
            if i == num-1:
                p1 =-1
        return p1
    def minOperations(self, nums: list[int]) -> int:
        re_nums = nums.copy()
        re_nums.reverse()
        answer1 = self.fun(nums)
        answer2 = self.fun(re_nums) + 1
        print(answer1, answer2)
        return min(answer1, answer2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations([1,0,2]))


