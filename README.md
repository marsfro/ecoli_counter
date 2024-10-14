# *Escherichia coli* Phylogroups K-mers Counter

This script counts the relative abundance of *Escherichia coli* phylogroups in metagenomic data by analyzing presence of E.coli k-mers in fastq files. It processes *E. coli* phylogroup-specific k-mers stored **ecoli_unique_kmers** directory and outputs the results in a CSV format.

## Features

- **Phylogroup detection**: Identifies and counts specific k-mers associated with various *E. coli* phylogroups.
- **Flexible input**: Supports multiple fastq files for processing.
- **Log tracking**: Provides detailed execution logs for easy troubleshooting.
- **Normalization**: Outputs normalized relative abundance percentages for each phylogroup.

## Requirements

- Python 3.11
- Biopython library
- Pandas library

## Installation

1.  Clone the repository:
```bash
   git clone https://github.com/marsfro/ecoli_counter.git
```

2. Install the required Python libraries if you haven't already:

   ```bash
   pip install biopython pandas
   ``` 

## Usage

```bash
python ecoli_kmer_counter.py -i <input_fastq_directory> -o <output_csv_file> -k <kmers_directory> -l <log_file_path>
```

#### Parameters
**-i**, **--input**: Path to the directory containing the metagenome fastq files.
**-o**, **--output**: Path to the output CSV file where the results will be saved.
**-k**, **--kmers**: Path to the directory containing the E. coli phylogroup-specific k-mer files.
**-l**, **--log**: Path to the log file to track script execution (default is "log_file.txt").

## Example

```bash
python ecoli_kmer_counter.py -i ./fastq -o output.csv -k ./ecoli_unique_kmers 
``` 

## Output
The script generates a CSV file with the following columns:

- Phylogroups: Names of the E. coli phylogroups.
- number_kmers: The number of k-mers identified for each phylogroup.
- The number of k-mers found for each phylogroup.
- The percentage of k-mers relative to the total number of k-mers for each phylogroup.

## Citing This Script

If you use this script in your research, please cite the following article:

 - Title of the article



