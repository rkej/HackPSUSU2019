
# importing required modules
import PyPDF2
from nltk.corpus import wordnet

# creating a pdf file object
pdfFileObj = open('resume.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
#print(pageObj.extractText())

x=pageObj.extractText()
#print(x)
#print(type(x))
y=(x.split("\n"))
z=[str(i) for i in y]

#z=y.split("\n")
#y=[str(i) for i in x]

f= ("".join(z).split())

print(f,"\n")


synonyms = []

#print(f[0])

for word in f:
    print word

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    #print(len(synonyms))

    for i in range(len(synonyms)):
        synonyms[i]=str(synonyms[i])

    print((synonyms))
    

# closing the pdf file object
pdfFileObj.close()
