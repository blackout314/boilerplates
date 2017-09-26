import sys
import sqlite3

def banner ():
  print """[EXAMPLE]"""

def menu ():
  resp=True
  while resp:
      print """---menu---\n1. Option \n9. Exit/Quit\n----------"""
      print "What would you like to do?"
      resp=raw_input ()
      if resp =="1":
        print "\nOption"
        target = raw_input()
        print target
      elif resp=="9":
        print "\n[>] Goodbye"
        resp = None
      else:
         print"\n Not Valid Choice Try again"

def main (argv):
  banner()
  menu ()

if __name__ == "__main__":
  main(sys.argv[1:])
