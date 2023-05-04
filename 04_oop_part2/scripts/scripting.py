#!/usr/bin/env python3
#run chmod +x /path/to/file to create an executable
#os lets us use terminal commnds
import os
#sys lets us take in arguments from the terminal
import sys
input = sys.argv[1]
input2 = sys.argv[2]

class Test:
    pass
#will run when you run the file
if __name__ == "__main__":
    print(f"The first name is {input}")
    print(f"The last name is {input2}")
    os.system("mkdir assets")


