import os
import nuke
def checkArchive () : 
    reads = nuke.allNodes("Read")

    archive = "ARCHIVES_COMPOSITING"

    reads = [read for read in reads if read["disable"].value() == 0]
    root = "//192.168.131.2/ds_projects"
    recupReads = []
    for read in reads : 
        basefile = read["file"].value()
        basefile = basefile.split(root)[-1]
        project = basefile.split("/",2)[1]
        file = "/".join(basefile.split("/")[2:-1])
        archivefile = "/".join([root,project,archive,file])
        #print("basefile",basefile, "project",project,"file",file,"archivefile",archivefile)
        if not os.path.exists(archivefile) : 
            recupReads.append(read["name"].value())
            print ("\n"+archivefile )
            print (read["name"].value(),read["file"].getValue())
            pass
    recupReads = sorted(recupReads)
    print (recupReads)
    # nuke.message(recupReads)
    pass
checkArchive()