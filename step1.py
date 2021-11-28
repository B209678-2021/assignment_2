#Shebang line
#!/usr/local/bin/python3

#Import Modules
import os, sys, shutil, subprocess, re
print("\nImported os, sys, shutil and subprocess\n")

os.system('clear')

#______________________________________________#

#User entry functions
def user(Protein, Taxonomic_group):
        import string
        print("The following details have been provided:\n\tProtein family: ",Protein, "\n\tTaxonomic_group: ",Taxonomic_group)


#Store output in an ordered Dictionary

#Ask the user to input a protein and taxonomic group
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

#Ask the user if they would like to see how many sequences were downloaded
count = input("Would you like to see how many sequences were downloaded?[YES|NO]\n").upper()

#Print the number of sequences downloaded
if count == "YES":

	#Count the number of sequences present
	file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_contents = file.read()
	seq_count = file_contents.count(">")
	print("The number of sequences downloaded is", seq_count)

#Do not print the number of sequences present
elif count == "NO":
	print("Continuing anyway")

#Any other input
else:
	print("Continuing anyway")

#Number of unique species present
#Ask the user would they like to see the number of unique species retrieved
species = input("Would you like to see the number of unique species retrieved?[YES|NO]\n").upper()

#User answers yes
if species == "YES":
	file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_contents = file.read()
	unique = set(re.findall('\[(.*?)\]',file_contents))
	print(len(unique))

#User answers no
elif species == "NO":
	print("Continuing anyways")

#User answers anything else
else:
	print("Continuing anyways")

#Ask the user if they would like to see the protein count for redundant species
pro_count = input("Would you like to see the protein count for each species?[YES|NO]\n").upper()

#User answers yes
if pro_count=="YES":
	import pandas as pd
	file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_contents = file.read()

	#Seperate sequences into individual sequences
	protein_sequences = file_contents.split(">")

	#Remove the first element because its empty
	protein_sequences.remove(protein_sequences[0])

	#Create an empty list with header lines
	sequence_header = []

	for sequence in protein_sequences:
		sequence_line = sequence.split("\n")
		header_line = sequence_line[0]
		#Only accept it in the format ">accession protein [species name]"
		if "[" in header_line:
			sequence_header.append(header_line)
	#Create a list for the species
	species_list = []
	#Extract the species from the headers
	for header in sequence_header:
		species = header.split("[")[1][:-1]
		species_list.append(species)
	#No. of redundant species and protein count for each
	species_series = pd.Series(species_list)
	species_count = species_series.value_counts()
	print(species_count)

#User answers no
elif pro_count== "NO":
	print("Continuing anyways")

#User answers anything else
else:
	print("Continuing anyways")


#Provide the user with basic sequence info
#Ask the user if they would like to see the basic sequence info
basic_info = input("Would you like to see the basic sequence information for the proteins downloaded?[YES|NO]\n").upper()

#User answers yes
if basic_info == "YES":
	subprocess.call("infoseq {0}.{1}.fa > {0}.{1}.infoseq.fa".format(questions["taxonomic_group"],questions["protein"]), shell = True)
	file_info = open("{0}.{1}.infoseq.fa".format(questions["taxonomic_group"],questions["protein"]))
	file_info_contents = file_info.read()
	print(file_info_contents)	


#User answers no
elif basic_info == "NO":
	print("Continuing anyways")

#User inputs anything else
else:
	print("Continuing anyways")


#Align multiple retrieved sequences using Clustalo
#Ask the user if they would like to align the protein sequences
align = input("Would you like to align the protein sequences?[YES|NO]\n").upper()

#Ask the user how many threads to run clustalo on
no_t = input("How many threads would you like to run clustalo on? Please see manual for guidance: ")
os.environ['no_t'] = no_t

#Run Clustalo
if align == "YES":
	#Run clustalo and change fasta format to msf format for plotcon step
	subprocess.call("clustalo -i {0}.{1}.fa -o {0}.{1}.msf -t protein --outfmt msf --threads=$no_t -v".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#If no, ended session
elif align == "NO":
	print("Session Ended")
	sys.exit()

#If anything else, end session
else:
	print("Session Ended")
	sys.exit

#Give basic alignment information
#Ask the user would they like to see basic alignment information
info_align = input("Would you like to see the basic alignment information?[YES|NO]\n").upper()

if info_align == "YES":
	subprocess.call("infoalign {0}.{1}.fa {0}.{1}.infoalign.fa".format(questions["taxonomic_group"],questions["protein"]), shell = True)
	#Print the output of the infoalign file
	file1 = open("{0}.{1}.infoalign.fa".format(questions["taxonomic_group"],questions["protein"]))
	file1_contents = file1.read()
	print(file1_contents)

#Continue on without doing infoalign
elif info_align == "NO":
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
	subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize $ws -graph ps".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Do not save the plotcon graph and continue on
elif plot == "NO":
	print("Continuing anyways")

#Any other input
else:
	print("Continuing anyways")
	

#Ask the user if they would like to view a conservation plot of the protein sequences
view = input("Would you	like to view a conservation plot of the protein sequences?[YES|NO]\n").upper()

#Show the plotcon graph
if view == "YES":
	subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize $ws -graph x11".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Do not show the plotcon graph
elif view == "NO":
	print("Continuing anyway")

#Any other input
else:
	print("Continuing anyways")

#Scan the PROSITE database
#Split the dataset into individual sequences for patmatmotifs
subprocess.call("seqretsplit {0}.{1}.fa seqoutall".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Run Prosite on all the individual files
#Ask the user would they like to ignore simple patterns
simple = input("Would you like to ignore simple patterns such as post-translational modification sites?[YES|NO]\n").upper()

#Ignore the simple patterns

if simple=="YES":
	prosite_command= 'for file in *.fasta; do patmatmotifs -noprune -sequence $file -sformat1 fasta "$(basename "$file".fasta)".patmatmotifs; done'
	subprocess.call(prosite_command,shell=True)

elif simple=="NO":
	prosite_command= 'for file in *.fasta; do patmatmotifs -norprune -sequence $file -sformat1 fasta "$(basename "$file".fasta)".patmatmotifs; done'
	subprocess.call(prosite_command,shell=True)

else:
	print("Continuing anyways")


#End Session
print("Protein analysis complete. Thank you for your participation")
sys.exit()



