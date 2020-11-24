def countEval(expr, desired):
  d = {}
  trues, falses = booleanEval(expr, d)
  if desired == True:
    return trues
  return falses 


def booleanEval(expr, d):
  trues, falses = 0, 0
  if len(expr) == 1:
    res = True if expr == "1" else False
    if res:
      trues = 1
    else:
      falses = 1
    return trues, falses
  
  for i in range(1, len(expr), 2):
    op = expr[i]
    l, r = expr[:i], expr[i+1:]
    ltrues, lfalses, rtrues, rfalses = 0, 0, 0, 0
    if l in d.keys():
      ltrues, lfalses = d[l][0], d[l][1]
    else:
      ltrues, lfalses = booleanEval(l, d)
      d[l] = (ltrues, lfalses)
    if r in d.keys():
      rtrues, rfalses = d[r][0], d[r][1]
    else:
      rtrues, rfalses = booleanEval(r, d)
      d[r] = (rtrues, rfalses)
  
    if op == "^":
      trues += ltrues * rfalses + lfalses * rtrues
      falses += ltrues * rtrues + lfalses * rfalses
    elif op == "|":
      trues += ltrues * rfalses + lfalses * rtrues + ltrues * rtrues
      falses += lfalses * rfalses
    elif op == "&":
      trues += ltrues * rtrues
      falses += lfalses * rfalses + ltrues * rfalses + lfalses * rtrues
  return trues, falses




print(countEval("0&0&0&1^1", False))