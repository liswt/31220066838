import difflib
import sys

if __name__=='__main__':
    # Extract the file names from the command line, using the sys lib
    try:
        
        in1=sys.argv[1]
        in2=sys.argv[2]
        out=sys.argv[3]
    except:
        print("The command line argument is incorrect!")
        exit()

    # Read files as string
    try:
        text1=open(in1,'r',encoding='UTF-8').read()
        text2=open(in2,'r',encoding='UTF-8').read()
    except FileNotFoundError:
        print("File not found!")
        sys.exit()


    # Calculate the answer, using the difflib lib
    ans=difflib.SequenceMatcher(None,text1,text2).ratio()

    # Write the answer to the output file, keeping 2 decimal places
    open(out,'w').write(str(round(ans,2)))
