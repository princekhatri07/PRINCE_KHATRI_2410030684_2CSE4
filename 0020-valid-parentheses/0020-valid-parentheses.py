class Solution(object):
    def isValid(self, s):

        st = []
        for c in s:
            if c == '(':
                st.append(')')
            elif c =='{':
                st.append('}')
            elif c=='[':
                st.append(']')
            else:
                if not st or st.pop() != c:
                    return False
        return len(st) == 0

        