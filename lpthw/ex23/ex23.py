#importing sys
import sys
#assinging things to be used with argv.
script, encoding, error = sys.argv
#defining the meet of the code
def main(language_file, encoding, errors):
    #setting  var line equal to reading one line in the language_file var.
    line = language_file.readline()
    #if var line has a line in it (line 11) then run line 12.
    if line:
        #
        print_line(line, encoding, errors)
        #final part of the loop throwing it back up to the top to start reading again
        return main(language_file, encoding, errors)
#start of defining the print_line function
def print_line(line, encoding, errors):
    #stripping away the trailing /n on the line strings
    next_lang = line.strip()
    #taking the language from the file and encoding it. next_lang var is a string so need to get it to bytes so call .encode() and pass encoding to encode and how to handle errors
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #this is the inverse of raw_bytes using raw_bytes and calling .decode on it to get a python string. cooked_string should = next_lang
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #print both raw_bytes and cooked_string to show them.
    print(raw_bytes, "<====>", cooked_string)
#opening the actual file we will be reading from
languages = open("languages.txt",encoding="utf-8")
#Kicking off the function with all of the correct parameters. It helps to the start loop which is the if statement.
main(languages, encoding, error)
