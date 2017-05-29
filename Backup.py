import os,sys,logging,platform,time




def CopyFile(SourceDir,FileName,SaveDir):
	logging.basicConfig(level=logging.CRITICAL)#INFO,WORRING,ERROR,CRITICAL


	try:
		
		#copy file
		import shutil
		
		filename1 = os.path.join(SourceDir, FileName)
		filename2 = os.path.join(SaveDir, FileName)

		print filename1, "=>", filename2


		shutil.copy2(filename1,filename2)

		if os.path.isfile (filename2): print "Success"
		
		Text = filename1+"=>"+filename2
		w = open(os.path.join(SaveDir, "CopyNote.txt"),'a')
		w.writelines(Text+"\n")
		w.close()
	except:
		logging.warning("Unexpected error:"+str(sys.exc_info()))
			





## main thread
print "e.g. txt"
FileType = raw_input('File Type you want to back-up: ')#py
print "e.g. C:\Users\Theta\Desktop"
StartPoint = raw_input('Which is the file that you want to start searching: ')#/var/..../
print "e.g. C:\Users\Theta\Desktop\NEW"
BackupPoint = raw_input('where that you want to save copy: ')#/var/..../

#cheak dir exists
if not os.path.exists(BackupPoint):
    os.makedirs(BackupPoint)
#create note to record copy process
w = open(os.path.join(BackupPoint, "CopyNote.txt"),'w')
w.close()


#search all subfile
for dirPath, dirNames, fileNames in os.walk(StartPoint or "./"):
    #print dirPath
    for f in fileNames:
        #print os.path.join(dirPath, f)
	if f[f.find(".")+1:]==FileType:
		print os.path.join(dirPath, f)
		CopyFile(dirPath,f,BackupPoint)
	pass

print("close program after 10s")
time.sleep(5)
print("close program after 5s")
time.sleep(5)


