select x.docid,y.docid,sum(x.count*y.count) from Frequency x,Frequency y where x.term==y.term group by x.docid,y.docid;
