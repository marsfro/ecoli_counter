import argparse
import os
import glob
import pandas as pd
import datetime
from Bio import SeqIO

# Creating a command line argument parser
parser = argparse.ArgumentParser(description='Script for counting relative abandance of E.coli phylogroups.')
parser.add_argument('-i', '--input', help='The metagenome fastq file')
parser.add_argument('-o', '--output', help='The output file in csv format.')
parser.add_argument('-k', '--kmers', help='The E.coli phylogroup kmers folder path.')
parser.add_argument('-l', '--log', help='The log file path.')

# Getting command line arguments
args = parser.parse_args()
path_fastq = args.input
output_file = args.output
path_kmers = args.kmers
log_file = "log_file.txt"

# Creating a log file
try:
    with open(log_file, "w") as f:
        f.write(f"Script execution started at: {datetime.datetime.now()}\n")
except Exception as e:
    print(f"An error occurred while creating the log file: {str(e)}")
    exit(1)

try:
    # Checking existence of input file
    #if not os.path.isfile(path_fastq):
    #    raise FileNotFoundError(f"Input file {snp_file} not found.")
    
    folder_files = glob.glob(path_kmers + '/*')

    # create dictionary with name of phylogroups and kmers
    group_kmers = {}
    for file in folder_files:
        #get name of phylogroup from file name
        file_name = os.path.splitext(os.path.basename(file))[0]
        #open txt files with kmers as set
        kmer_set =  set(open(file).read().split())
        #create dictionary
        group_kmers[file_name] = kmer_set
        print(file_name)

    # get dictionary with numbers of kmers

    num_kmers = {}
    for group in group_kmers.keys():
        num_kmers[group] = len(group_kmers[group])
        print(group, len(group_kmers[group]))

    num_kmers = dict(sorted(num_kmers.items()))
    print(num_kmers)

    sample_df = pd.DataFrame()
    sample_df['Phylogroups'] = num_kmers.keys()
    sample_df['number_kmers'] = num_kmers.values()

    for fastq in glob.glob(path_fastq + '/*.fastq'):
        print(fastq)
        sample_name = os.path.splitext(os.path.basename(fastq))[0]
        
        len_fastq = 0
        freqMap = {'A': 0, 'B1': 0, 'B2': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
        for seq_parse in SeqIO.parse(fastq, "fastq"):
            len_fastq += 1
            seq2kmers = set()
            sequence = str(seq_parse.seq)
            #transform read to kmers set
            for i in range(len(sequence)-18+1):
                kmer = sequence[i:i+18]
                seq2kmers.add(kmer)
                
            #counter for reads
            for group in group_kmers.keys():
                entry = seq2kmers.intersection(group_kmers[group])
                if len(entry) > 0:
                    freqMap[group] = freqMap[group] + 1
        print(freqMap)    
        sample_df[f'{sample_name}'+' kmers'] = freqMap.values()  
        print(sample_name)
        #normalization of counts
        norm = {}
        for key in freqMap.keys():
            print(freqMap[key]* 100000000/len_fastq/num_kmers[key])
            norm[key] = freqMap[key]* 100000000/len_fastq/num_kmers[key]
        print(len_fastq)
        #sample_df[f'{sample_name}'+'_group'] = norm.keys()
        #sample_df[sample_name] = norm.values() 
        sample_df[f'{sample_name}'+' %'] = norm.values() 
    
    sample_df.to_csv(output_file, index=False)
    

    with open(log_file, "a") as f:
        f.write(f"Script execution completed successfully at: {datetime.datetime.now()}\n")
   
    print('Done')
    
except Exception as e:
    with open(log_file, "a") as f:
        f.write(f"An error occurred during script execution: {str(e)}\n")