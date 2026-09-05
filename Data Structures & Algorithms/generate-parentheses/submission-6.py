class Solution:

    def validate(self, _str):
        stk = []
        for ch in _str:
            if "(" == ch:
                stk.append(ch)
            elif stk and ch == ")":
                stk.pop()
            else: return False
        return not stk 

    def generateParenthesis(self, n: int) -> List[str]:
        array = []
        def dfs(balance = ""):

            if len(balance) == 2 * n:
                if self.validate(balance):
                    array.append(balance)
                return
            
            dfs(balance + "(")
            dfs(balance + ")")
            return array
        
        dfs()
        return array