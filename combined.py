import os
import shutil
from subprocess import call
from PIL import Image

VALID_IMAGES = [".jpg", ".gif", ".png", ".tga", ".tif", ".bmp"]
valid = []
tlist = []
extra = []
oscr = []
pics=[]
didnt=[]
search_path = input("Enter directory path to search : ")
search_str = input("Enter string to search : ")

if not(search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"

conpath = search_path + "converted-text/"
arch = search_path + "converted-text/" + "Archive/"

if not os.path.exists(conpath):
    os.makedirs(conpath)
if not os.path.exists(arch):
    os.makedirs(arch)

# Making a list of all SCREENSHOTS files ' names without extension part

scrlist = os.listdir(search_path)
scrlist.remove('converted-text')
for x in scrlist:
    if os.path.splitext(x)[1].lower() in VALID_IMAGES and x != "converted-text":
        valid.append(os.path.splitext(x)[0])

conv = os.listdir(search_path + "converted-text/")
conv.remove('Archive')
for y in conv:
    if y != "Archive":
        tlist.append(os.path.splitext(y)[0])

setvalid = set(valid)
ext = ".txt"

for k in conv:
    if os.path.splitext(k)[0] not in setvalid:
        count = 1
        archlist=os.listdir(arch)
        while(k in archlist):
            count=count+1
            k=os.path.splitext(k)[0]+" ("+str(count)+")"+ext
        shutil.move(conpath+k,arch+k)
    
    else :
        for name in scrlist:
            kk= os.path.splitext(k)[0]
            if kk == os.path.splitext(name)[0]:
                extra.append(name)

oscr=[x for x in scrlist if x not in extra]

for d in oscr:
    if os.path.splitext(d)[1] in VALID_IMAGES:
        try:
            call(["tesseract", search_path + d, conpath + os.path.splitext(d)[0]])
        except:
            didnt.append(d)

if len(didnt)>0:
    print("Couldn't read these images :\n")
    for dn in didnt:
        print(dn+"\n")
    print("\n")

for fname in conv:
    fo = open(conpath + fname)
    line = fo.readline()
    line_no = 1
    while line != '':
        index = line.find(search_str)
        if (index != -1):
            print(fname, "[line no.->", line_no, ",index->", index, "] ", line, sep = "")
            pics.append(os.path.splitext(fname)[0])
        line = fo.readline()
        line_no += 1
    fo.close

if(len(pics))<2:
    for ii in scrlist:
        if pics[0] == os.path.splitext(ii)[0]:
            img= Image.open(search_path+ii)
            img.show()
            
