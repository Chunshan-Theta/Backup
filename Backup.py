import os,sys,logging,platform




def CopyFile(SourceDir,FileName,SaveDir):
	logging.basicConfig(level=logging.CRITICAL)#INFO,WORRING,ERROR,CRITICAL

	#if(getattr(sys, "getwindowsversion", None)):
	#    logging.info("Windows version   : %s", sys.getwindowsversion())
	 
	logging.info("Your OS is : %s", platform.system())
	OS = platform.system()

	if OS == "Linux":
		try:
			#cheak dir exists
			if not os.path.exists(SaveDir):
	    			os.makedirs(SaveDir)
			#copy file
			import shutil

			filename1 = os.path.join(SourceDir, FileName)
			filename2 = os.path.join(SaveDir, FileName)

			print filename1, "=>", filename2
	

			shutil.copy2(filename1,filename2)

			if os.path.isfile (filename2): print "Success"
		except:
			logging.warning("Unexpected error:"+str(sys.exc_info()))
			

	if OS == "Windows":
		try:
			#cheak dir exists
			if not os.path.exists(SaveDir):
	    			os.makedirs(SaveDir)
			#copy file
			import shutil

			filename1 = os.path.join(SourceDir, FileName)
			filename2 = os.path.join(SaveDir, FileName)

			print filename1, "=>", filename2
	

			shutil.copy2(filename1,filename2)

			if os.path.isfile (filename2): print "Success"
		except:
			logging.warning("Unexpected error:"+str(sys.exc_info()))



## main thread

FileType = raw_input('File Type you want to back-up: ')#py
StartPoint = raw_input('Which is the file that you want to start searching: ')#/var/..../
BackupPoint = raw_input('where that you want to save copy: ')#/var/..../

#search all subfile
for dirPath, dirNames, fileNames in os.walk(StartPoint or "./"):
    #print dirPath
    for f in fileNames:
        #print os.path.join(dirPath, f)
	if f[f.find(".")+1:]==FileType:
		print os.path.join(dirPath, f)
		CopyFile(dirPath,f,BackupPoint or "./")
	pass

print("close program after 10s")
time.sleep(5)
print("close program after 5s")
time.sleep(5)

