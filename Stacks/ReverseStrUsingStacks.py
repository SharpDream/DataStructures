# Leetcode 344. Reverse String
# or a list

def reverseString(string: str) -> str:
  # time complexity: o(n)

  s = [x for x in string]

  l,r = 0, len(s)-1
  while l<r:
    s[l],s[r] = s[r],s[l]
    l,r = l+1,r-1

  return "".join(s)
