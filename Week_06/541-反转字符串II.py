class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        n1=n//(2*k)
        d=list(s)
        for i in range(n1):
            u=d[2*k*i:2*k*i+k]
            d[2*k*i:2*k*i+k]=u[::-1]
        u=d[n1*2*k:]
        if len(u)<k:
            d[n1*2*k:]=u[::-1]
        if len(u)<2*k and len(u)>=k:
            u1=u[:k]
            u[:k]=u1[::-1]
            d[n1*2*k:] = u
        return ''.join(d)