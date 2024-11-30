import os
import nuke
import shutil
import os
import nuke
def backupRead():
    read = nuke.selectedNode()
    source = read["file"].value()
    basefile = source.split(root)[-1]
    project = basefile.split("/",2)[1]
    file = "/".join(basefile.split("/")[2:-1])
    archivefile = "/".join([root,project,archive,file])
    source = os.path.dirname(source)
    askResult = nuke.ask(f"Backup for {read['name'].value()}\nSource: \n{source}\nDesti: \n{archivefile} \n? ")
    if not askResult : return
    if os.path.exists(archivefile): 
        nuke.message(f"Not copy {archivefile}")
        return
    shutil.copytree(source,archivefile,ignore_dangling_symlinks=True)
    nuke.message("\n"+read["name"].value()+" ARCHIVED")

backupRead()