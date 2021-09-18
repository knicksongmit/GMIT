f = open ('moby-dick.txt', 'r')
moby = f.read ()
f.close ()

freq = moby.count ('e')
print (freq)