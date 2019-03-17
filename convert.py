
# importing required modules
#  import PyPDF2
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
#list is the list of ALL the skills that the recruiter wants to check for
def read(lis):
    #list(lis)
    #print("in read")
    #print((lis))
    #print(lis[0][0])
    #lis=list(lis)

    field=[]
    for i in range(len(lis)):
        field.append(str(lis[i][1]))

    print (field)
    #print(lis[0])
    skills=[]
    skills.append(field[1])
    skills.append(field[2])
    print(skills)
    count =0
    hit=0
    x=pageObj.extractText()
    y=(x.split("\n"))
    z=[str(i) for i in y]

    f= ("".join(z).split())
    print(f,"\n")

    synonyms = []
    #compiles all the syn of all words in passes list
    for num in range(len(skills)):
        word=skills[num]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
    #convers to comparable string
    for i in range(len(synonyms)):
        synonyms[i]=str(synonyms[i])
        synonyms[i]=(synonyms[i]).lower()
        #count+=1

    #print((synonyms))
    synonyms=Remove(synonyms)
    print((synonyms))
    count=len(synonyms)
        #checks total number of hits in resume
    for num in range(len(synonyms)):
        word=synonyms[num]
        for num2 in range(len(f)):
            if word.lower()==f[num2].lower():
                hit+=1

    percent=(float(hit)/float(count))*100.00
    print(hit, count)
    print(percent,"%")




    # closing the pdf file object
    pdfFileObj.close()
    return


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#list=['tech','leadership','Java','C++']
#read(list)
