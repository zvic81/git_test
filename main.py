mfile = open('self-test.txt', 'r')
sfile=open('copy.txt','w')
sfile.write(mfile.read())

'''
коментарий
test comennt
арара

мчсмч


'''
mfile.close()
sfile.close()
mfile = open('self-test.txt', 'r')
sfile=open('copy.txt','r')
mas1=mfile.read()
mas2=sfile.read()
print(str(len(mas1)),str(len(mas2)))

mfile.close()
sfile.close()