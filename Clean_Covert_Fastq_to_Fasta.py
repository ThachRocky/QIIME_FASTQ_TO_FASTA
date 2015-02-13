#convert fastq to fasta


#!/usr/bin/python
import sys
import os
from Bio import SeqIO


"""
author : Thach Bui
Clean and convert Fastq with high qual reads to Fasta format
Executable format  in cmd:

python Clean_Convert_Fastq_to_Fasta.py <fastq_file> <new_name.fasta>

"""

# Get inputs:

#get fastq path
fq_path = sys.argv[1]

#get fasta path
fa_path = sys.argv[2]


fa_in = open (fa_path, 'w')
 
# Get fastq cleans and saves to fasta file

for record in SeqIO.parse(fq_path, "fastq"):
        header = record.id .replace(".","_")
        fa_in.write (">%s \n"%header)
        fa_in.write ("%s\n"%record.seq)

fa_in.close()

#end

    


        
