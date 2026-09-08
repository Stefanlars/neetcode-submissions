class Solution:

    # approach we can encode into a frequency encoding such as a2b4c1 = aabbbbc followed by a ';' as a seperator. 
    # That way the memory footprint is smaller

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        returnVal = ""

        lengths = []
        str_list = []
        
        for st in strs:
            lengths.append(str(len(st)))
            returnVal += st
        
        returnVal = "#" + ",".join(lengths) + "#" + returnVal
            

        return returnVal

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        returnVal = []

        seen = 0
        lengthString = ""
        startingidx = 0
        for char in s:
            startingidx += 1
            if char == "#":
                seen += 1

                if seen == 2:
                    break
            else:
                lengthString += char
        
        lengths = [int(num) for num in lengthString.split(",")]

        currIdx = startingidx
        for length in lengths:
            returnVal.append(s[currIdx: currIdx + length])

            currIdx += length


        return returnVal