#Shebang line
#!/usr/local/bin/python3

#Import Modules 
import os, sys, shutil, subprocess

#User entry functions 
def user(Protein, Taxonomic_group):
	import string 
	print("The following details have been provided:\n\tProtein family: ",Protein, "\n\tTaxonomic_group: ",Taxonomic_group)
	for character in protein:
		if character not in string.ascii_letters: 
			return print("\nInvalid entry: re-enter protein family name please")
		if character not in string.ascii_letters:	
			return print("\nInvalid entry")

#Store output in an ordered Dictionary

questions ={}
questions["protein_family"] = input("Please enter protein family:\n")
questions["taxonomic_group"] = input("Please enter taxonomic group:\n")

#Combine protein family and taxonomic group
user(*list(questions.values()))
print("\n\nComplete\n\n")

#retrieve the sequences
command = "esearch -db protein -query "{1}[Organism] AND {0}[Protein name] NOT PARTIAL' | efetch -db protein -format fasta ".

#Run in the command bash
subprocess(command, shell = True)

#Limit the number of sequences


#Align multiple sequences in clustalo 
#clustalo_command = r'clustalo -i protein.fa -o protein.msf -t4'
#subprocess.call(clustalo_command, shell=True)

clustalo -i help.fa -o glu.align.msf -t4  protein --outfmt msf -v


#Make a plotcon
#plotcon -sformat msf glu.align.msf -winsize 10 -graph ps
#plotcon -sformat msf glu.align.msf -winsize 10 -graph x11



#Scan the PROSITE database 

#Run prosextract first
#prosextract -prositedir directory
#Prosite files located 
/localdisk/software.local/EMBOSS-6.6.0/share/EMBOSS/data/PROSITE/


#Run patmatmotifs next

#Sequences need to be entered individually 
#



