def numbers(n):
  ones=['zero','one','two','three','four','five','six','seven','eight','nine']
  teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  tens=['', '','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
  if n<10:
    return ones[n]
  elif 10<=n<20:
    return teens[n-10]
  elif 20<=n<100:
    if n%10==0:
      return tens[n//10]
    else:
      return tens[n//10]+' '+ones[n%10]
  elif 100<=n<=999:
    if n%100 ==0:
      return ones[n//100]+' hundred only'
    else:
      return ones[n//100]+' hundred and '+numbers(n%100)
      
num=int(input())
print(numbers(num))
    
  
def removec(s1,s2):
  s1_set=set(s1)
  res=[char for char in s1 if char not in s2]
  return ''.join(res)
  
s1,s2=input().split(" ")

print(removec(s1,s2))
      
def palindrome(input_string):
  words=input_string.split()
  non_pali=[word for word in words if word.lower() != word[::-1].lower()]
  return ' '.join(non_pali)
  
input_string=input()
print(palindrome(input_string))
      
      
def mismatch(s1,s2):
  min_len=min(len(s1),len(s2))
  pairs=[]
  for i in range(min_len):
    if s1[i] != s2[i]:
      pairs.append(s1[i]+','+s2[i])
      
  return ' '.join(pairs)
  
s1,s2=input().split(" ")
print(mismatch(s1,s2))
      
      
def solve(s, wordDict):
  word_set = set(wordDict)
  memo = {}
  
  def dfs(s):
    if s in memo:
      return memo[s]
      
    if not s:
      return []
      
    res = []
    
    for i in range(1, len(s) + 1):
      if s[:i] in word_set:
        right_sents = dfs(s[i:])
        if right_sents:
          for right_sent in right_sents:
            res.append(s[:i] + " " + right_sent)
        elif not s[i:]:
          res.append(s[:i])
    memo[s] = res
    return res
    
  return dfs(s)
  
inp = input().split(" ")
n = (int(inp[0]))
inp[1:]
s = inp[-1]
imp = inp[:len(inp)-1]

ans = solve(s, imp)

x = ""
sz = 1000000

for i in ans:
  if len(i.split(" ")) < sz:
    x = i
    sz = len(i.split(" "))
    
print(x)