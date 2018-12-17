#importing the things agian
from sys import argv
from os.path import exists

#adding script, from_file and to_file to argv
script, from_file, to_file = argv

#printing out what is being copied, those args are being taken from what is being passed in at execution in that order.
print (f"copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#printing the length(len) of the data in from_file which is being read to var indata.
print(f"The input file is {len(indata)} bytes long")

#checking to see if the output file, aka the second file passed at execution, exists (nothing written to handle it not being there)
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue or CTRL-C to abort")

#opening to_file and making sure we can write to it.
out_file = open(to_file, 'w')
#here we are writing to out_file which is above and we are writing the contents of indata to it. the whole function copies from one file to another
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
