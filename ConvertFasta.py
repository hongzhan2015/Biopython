from Bio.Seq import Seq
from Bio import SeqIO

class alignmentFasta:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def convert(self):
        record=SeqIO.parse(self.name, self.type)
        OutPut_name=' '.join([self.name,'.clustal'])
        count = SeqIO.write(record, OutPut_name, "clustal")
        #print("Converted $i records" % count)
        
        
test1 = alignmentFasta("aligned.fasta","fasta")
test1.convert()
