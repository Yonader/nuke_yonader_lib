import math
import nuke
class aovsFilter : 
    compo = ["diffuse","sss","transmission","specular","coat","emission","alpha"]
    util = ["N","P","UV","fresnel","motionvector","alpha","depth"]

def aovs_spliter_ui():
    text = """<b><center>AOVS</center></b><hr>
    Enter a aov name <i> eg : spec, transmi, N,...</i><br>
    <b>keys :</b>
    > all <i>- all AOVS</i>
    > util <i>- utilities AOVS (N,P,UV,...)</i>
    > compo <i>- AOVS for compo </i>
    
    """
    #aovs = nuke.getInput(text)
    print ("ok")
    if aovs == None : return

    aovs = aovs.replace(" ","")
    aovs = aovs.split(",")

    aovs_spliter_core (aovs)

def aovs_spliter_core (aov_filters) :
    read = nuke.selectedNode()
    layers = get_layers(read,list(aov_filters))

    if not layers : return
    
    read_xpos = read.xpos()
    read_ypos = read.ypos()
    read_height = read.screenHeight()
    read_width = read.screenWidth()
    offset_y = 50
    new_ypos = int(read_ypos+read_height+offset_y)
    dot_xpos = int(read_xpos+(read_width/2))
    dot = create_dot(d_intput = None, pos = [dot_xpos,new_ypos])
    dot = nuke.toNode([k for k in dot.keys()][0])
    new_ypos += 50

    for i,layer in enumerate(layers):
        shuffle1 = nuke.createNode("Shuffle2")
        shuffle1.setInput(0,dot)
        if i == 0 : 
            new_xpos = read_xpos
        else : 
            new_xpos = read_xpos + (read_width +10)*i
        shuffle1["in1"].setValue(layer)
        shuffle1["in2"].setValue("alpha")
        shuffle1["hide_input"].setValue(True)
        shuffle1["label"].setValue("[value in1]")
        shuffle1["xpos"].setValue(new_xpos)
        shuffle1["ypos"].setValue(new_ypos)

        try : 
            shuffle1["mappings"].setValue('rgba.alpha',"rgba.alpha")
        except: 
            pass


def get_layers(node=None,aov_filters=[""]) : 
    if not node : node = nuke.selectedNode()
    
    node_channels = node.channels()
    node_layers = []
    deny_list =   ["rgba","crypto"]
    remove_items = []

    aov_filters = [aov.lower() for aov in aov_filters]
    
    if "util" in aov_filters : 
        aov_filters = aovsFilter.util
    
    elif "compo" in aov_filters :
        aov_filters = aovsFilter.compo
    
    elif "all" in aov_filters :
        aov_filters.remove("all")
        for filter in aov_filters : 
            deny_list.append(filter)
        aov_filters = [""]

    for aov_filter in aov_filters :
        for c in node_channels :
            if c.find(aov_filter)!=-1 :
                node_layers.append(c.split('.')[0])

    node_layers = sorted(list(set(node_layers)))

    if deny_list :
        for layer in node_layers : 
            for i in deny_list :
                if layer.find(i) != -1 :
                    remove_items.append(layer)
        remove_items = sorted(list(set(remove_items)))
        for item in remove_items : 
            node_layers.remove(item)


    return node_layers


def create_dot(d_intput = None, pos = [0,0]) : 
    d = nuke.createNode("Dot")
    if d_intput :
        d.setInput(0,d_intput)
    if pos != [0,0] : 
        d["xpos"].setValue(pos[0])
        d["ypos"].setValue(pos[1])
    return {d["name"].getValue():[d.xpos(),d.ypos()]}

# aovs_spliter_ui()