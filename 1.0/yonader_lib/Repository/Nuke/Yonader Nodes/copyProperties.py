def copyProperties() : 
    nodes = nuke.selectedNodes()
    # ref_node = nodes[-1]
    ref_node = nodes.pop(-1)
    deniKnobs = ["name","help","onCreate","onDestroy","knobChanged","updateUI","autolabel","panel","label","selected","xpos","ypos","icon","indicators","cached","lifetimeStart","lifetimeEnd","useLifetime","postage_stamp","postage_stamp_frame","dope_sheet","bookmark","rootNodeUpdated",""]
    user_knobs = nuke.getInput("knob name")
    if user_knobs == None : return
    user_knobs = user_knobs.replace(" ","")
    user_knobs = user_knobs.split(",")
    needKnobs = []
    if user_knobs != [""] : 
        needKnobs = user_knobs
    copy_knob = []

    print (ref_node["name"].value())
    for node in nodes : 
        if node.Class() == ref_node.Class(): 
            for knob in ref_node.knobs():
                if needKnobs:
                    if (not knob in deniKnobs) and (knob in needKnobs) :
                        copy_knob.append(knob)
                else : 
                    if (not knob in deniKnobs) : 
                        copy_knob.append(knob)
        
            print (f"Copy ref node {ref_node.name()} to node {node.name()}")
            for knob in copy_knob :
                print (f"Copy {knob} ")
                node[knob].setValue(ref_node[knob].value())
                print (knob)
    print (f"{len(copy_knob)} knobs copied")

    del nodes, ref_node, needKnobs, copy_knob, user_knobs, deniKnobs

copyProperties()
