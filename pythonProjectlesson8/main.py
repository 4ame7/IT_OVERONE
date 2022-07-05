Fin = open ( "input.txt" )
Fout = open ( "output.txt", "w" )
while True:
    s = Fin.readline()
    if not s: break
    age = int ( s.split()[1] )
    if age < 5:
        Fout.write ( s )
        Fin.close()
        Fout.close()
