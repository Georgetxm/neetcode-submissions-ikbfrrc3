class Solution:

    # Transforms the string array into 
    # [length of word1, #, word1, length of word2, # word2]
    def encode(self, strs: List[str]) -> str:
        str_count_list = ''
        for word in strs:
            word_len = len(word)
            str_count_list += (str(word_len))
            str_count_list += ("#")
            str_count_list += (word)
 
        return str_count_list

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i

            # Iterate till we reach the delimiter 
            while s[j] != "#":
                j += 1 

            # Since we know length comes before the delimiter based on encoding
            length_of_word = int(s[i:j])
            print(length_of_word)
            # Append whole string which starts from j + 1 till j + 1 + length of word
            decoded_str.append(s[j+1 : j + 1 + length_of_word])
            # set i to new index at end of word
            i = j + 1 + length_of_word

        return decoded_str

