""" Action set for the Oracl plugin

"""
# Copyright (C) 2009-2010, Ecole Polytechnique Federale de Lausanne (EPFL) and
# University Hospital Center and University of Lausanne (UNIL-CHUV)
#
# Modified BSD License

# Enthought library imports
from envisage.ui.action.api import Action, Group, Menu, ToolBar
from envisage.ui.workbench.api import WorkbenchActionSet



networkrepo = Action(
    id            = "OracleCNetworkReport",
    class_name    = "cviewer.plugins.codeoracle.actions.NetworkReport",
    name          = "Network Report",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Analysis"
)

xnat_pushpull = Action(
    id            = "OracleXNATPushPull",
    class_name    = "cviewer.plugins.codeoracle.actions.XNATPushPull",
    name          = "XNAT Push and Pull",
    path          = "MenuBar/Code Oracle/Other/XNAT"
)

show_surface = Action(
    id            = "OracleCSurface",
    class_name    = "cviewer.plugins.codeoracle.actions.ShowSurfaces",
    name          = "Show Surface",
    path          = "MenuBar/Code Oracle/Connectome/CSurface/Visualization"
)

show_volumecre = Action(
    id            = "OracleCVolumeCre",
    class_name    = "cviewer.plugins.codeoracle.actions.ShowVolumes",
    name          = "Volume Creation",
    path          = "MenuBar/Code Oracle/Connectome/CVolume/Visualization"
)

show_network = Action(
    id            = "OracleCNetwork3D",
    class_name    = "cviewer.plugins.codeoracle.actions.ShowNetworks",
    name          = "3D Network",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Visualization"
)

show_network2 = Action(
    id            = "OracleCNetwork3D2",
    class_name    = "cviewer.plugins.codeoracle.actions.NetworkVizTubes",
    name          = "3D Network (with tubes and node color)",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Visualization"
)

connection_matrix = Action(
    id            = "OracleCNetworkMat",
    class_name    = "cviewer.plugins.codeoracle.actions.ConnectionMatrix",
    name          = "Connection Matrix",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Visualization"
)

simple_connection_matrix = Action(
    id            = "OracleCNetworkSimpleMat",
    class_name    = "cviewer.plugins.codeoracle.actions.SimpleConnectionMatrix",
    name          = "Simple Connection Matrix",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Visualization"
)

writegexf = Action(
    id            = "OracleCNetworkWriteGEXF",
    class_name    = "cviewer.plugins.codeoracle.actions.WriteGEXF",
    name          = "Write Gephi GEXF",
    path          = "MenuBar/Code Oracle/Connectome/CNetwork/Analysis"
)

compute_nbs = Action(
    id            = "OracleNBS",
    class_name    = "cviewer.plugins.codeoracle.actions.ComputeNBS",
    name          = "Network-based statistic (NBS)",
    path          = "MenuBar/Code Oracle/Statistics"
)

show_tracks = Action(
    id            = "OracleShowTracks",
    class_name    = "cviewer.plugins.codeoracle.actions.ShowTracks",
    name          = "Tracks between regions",
    path          = "MenuBar/Code Oracle/Connectome/CTrack/Visualization"
)

cortico_cortico = Action(
    id            = "OracleCorticoCorticoTracks",
    class_name    = "cviewer.plugins.codeoracle.actions.CorticoCortico",
    name          = "Extract cortico-cortico fiber tracks",
    path          = "MenuBar/Code Oracle/Connectome/CTrack/Analysis"
)

nipype_bet = Action(
    id            = "OracleNipypeBet",
    class_name    = "cviewer.plugins.codeoracle.actions.NipypeBet",
    name          = "Brain extraction using BET",
    path          = "MenuBar/Code Oracle/Other/Nipype"
)

nipype_PlotNodes = Action(
    id            = "NipypePlotNodes",
    class_name    = "cviewer.plugins.codeoracle.actions.PlotNodes",
    name          = "Plot Nodes",
    path          = "MenuBar/Plotting"
)

nipype_PlotEdges = Action(
    id            = "NipypePlotEdges",
    class_name    = "cviewer.plugins.codeoracle.actions.PlotEdges",
    name          = "Plot Edges",
    path          = "MenuBar/Plotting"
)

nipype_PlotLabelsByPhrase = Action(
    id            = "NipypePlotLabelsByPhrase",
    class_name    = "cviewer.plugins.codeoracle.actions.PlotLabelsByPhrase",
    name          = "Plot Labels By Phrase",
    path          = "MenuBar/Plotting"
)


class OracleActionSet(WorkbenchActionSet):
    """ The actionset for the Oracle plugin """
    
    id = "cviewer.plugins.codeoracle.action_set"
    
    actions = [
        show_surface,
        show_network,
        show_network2,
        compute_nbs,
        show_volumecre,
        connection_matrix,
        simple_connection_matrix,
        show_tracks,
        cortico_cortico,
        xnat_pushpull,
        nipype_bet,
        networkrepo,
        writegexf,
        nipype_PlotNodes,
        nipype_PlotLabelsByPhrase,
        nipype_PlotEdges,
    ]
