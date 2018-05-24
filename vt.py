#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import os
import stat
import sys
import re

'''
    一键修改王者荣耀优化为V.T，需要root
'''




if(__name__ == "__main__"):
    #print(os.getuid())

    
    '''
    if os.getuid():
        args = [sys.executable] + sys.argv
        os.execlp('su','su','-c',''.join(args))
        
    #print(open("/data/data/com.tencent.tmgp.sgame"))
    #os.chmod("/data/data/com.tencent.tmgp.sgame/shared_prefs",stat.S_IXUSR+stat.S_IRUSR+stat.S_IRGRP+stat.S_IXGRP+stat.S_IXOTH)
    #f = open("/data/data/com.tencent.tmgp.sgame/shared_prefs/com.tencent.tmgp.sgame.v2.playerprefs.xml","r+")
    '''
    f = open("D:/com.tencent.tmgp.sgame.v2.playerprefs.xml","r+")
    
    
    
    flist = f.readlines()

    for i in range(len(flist)):
        
        EnableGLES3 = re.search(r'<int name="EnableGLES3" value="(.)" />',flist[i])
        if EnableGLES3:
            flist[i] = flist[i].replace("value=" + EnableGLES3.group(1),'value="3')

        EnableVulkan = re.search(r'<int name="EnableVulkan" value="(.)" />',flist[i])
        if EnableVulkan:
            flist[i] = flist[i].replace("value=" + EnableVulkan.group(1),'value="2')

        EnableMTR = re.search(r'<int name="EnableMTR" value="(.)" />',flist[i])
        if EnableMTR:
            flist[i] = flist[i].replace("value=" + EnableMTR.group(1),'value="1')
    
    
    print ("".join(flist))



    
    f.close()


















