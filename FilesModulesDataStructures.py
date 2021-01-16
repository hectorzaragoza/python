#opening a file
#editingType is reading or writing or appending //writing will overwrite things in file, that's why appending is important
#varName = open("fileName.extension", "editingType")

#if file doesnt exist, the w will automatically create it.
#because you didnt specify a path, it will create the output file in the same path of the code file.
out = open("firstOutput.txt", "w")
intOutput = 7
#out.write(string) // Arguments in .write must be string
out.write(("Test String") + (" "))
out.write(str(intOutput) + " ") #adding a space for formatting when appending
out.write("\n") #escape sequence jumps to new line
out.close() #necessary to close first before being able to use out variable again in line 16.

out = open("firstOutput.txt", "a") #append mode

out.write("Appending Text rather than overwriting")
out.close()

#another format of opening a file
with open("firstOutput.txt","a") as out: #opening txt file and storing it as out
    out.write("\n")
    out.write("end of file")
    #using with open will automatically close your file without having to use .close function
    
