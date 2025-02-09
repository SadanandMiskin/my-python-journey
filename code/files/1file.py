f=open('/home/sads/Desktop/data-science/book.txt' , 'r')
f_out=open('/home/sads/Desktop/data-science/out.txt' , 'w')


for line in f:
  tokens = line.split(' ')
  f_out.write(str(len(tokens)) + " " + line+ " " )



f.close()
f_out.close()