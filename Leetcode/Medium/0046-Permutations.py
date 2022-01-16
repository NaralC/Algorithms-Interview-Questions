class Solution:
    def permute(self, inputNum: List[int]) -> List[List[int]]:
        #Time: O(!n) As there's one less element in the input each time
        #Space: O( !n) Recursion call-stack

        generate(output := [], [], inputNum)
        return output
    
def generate(output, current, inputNum):
    if inputNum == []:
        output.append(current)
    else:
        for idx, num in enumerate(inputNum):
            generate(output, current + [num], inputNum[:idx] + inputNum[idx + 1:])