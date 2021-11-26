#Shebang line
#!/usr/local/bin/python3

#Import Modules
import os, sys, shutil, subprocess
print("\nImported os, sys, shutil and subprocess\n")

os.system('clear')

#______________________________________________#

#User entry functions
def user_entry(protein, taxonomic_group):
        import string
        print("The following details have been provided:\n\tProtein family: ",protein, "\n\tTaxonomic_group: ",taxonomic_group)


#Store output in an ordered Dictionary

questions ={}
questions["protein"] = input("Please enter protein family:\n")
questions["taxonomic_group"] = input("Please enter taxonomic group:\n")

protein = questions["protein"]
taxonomic_group = questions["taxonomic_group"]
user_entry(*list(questions.values()))

#os.environ["protein"] = protein
#os.environ["taxonomic_group"] = taxonomic_group
#Retrieve the sequences using Esearch and Efetch from EDirect
command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein] NOT PARTIAL' | efetch -db protein -format fasta > {0}.search.fasta ".format(questions["taxonomic"],questions["protein"])
subprocess.call(command, shell = True)



#Limit the number of sequences





#Align multiple sequences in clustalo
#Convert from fasta to msf format for the plotcon step
#clustalo_command = r'clustalo -i help.fa -o glu.align.msf -t4  protein --outfmt msf -v'
#subprocess.call(clustalo_command, shell=True)

#clustalo -i help.fa -o glu.align.msf -t4  protein --outfmt msf -v


#Make a plotcon 
#Ps saves graph
#x11 prints to the screen
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



