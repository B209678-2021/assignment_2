ç#Shebang line
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

sequence_full = input("Do you want partial sequences?[YES|NO\n").upper()

if sequence_full == "YES":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein]' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)
elif sequence_full == "NO":
        search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein] NOT PARTIAL' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
        subprocess.call(search_command, shell = True)
else:
     	sys.exit()

#Limit the number of sequences

#Count the number of sequences present
file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
file_contents = file.read()
seq_count = file_contents.count(">")
print(seq_count)


#Clustalo
subprocess.call("clustalo -i {0}.{1}.fa -o {0}.{1}.msf -t protein --outfmt msf -v".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Plotcon
#Plot the protein conservation and save the graph
subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize 4 -graph ps".format(questions["taxonomic_group"],questions["protein"]), shell = True)

#Plot the protein conservation and save	the graph
subprocess.call("plotcon -sformat msf {0}.{1}.msf -winsize 4 -graph x11".format(questions["taxonomic_group"],questions["protein"]), shell = True)



#Split all the proteins into individual sequences
subprocess("seqretsplit {0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]), shell = True) 




#Scan the PROSITE database 

#Run prosextract first
#prosextract -prositedir directory
#Prosite files located 
/localdisk/software.local/EMBOSS-6.6.0/share/EMBOSS/data/PROSITE/


#Run patmatmotifs next

#Sequences need to be entered individually 
#



