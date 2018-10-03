import string
import sys

def make_rot_n(n):
  lc = string.ascii_lowercase
  uc = string.ascii_uppercase
  trans = string.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
  return lambda s: string.translate(s, trans)

for c in range(0, 26):
  rot13 = make_rot_n(c)
  print str(c) + ' || -' + str(26-c) + ' => ' +  rot13(sys.argv[1])
