#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Offset to Left
#
#----------------------------------------------------------------------------------------------------------

inc = 100

for node in nuke.selectedNodes():
    node.setXYpos(node.xpos()-inc, node.ypos())