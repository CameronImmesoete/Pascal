# Retrying the Pascal problem

def PascalNChooseK(n, k):
  if n < 0 or k < 0 or k > n:
    return "Invalid"
  
