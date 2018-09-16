#!/usr/bin/python
import sys
from optparse import OptionParser
#class for opening files and retrieving each line
class filelist:
    def __init__(self, filename, parser):
        try:
            f = open(filename, 'r')
            self.lines = []
            self.lines = f.readlines()
            f.close()
        except:
            parser.error("Cannot read file")
#this function retursn the each line from an opened file in a list
    def returnlines(self):
        return self.lines
    
def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2"""
#parser creates a boolean variable to store any additional input commands
    parser = OptionParser(version=version_msg, usage=usage_msg)
    parser.add_option("-1", action="store_true", dest="first", default=0)
    parser.add_option("-2", action="store_true", dest="second", default=0)
    parser.add_option("-3", action="store_true", dest="third", default=0)
    parser.add_option("-u", action="store_true", dest="unsorted", default=0)
    options, args = parser.parse_args(sys.argv[1:])
#parser variable 'args' contains input files

    if len(args) != 2:           #can not be more than two input files
        parser.error("Wrong number of operands")

    if args[1] == "-":           #checks for stdin input case
        file2 = filelist(args[0], parser) 
        f1 = sys.stdin.readlines()
    else:
        file1 = filelist(args[0], parser)
        file2 = filelist(args[1], parser)
        f1 = []
        f1 = file1.returnlines()

    f2 = []
    f2 = file2.returnlines()

    tab = "\t"
    newline = "\n"
    output = ""

    if options.unsorted == 0:
        #creates list containing duplicate words and removes those words from other lists
        f3 = [i for i in f1 if i in f2]
        for word in f3:
                f1.remove(word)
                f2.remove(word)
        #creates a unique list of ever word from each input file           
        out = sorted(set(f1 + f2 + f3))
            
        i = 0
        while i < len(out):
            #loops through every unique word and adds it to output stream plus number of tabs depending on commands and column location
            for word in f3: #checks for matches for duplicate words
                if out[i] == word:
                    if options.third == 0 and options.second == 0 and options.first == 0:
                        output+= tab + tab + out[i]
                        if "\n" not in out[i]:
                            output+=newline              #ensures that output word will have a newline character
                    elif options.third == 0 and (options.second == 0 or options.first == 0):
                        output += tab + out[i]
                        if "\n" not in out[i]:
                            output+=newline
                    elif options.third == 0:
                        output+= out[i]
                        if "\n" not in out[i]:
                            output+=newline

            for word in f1:                    #checks for matches in first input file
                if out[i] == word:
                    if options.first == 0:
                        output += out[i]
                        if "\n" not in out[i]:
                            output+=newline

            for word in f2:                     #checks for matches in second input file
                if out[i] == word:                    
                    if options.second == 0 and options.first == 0:
                        output+= tab + out[i]
                        if "\n" not in out[i]:
                            output+=newline
                    elif options.second == 0 and options.first != 0:
                        output+= out[i]
                        if "\n" not in out[i]:
                            output+=newline
                        
            i+=1

    else:
        #creates third list containing duplicates and removes duplicates from second column list
        f3 = [i for i in f1 if i in f2]
        for word in f3:
                f2.remove(word)

        i = 0
        while i < len(f1):   #loops through every word in the first input file
            if f1[i] in f3:  #adds word to string if its found in the third column, plus certain number of tabs
                    if options.third == 0 and options.second == 0 and options.first == 0:
                        output += tab + tab + f1[i]
                        if "\n" not in f1[i]:
                            output+=newline             #ensures words end with newline character
                    elif options.third == 0 and (options.second == 0 or options.first == 0):
                        output += tab + f1[i]
                        if "\n" not in f1[i]:
                            output+=newline
                    elif options.third == 0:
                        output += f1[i]
                        if "\n" not in f1[i]:
                            output+=newline
            elif f1[i] not in f3 and options.first == 0: #checks for whether or not first file words should be printed
                output += f1[i]
                if "\n" not in f1[i]:
                    output+=newline
                
            i+=1
            
        if options.second == 0:
            for word in f2:  #if second file should be printed, loops through all non duplicate words in second file and adds them to output
                if options.first != 0:
                    output += word
                    if "\n" not in word:
                        output+=newline
                else:
                    output += tab + word
                    if "\n" not in word:
                        output+=newline

    sys.stdout.write(output)  #prints out output stream
    
if __name__ == "__main__":
    main()
