#punctuation.py It removes all the Punctuation symbols
import string 
name='hghhhs $hhhs @hsh !jsj ^jjjs'
word=[x for x in name if x not in string.punctuation]
newword=' '.join(word)
print(newword)

