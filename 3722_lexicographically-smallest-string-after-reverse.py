# Question Link:
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/description/




class Solution:
    def lexSmallest(self, s: str) -> str:
        org_s=s
        lex_sm_s=min(s,s[::-1])
        if len(s)==1:
            return s
        # for k in range(2,len(org_s)):
        #     first_case=org_s[k-1::-1]+org_s[k:]
        #     second_case=org_s[:len(org_s)-k]+org_s[len(org_s)-1:len(org_s)-k-1:-1]
        #     lex_sm_s=min(lex_sm_s,first_case,second_case)
        # return lex_sm_s



        # first way of list comprehension
        # first_ls=[org_s[k-1::-1]+org_s[k:] for k in range(2,len(org_s))]
        # second_ls=[org_s[:len(org_s)-k]+org_s[len(org_s)-1:len(org_s)-k-1:-1] for k in range(2,len(org_s))]
        # if len(first_ls)==0:
        #     first_ls.append(org_s)
        
        # if len(second_ls)==0:
        #     second_ls.append(org_s)

        # lex_sm_s=min(lex_sm_s,min(first_ls),min(second_ls))
        # return lex_sm_s




        lex_sm_s = min(
            [lex_sm_s] + [
                min(
                    org_s[k-1::-1] + org_s[k:],
                    org_s[:len(org_s)-k] + org_s[len(org_s)-1:len(org_s)-k-1:-1]
                )
                for k in range(2, len(org_s))
            ]
        )
        return lex_sm_s

