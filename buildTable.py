def getVerb():
    global irrvListf
    global llist

    irrvDataf.write('new verbData(\n')

    for i in range(9):
        st=verbsf.readline()
        if st=="":
            print ("End of File reached unexpectadly!")
            print ("End of File reached unexpectadly!")
            print ("End of File reached unexpectadly!")
            exit()
        if (i==0):
            theVerb=st.split()[0]
            irrvListf.write(repr(theVerb)+',\n')
            print (theVerb)
            comma=''
        tst=st.split()
        irrvDataf.write(comma+str(tst)+'\n')
        comma=","
#
#   End of verb
    irrvDataf.write('),\n')        

def closeirrvListfile():
    irrvListf.write('    ];\n')
    irrvListf.close()

def closeIrrvDataFile():
    irrvDataf.write('    ];\n')
    irrvDataf.close()

verbs="verbs.txt"
verbsf = open(verbs, "r")
irrv="irregularVerbsList.js"
irrvListf= open(irrv, "w")
irrvData="irregularVerbsData.js"
irrvDataf= open(irrvData, "w")
irrvListf.write('const    irregularVerbs = ['+'\n')

irrvDataf.write('irregularVerbsData = ['+'\n')

while True: 
    # Search for ">>" for beginning of verb
    st=verbsf.readline()
    if st=="":
        closeirrvListfile()
        closeIrrvDataFile()
        print ("End of File reached")
        exit()
    if st.startswith(">>>>"):
        getVerb()
