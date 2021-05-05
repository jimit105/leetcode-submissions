class Solution:
	def reverse(self, x: int) -> int:
		
		rev_x = int(str(abs(x))[::-1])
		return_x = rev_x if x > 0 else -1*rev_x
		
		return return_x if -2 ** 31 <= return_x <= 2 ** 31 - 1 else 0
