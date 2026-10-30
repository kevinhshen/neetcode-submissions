class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + '#' + i
            

        print("encoded_string: " +encoded_string)
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs = [];
        string = "";
        i = 0

        while i < len(s):
            j=i

            while s[j] != '#':
                j += 1
            
            string_length = int(s[i:j])
            
            i = j + string_length + 1
        
            string += s[j + 1 : i]

            decoded_strs.append(string)
            string=""
        return decoded_strs;
