def lue4nukeConvert() : 
    nodes = nuke.selectedNodes()
    ref_node = nodes.pop(-1)
    needKnobs = ["blackpoint", "whitepoint" ,"add", "red", "Temperature", "Tint", "Contrast", "ColorBoost", 'General_Enable', 'liftgammagain_Enable', 'LiftEnabled', 'GammaEnabled', 'GainEnabled', 'SMH_Enable', 'ShadowsEnabled', 'MidtonesEnabled', 'HighlightsEnabled', 'SplitToning_Enable', 'Primaries_Enable', 'ColorMixer_Enable', 'BW_Enable', 'Vingette_Enable', 'VingetteO_Enable', 'Sharpen_Enable', 'Grain_Enable', 'Mist_Enable', "colorspace_out", "Lift", "Gamma","Gain", "Midtones", "Highlights", "High", "low", "LumaMix", 'Split_Bright_Hue', 'Split_Bright_Sat', 'Split_Dark_Hue', 'Split_Dark_Sat', 'Split_Contrast', 'Split_Offset', 'Split_Mix', 'Prim_HueRed', 'Prim_HueGreen', 'Prim_HueBlue',"PO_Method","RED","Green", "Blue", "BWSoftFilter", 'Vin_Gain', 'Vin_Scale', 'Vin_Feather', 'Vin_Offset', 'Vin_HighlightPrio', 'Vin_Method', 'Vin_HilightIn', 'Vin_HilightOut', 'VinO_Opacity', 'VinO_Invert', 'VinO_Scale', 'VinO_Feather', 'VinO_Offset', 'VinO_Tint', 'Sharpen_1' ,'Grain_Size', 'Grain_Intensity' ,'Mist_Opacity', 'Mist_Gamma', 'Mist_ColorMix', 'Mist_Premultiplied', 'mix','invert_mask' ]
    
    for node in nodes : 
        if not "lue4" in node["name"].value().lower(): 
            continue

        for knob in needKnobs :
            print (f"Copy {knob} ")
            node[knob].setValue(ref_node[knob].value())

lue4nukeConvert()
