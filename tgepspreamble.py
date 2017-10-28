import codecs

fin = codecs.open('tgepspreamble.eps', 'r', 'utf_8')
fout = codecs.open('tgepspreamble.sty', 'w', 'utf_8')
writable = False
for str in fin:
	if writable:
		str = str.strip(' \t\n')
		if len(str) > 0 and str[0] != '%':
			idx = str.find('%')
			idx = None if  idx == -1 else idx
			str = str[0 : idx]
			str = str.replace('{', '\\@charlb ')
			str = str.replace('}', '\\@charrb ')
			fout.write('\\immediate\\write\\tg@epsfile{' + str + '}%\n')
		elif str == '% endinput':
			fout.write('}\n')
			break
	elif str == '% begininput\n':
		fout.write('\\def\\tg@epspreamble{%\n')
		writable = True
fin.close()
fout.close()
print("abgeschlossen")
