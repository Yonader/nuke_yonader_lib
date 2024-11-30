def ptitDotter() : 
    import math

    offset = nuke.getInput("<b>OFFSET</b><br><i>Integer needed (0=center)")
    if offset == None : return
    if offset == "": 
        offset = int(0)
    try: 
        offset = int(offset)
    except:
        nuke.critical("Integer needed for offset ! ")
        return
    
    nodes = nuke.selectedNodes()
    if not nodes :
        nuke.critical("Nothing selected")
        return

    fuckingClasses = ["Merge","Copy"]
    is_fuckingClass = False
    dot_size = nuke.toNode('preferences')['dot_node_scale'].getValue()
    
    for node in nodes :
        #node["selected"].setValue(False)
        node_x = node["xpos"].getValue()
        node_y = node["ypos"].getValue()
        j = None
        for i,child in enumerate(node.dependencies()) : 

            dot = nuke.createNode("Dot", inpanel = False)
            dot["selected"].setValue(False)
            dot.setInput(0,child)
            for fuckingClass in fuckingClasses : 
                if node.Class().find(fuckingClass) is not -1 : 
                    is_fuckingClass = True

            if is_fuckingClass :
                if i == 2 and not node.input(2) :
                    j = i+1 
                    node.setInput(j,dot)            
                else : 
                    if j : 
                        node.setInput(j,dot)
                    else : 
                        node.setInput(i,dot)
            else: 
                node.setInput(i,dot) 


            child_x = int(child["xpos"].getValue()+ (child.screenWidth()*.5))
            child_y = int(child["ypos"].getValue()+ child.screenHeight())
            child.setXpos(int(child["xpos"].getValue()))

            dot_xpos = child_x - dot.screenWidth() * .5
            dot.setXpos(int(dot_xpos))

            if offset == 0 : 
                dot_ypos =  child_y + ((node_y - child_y ) *.5)
            else : 
                dot_ypos = child_y + offset*10
            
            dot["ypos"].setValue(int(dot_ypos))
            del dot
    
    for node in nodes :
        node["selected"].setValue(True)
ptitDotter()



