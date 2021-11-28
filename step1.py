#Shebang line
#!/usr/local/bin/python3

#Import Modules
import os, sys, shutil, subprocess
print("\nImported os, sys, shutil and subprocess\n")

os.system('clear')

#______________________________________________#

#User entry functions
def user(Protein, Taxonomic_group):
        import string
        print("The following details have been provided:\n\tProtein family: ",Protein, "\n\tTaxonomic_group: ",Taxonomic_group)


#Store output in an ordered Dictionary

questions ={}
questions["protein"] = input("Please enter protein family:\n")
questions["taxonomic_group"] = input("Please enter taxonomic group:\n")

protein = questions["protein"]
taxonomic_group = questions["taxonomic_group"]
user(*list(questions.values()))


#Retrieve the sequences using Esearch and Efetch from EDirect
#Ask the user the user if they want Partial or full sequences

sequence_full = input("Do you want partial sequences?[YES|NO]\n").upper()

#Retrieve full sequences
if sequence_full == "YES":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein]' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)

#Retrieve partial sequences
elif sequence_full == "NO":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein] NOT PARTIAL' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)

#Any other input
else:
     	print("Session ended")
	sys.exit()


#Limit the number of sequences

#Ask the user if they would like to see how many sequences were downloaded
count = input("Would you like to see how many sequences were downloaded?[YES|NO]\n").upper()

#Print the number of sequences downloaded
if count == "YES":

	#Count the number of sequences present
	file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_contents = file.read()
	seq_count = file_contents.count(">")
	print("The number of sequences is downloaded", seq_count)

#Do not print the number of sequences present
elif count == "NO":
	print("Continuing anyway")

#Any other input
else:
	print("Continuing anyway")

#Align multiple retrieved sequences using Clustalo
#Ask the user if they would like to align the protein sequences
align = input("Would you like to align the protein sequences?[YES|NO]\n").upper()

#Run Clustalo
if align == "YES":
	#Run clustalo and change fasta format to msf format for plotcon step
	subprocess.call("clustalo -i {0}.{1}.fa -o {0}.{1}.msf -t protein --outfmt msf -v".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#If no, ended session
elif align == "NO":
	print("Session Ended")
	sys.exit()

#If anything else, end session
else:
	print("Session Ended")
	sys.exit

#Give basic alignment information
#Ask the user would they like to see basic align information
info_align = input("Would you like to see the basic alignment information?[YES|NO]\n").upper()

if info_align = "YES":
	subprocess.call("infoalign {0}.{1}.fa {0}.{1}.infoalign.fa".format(questions["taxonomic_group"],questions["protein"]), shell = True)
	#Print the output of the infoalign file
	file1 = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file1_contents = file1.read()
	print(file1_contents)

#Continue on without doing infoalign
elif info_align = "NO":
	print("Continuing anyway")

#For any other input, continue on 
else:
	print("Continuing anyway")


#Plotcon
#Ask the user if they would like to create a conservation plot of the protein sequences 
plot = input("Would you like to create a conservation plot of the protein sequences?[YES|NO]\n").upper()

windowsize = input("Please specify a window size to create the plot. Please see manual for description of windowsize: " )
os.environ['ws'] = windowsize 

#Make a plotcon graph and save it 
if plot == "YES":
	subprocess.call("plotcon -sformat msf {0}.{1}.msf $ws  -graph ps".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Do not save the plotcon graph and continue on
elif plot == "NO":
	print("Continuing anyways")

#Any other input
else:
	print("Continuing anyways")
	

#Ask the user if they would like to view a conservation plot of the protein sequences	
view = input("Would you	like to view a conservation plot of the protein sequences?[YES|NO]\n").upper()

#Show the plotcon graph
if view == "YES"
	subprocess.call("plotcon -sformat msf {0}.{1}.msf $ws -graph x11".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Do not show the plotcon graph
elif view == "NO"
	print("Continuing anyway")

#Any other input
else:
	print("Continuing anyways")


#Scan the PROSITE database
#Split the dataset into individual sequences for patmatmotifs
subprocess("seqretsplit {0}.{1}.fa seqoutall".format(questions["taxonomic_group"],questions["protein"]), shell = True) 

#Run Prosite on all the individual files 
#Ask the user would they like to ignore simple patterns 
simple = input("Would you like to ignore simple patterns such as post-translational modification sites?[YES|NO]\n").upper()

#Ignore the simple patterns
if simple == "YES":
	prosite_command ="for file in *.fasta; do patmatmotifs -noprune -sequence $file  -sformat1 fasta  "(basename "$file .fasta)".patmatmotifs; done"
	subprocess(prosite_command, shell = True)

#Give full sequences
elif simple == "NO":
	prosite_command ="for file in *.fasta; do patmatmotifs -full -sequence $file  -sformat1 fasta  "(basename "$file .fasta)".patmatmotifs; done"
	subprocess.call(prosite_command, shell = True)

#Anything else
else:
	print("Session Ended")
	sys.exit()


#End Session
print("Protein analysis complete. Thank you for you participation")
sys.exit()



