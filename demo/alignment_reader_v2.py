import sys
import numpy as np
from Bio.Seq import Seq
import pandas as pd
from Bio import SeqIO

if __name__ == '__main__':

    from ConservationAnalyser import ConservationAnalyser 

    #load motifs to analyse conservation
    motifs=pd.read_csv('URRUXXXXXXXXURRU_mc.csv')


    #read through motifs
    for k in range(len(motifs)):
	
        #print average conservation across motif
	print ConservationAnalyser("merbeco_neighbours_27_5_10_aligned_mers_on_top.fasta",motifs['seq'][k],motifs['# position'][k])
	


