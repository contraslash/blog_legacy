Title: RC4 y Gzip, no pudiste conmigo
Date: 2016-10-01T02:30:41+00:00
Description: Desencriptando archivos con RC4 y GZip
Tags: Hacking,Open Speech Corpus,Cifrado
---
# RC4 y Gzip, no pudiste conmigoExiste código que es bello por su estética, su funcionalidad o simplemente por el valor sentimental que le agregamos.

Este, por ejemplo hoy tiene alto valor para mi, pues es el fruto del trabajo de un día, donde tuve que decompilar APKs, traducir código de smali a Java, entender el funcionamiento los streams y los buffers de nuevo y finalmente recurrir a una implementación sencilla en pythonde RC4 y GZip
```python
import os
import gzip

encrypted_files_folder = 'assets'
gzipped_files_folder = 'ziped'
decrypted_files_folder = 'decrypted'
key = 'DD15740C-3AE4-4CD1-A117-3F7A990CC74A'


encrypted_files = os.listdir(encrypted_files_folder)

for f in encrypted_files:
	if f.endswith('.txt'):
		encrypted_file = os.path.join(encrypted_files_folder, f)
		zipped_file = os.path.join(gzipped_files_folder, '%s.gz'%(f,))
		out=file(zipped_file,'wb')

		with open (encrypted_file, "rb") as ef:
		    data = ef.read()
		    S = range(256)
		    j = 0

		    for i in range(256):
			j = (j + S[i] + ord(key[i % len(key)])) % 256
			S[i] , S[j] = S[j] , S[i]

		    i = 0
		    j = 0      
		    for char in data:

			i = ( i + 1 ) % 256
			j = ( j + S[i] ) % 256
			S[i] , S[j] = S[j] , S[i]
			out.write(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

		out.close()

		with gzip.open(zipped_file, 'rb') as gzf:
		    decrypted_file = os.path.join(decrypted_files_folder, f)
		    with open(decrypted_file, 'wb') as o:
			for l in gzf:
			    o.write(l)    
```
Todo esto para tener el texto de 26 cuentos de H. P. Lovecraft..

Pronto en Open Speech Corpus