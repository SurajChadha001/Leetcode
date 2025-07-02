class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()

        n = len(s)

        if n == 0:
            return ""

        first_group_size = n % k id n % k  != 0 else k 

        result = s[:first_group_size]

        for i i range(first_group_size, n , k):
            result += '-' + s[i:i+k]

        return result