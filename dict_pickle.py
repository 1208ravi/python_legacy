import pickle
data={'ravi':1,'subbu':2,'chinna':3}
f=open('data.p','w')
pickle.dump(data,f)
f.close()