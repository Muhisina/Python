d2=dict(((3,'jithu'),(5,'Nayana'),(2,'Abhitha')))
print({x:d2[x] for x in sorted(d2)})
print({x:d2[x] for x in sorted (d2,reverse=True)})
