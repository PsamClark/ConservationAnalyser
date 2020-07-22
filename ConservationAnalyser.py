""" ConservationAnalyser

	Calculate average conservation of subsequence over multiple 
	aligned DNA or RNA sequences. 
"""

import sys
import numpy as np
from Bio.Seq import Seq
import pandas as pd
from Bio import SeqIO

__author__  = 'Sam Clark <sam.clark@york.ac.uk>'
__license__ = 'MIT'
__version__ = '1.0'

def ConservationAnalyser(seq_file,subseq,start_pos):


    """ Calculate average conservation of subsequence over multiple 
	aligned DNA or RNA sequences. 
    """

    seqs=[]

    #read in sequences
    for rec in SeqIO.parse(seq_file, "fasta"):
	seqs.append(str(rec.seq))

    #determine aalignment mapping of ref sequence
    ref_pos=[i for i in range(len(seqs[0])) if seqs[0][i]!='-']

    #initialise count array		
    rc=[1]*len(subseq)

    #get start and end position
    start=start_pos
    end=start+len(subseq)

    #iterate through sequences	
    for seq in seqs[1:]:
	
	#iterate along subsequence
	for t in range(len(subseq)):

		#get position in ref genome of subsequence position 
		ind=start+t
		
		#find position in aligned genome
		pos=ref_pos[ind]
		
		#if nucleotide in sequence matches tally
		if seq[pos]==seqs[0][pos]:
    			rc[t] += 1

    #get percentage conservation of each position across motif	    
    asc=[rc[i]/(0.01*len(seqs)) for i in range(len(subseq))]
    asc=np.array(asc)

    #calculate average conservation across subsequence
    score=np.mean(asc)

    return score
		
    




