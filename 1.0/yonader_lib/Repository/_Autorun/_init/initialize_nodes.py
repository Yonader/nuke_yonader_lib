
import nuke
import nukescripts
import os


# Time Offset Label Modification

def OnTimeOffsetCreate():
     timeOffsetNode = nuke.thisNode()
     if timeOffsetNode != None:
          label = timeOffsetNode['label'].value()
          timeOffsetNode['label'].setValue('[value time_offset]\n'+label)

# Tracker Label Modification

def OnTrackerCreate():
     trackerNode = nuke.thisNode()
     if trackerNode != None:
          label = trackerNode['label'].value()
          trackerNode['label'].setValue('Motion: [value transform]\nRef Frame: [value reference_frame]\n' + label)

          

# Shuffle Label Modification

def OnShuffleCreate():
     shuffleNode = nuke.thisNode()
     if shuffleNode != None:
          label = shuffleNode['label'].value()
          shuffleNode['label'].setValue('[value in]\n' + label)
          shuffleNode['postage_stamp'].setValue(False)
    

# Read Modification

def OnReadCreate():
     readNode = nuke.thisNode()
     if readNode != None:
          label = readNode['label'].value()
          readNode['label'].setValue('[value width]x[value height]\n[value first_frame] - [value last_frame]\n'+label)
          readNodeNewTileColor = int('%02x%02x%02x%02x' % (0,191,255,255),16)
          readNode['tile_color'].setValue(readNodeNewTileColor)
          

# Switch Modification

def OnSwitchCreate():
     switchNode = nuke.thisNode()
     if switchNode != None:
          label = switchNode['label'].value()
          switchNode['label'].setValue('[value which]')

          switchNodeNewTileColor = int(0x22b300ff)
          switchNode['tile_color'].setValue(switchNodeNewTileColor)
 

def switchChangeColor():
     n = nuke.thisNode()
     k = nuke.thisKnob()
     if k.name() == 'which':
          colors = [582156543,3003121919]
          try:
               n.knob('tile_color').setValue( colors[ int( n.knob('which').value() ) ] )
          except:
               pass

def OnFrameHoldCreate():
     frameHoldNode = nuke.thisNode()
     if frameHoldNode != None:
          frameHoldNode['first_frame'].setValue(nuke.frame())
 
def OnRetimeCreate():
     label = "[value output.first] - [value output.last]"
     node = nuke.thisNode()
     if node : 
          node["label"].setValue(label)

def OnTimeClipCreate():
     label = "[value first] - [value last]"
     node = nuke.thisNode()
     if node : 
          node["label"].setValue(label)

def OnAppendClipCreate():
     label = "[value firstFrame] - [value lastFrame]"
     node = nuke.thisNode()
     if node : 
          node["label"].setValue(label)

def OnTransformCreate():
     transform = nuke.thisNode()
     if transform != None:
          tabUtilities_name = "tabUtilities"
          if not tabUtilities_name in transform.knobs().keys()  :
               # BUTTON CENTER PIVOT : 
               cmd_pyButtonCenterPivot = """
node = nuke.thisNode()
print (node['name'].value(), " Center pivot : ")
nodeCenterWidth = int( nuke.tcl("value width") ) /2
nodeCenterHeight = int( nuke.tcl("value height") )/2
nodeNewCenter= [nodeCenterWidth,nodeCenterHeight]
node["center"].setValue(nodeNewCenter)
print ("\tNew pivot ( x =", nodeNewCenter[0] , "; y =" , nodeNewCenter[1] ,")")
               """
               add_pyButtonCenterPivot = nuke.PyScript_Knob("pyButtonCenterPivot","Center Pivot",cmd_pyButtonCenterPivot)
               add_pyButtonCenterPivot.setTooltip("center pivot = center pivot, what else ?.")
               add_pyButtonCenterPivot.setFlag(nuke.STARTLINE)

               # BUTTON LINKE CENTER TO FORMAT
               cmd_pyButtonLinkToFormat = """
node = nuke.thisNode()
nodeCenterWidth = 'input.width/2'
nodeCenterHeight = 'input.height/2'
node["center"].setExpression(nodeCenterWidth,0)
node["center"].setExpression(nodeCenterHeight,1)
               """
               add_pyButtonLinkToFormat = nuke.PyScript_Knob("pyButtonLinkToForma","Link Center to format",cmd_pyButtonLinkToFormat)
               add_pyButtonLinkToFormat.setTooltip("center y = input.height/2\ncenter x = input.width/2")
               add_pyButtonLinkToFormat.setFlag(nuke.STARTLINE)
               #Add Buttons
               add_tabUtilities = nuke.Tab_Knob(tabUtilities_name, 'Utilities')
               transform.addKnob(add_tabUtilities)
               transform.addKnob(add_pyButtonCenterPivot)
               transform.addKnob(add_pyButtonLinkToFormat)


          
# Customize nodes

nuke.addOnUserCreate(OnTimeOffsetCreate, nodeClass="TimeOffset")
nuke.addOnUserCreate(OnTrackerCreate, nodeClass="Tracker4")
nuke.addOnUserCreate(OnShuffleCreate, nodeClass="Shuffle")
nuke.addOnUserCreate(OnShuffleCreate, nodeClass="Shuffle2")
nuke.addOnUserCreate(OnReadCreate, nodeClass="Read")
nuke.addOnUserCreate(OnSwitchCreate, nodeClass="Switch")
nuke.addKnobChanged(switchChangeColor,nodeClass="Switch")
nuke.addOnUserCreate(OnTransformCreate, nodeClass="Transform")
nuke.addOnUserCreate(OnRetimeCreate, nodeClass="Retime")
nuke.addOnUserCreate(OnTimeClipCreate, nodeClass="TimeClip")
nuke.addOnUserCreate(OnAppendClipCreate, nodeClass="AppendClip")
#Change default knob Setting

nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")


