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

if sequence_full == "YES":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein]' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)
elif sequence_full == "NO":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein] NOT PARTIAL' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)
else:
     	print("Session ended")
	sys.exit()


#Limit the number of sequences

#Ask the user if they would like to see how many sequences were downloaded
count = input("Would you like to see how many sequences were downloaded?[YES|NO]\n").upper()

if count == "YES":

	#Count the number of sequences present
	file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_contents = file.read()
	seq_count = file_contents.count(">")
	print(seq_count)

elif count == "NO":
	print("Continuing anyway")

else:
	print("Continuing anyway")

	
#Remove redundant sequences 
#redundant = input("Would you like to remove redundant sequences?"YES|NO\n").upper()

#if redundant == "YES":
	subpro

#Align multiple retrieved sequences using Clustalo
#Ask the user if they would like to align the protein sequences
align = input("Would you like to align the protein sequences?[YES|NO]\n").upper()

if align == "YES":
	#Run clustalo and change fasta format to msf format for plotcon step
	subprocess.call("clustalo -i {0}.{1}.fa -o {0}.{1}.msf -t protein --outfmt msf -v".format(questions["taxonomic_group"],questions["protein"]), shell = True)

elif align == "NO":
	print("Session Ended")
	sys.exit()
else:
	print("Session Ended")
	sys.exit

#Give basic alignment information
#Ask the user would they like to see basic align information
info_align = input("Would you like to see the basic alignment information?[YES|NO]\n").upper()

if info_align = "YES":
	subprocess.call("infoalign {0}.{1}.fa {0}.{1}.infoalign.fa".format(questions["taxonomic_group"],questions["protein"]), shell = True)
elif info_align = "NO":
	print("Continuing anyway")
else:
	print("Continuing anyway")

#Plotcon
#Ask the user if they would like to create a conservation plot of the protein sequences 
plot = input("Would you like to create a conservation plot of the protein sequences?[YES|NO]\n").upper()

if plot == "YES":
	subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize 4 -graph ps".format(questions["taxonomic_group"],questions["protein"]), shell = True)
elif plot == "NO":
	print("Session Ended")
	sys.exit()
else:
	print("Session Ended")
	sys.exit()

#Ask the user if they would like to view a conservation plot of the protein sequences	
view = input("Would you	like to view a conservation plot of the protein sequences?[YES|NO]\n").upper()

if view == "YES"
	subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize 4 -graph x11".format(questions["taxonomic_group"],questions["protein"]), shell = True)
elif view == "NO"
	print("Continuing anyway")
else:
	print("Contiuing anyways")


#Scan the PROSITE database
#Split all the dataset into individual sequences
subprocess("seqretsplit {0}.{1}.fa seqoutall".format(questions["taxonomic_group"],questions["protein"]), shell = True) 

#Run Prosite on all the individual files 
prosite_command ="for FILE in *.fasta; do patmatmotifs -full -sequence $FILE  -sformat1 fasta  "$FILE".patmatmotifs; done"
subprocess.call(prosite_command, shell = True)


