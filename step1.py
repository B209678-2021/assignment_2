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
search_command = "esearch -db protein -query '{0}[Organism] AND {1}[Protein] NOT PARTIAL' | efetch -format fasta > {0}.{1}.fa ".format(questions["taxonomic_group"],questions["protein"])
subprocess.call(search_command, shell = True)



#Limit the number of sequences

#Count the number of sequences present
file = open("{0}.{1}.fa".format(questions["taxonomic_group"],questions["protein"]))
file_contents = file.read()
seq_count = file_contents.count(">")
print(seq_count)


#Clustalo
subprocess.call("clustalo -i {0}.{1}.fa -o {0}.{1}.msf -t protein --outfmt msf -v".format(questions["taxonomic_group"],questions["protein"]), shell = True)




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



