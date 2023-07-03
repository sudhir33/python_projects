import PyPDF2
import re
import csv
certid=[]
roll=[]
college=[]
branch=[]
with open("java.csv")as f1:
    dd=list(csv.reader(f1))
    for d in dd[1:]:
        roll.append(d[0])
        certid.append(d[-3])
        college.append(d[4])
    #print(*certid)



reader = PyPDF2.PdfReader("java.pdf")

num_pages = len(reader.pages)


for d in range(len(roll)):
    i=0
    #print(roll[d])
    for page in reader.pages:
        text = page.extract_text()
        ids=list(certid[d])
        ids=' '.join(ids)
        #res_search = re.search(ids, text)
        res_search = re.search(certid[d], text)
        #print(text)
        if res_search:
            #print(roll[d])
            output = PyPDF2.PdfWriter()
            output.add_page(reader.pages[i])
            with open("java/"+roll[d]+".pdf", "wb") as outputStream:
                output.write(outputStream)
            break
        i+=1
    else:
        print("Not Found",roll[d])
    

