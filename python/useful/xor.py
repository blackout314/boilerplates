#!/usr/bin/python
import sys, getopt, ntpath, os

"""
python script.py -s "source.exe" -o "output.exe" -k "key"
"""

def xor(source, output, key):
        contents = bytearray(open(source, "rb").read())
        for i in range(len(contents)):
                for j in range(len(key)):
                        contents[i] ^= ord(key[j])

        with open(output, 'wb') as output:
                output.write(contents)

def main(filename, argv):
        inputfile = ''
        outputfile = ''
        key = ''
                                                        
        try:
                opts, args = getopt.getopt(argv, "hs:o:k:", ["source=", "output=", "key="])
        except getopt.GetoptError:
                print(filename + ' -s <source> -o <output> -k <key>')
                sys.exit(1)
                                                        
        for opt, arg in opts:
                if opt == '-h':
                        print(filename + ' -s <source> -o <output> -k <key>')
                        sys.exit()
                elif opt in ("-s", "--source"):
                        if not os.path.exists(arg):
                                print('The source file does not exist')
                                sys.exit(1)
                        inputfile = arg
                elif opt in ("-o", "--output"):
                        outputfile = arg
                elif opt in ("-k", "--key"):
                        key = arg
                                                        
        if not inputfile or not outputfile or not key:
                print(filename + ' -s <source> -o <output> -k <key>')
                sys.exit(1)
                                                        
        xor(inputfile, outputfile, key)
                                                        
if __name__ == "__main__": main(ntpath.basename(sys.argv[0]), sys.argv[1:])
