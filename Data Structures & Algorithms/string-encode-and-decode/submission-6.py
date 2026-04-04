class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for i in range(len(strs)):
            cur = strs[i]
            strs[i] = str(len(cur)) + "#" + cur

        return ''.join(strs)


    def decode(self, s: str) -> List[str]:

        print
        if not s:
            return []

        res = []
        i = 0

        while i < len(s):
            j = i # delimiter

            while s[j] != '#':
                j += 1
            
            len_str = int(s[i:j]) # Ensure char before delimiter is length
            i = j + 1 # First char after delimiter
            j = i + len_str # End of char based on 

            res.append(s[i:j])

            i = j

        return res
