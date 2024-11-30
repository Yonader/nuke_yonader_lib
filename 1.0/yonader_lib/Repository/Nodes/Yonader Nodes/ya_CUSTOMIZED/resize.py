#____FONCTIONS____#
#_QUESTION
def askCreateFormat():
     askCF = nuke.ask("Create new format ?");
     return askCF;

#_INITIALISATION NEW FORMAT 
def initNewFormat(sizeW,sizeH):
     newformat = ""
     
     if sizeW == sizeH:
          newFormatName = "square_"+ str(sizeW);
     else:
          newFormatName =  str(sizeW) + "*"+ str(sizeH);
     
     newformat = str(outputSizeW) + " " + str(outputSizeH) + " " + str(newFormatName);

     return newformat, newFormatName

#_FORMAT CHECKER
def formatChecker(formatName):
     nukeFormats = nuke.formats()
     valid = 1
     for nukeFormat in nukeFormats:
          nukeFormatName = nukeFormat.name()
          if formatName == nukeFormatName:
               valid = 0;

     return valid

#____INITIALISATION____#
#inputNode = nuke.knob.input
#if inputNode == none
#     inputNodeName = nodeName
#
node = nuke.toNode("Read1")
nodeFormat = node.format()

#outputSizeW = node.format.w
#outputSizeH = node.format.h
outputSizeW = 1000
outputSizeH = 1000
newFormatName = initNewFormat(outputSizeW, outputSizeH)[1]
formatChecker = formatChecker( initNewFormat( outputSizeW, outputSizeH )[1] )


#____EXECUTE BUTTON____#

if askCreateFormat():
     
     if formatChecker != 0:
          
          createFormat(outputSizeW,outputSizeH);
          nuke.message("format " + newFormatName + " created!")
     
     else:
          
          nuke.message( newFormatName + " existe !" )
     
else:
     nuke.message("format no created");

     
#_____BOUTTON CREER REFORMAT AVEC LE NEW FORMAT___

thisNode = nuke.knob()
reformat = nuke.node.Reformat()
reformat.setInput(thisNode)
reformat['format'].setValue(newFormatName)
