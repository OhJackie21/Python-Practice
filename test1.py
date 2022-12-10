dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(love):
  for fkey, fval in dojo.items():
    print(f"{len(fval)} {fkey}")
    for i in range(len(fval)):
      print(fval[i])

printInfo(dojo)