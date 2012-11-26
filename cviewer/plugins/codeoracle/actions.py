import logging

from apptools.io.api import File
from pyface.api import FileDialog, OK
from pyface.action.api import Action
from traits.api import Any

from cviewer.plugins.text_editor.editor.text_editor import TextEditor
from cviewer.plugins.ui.preference_manager import preference_manager

# Logging imports
import logging
logger = logging.getLogger('root.'+__name__)

class PlotEdges(Action):
    tooltip = "Plot edges"
    description = "Plots edges from a selected network"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):
        from cnetwork_action import EdgeParameter
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = EdgeParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            import tempfile
            import networkx as nx
            import nipype.interfaces.connectomeviewer as cv
            
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            network = no.netw[no.graph]['name']
            graph = cfile.obj.get_by_name(network).data
            tmpname = '/tmp/' + network + '.pck'
            nx.write_gpickle(graph, tmpname)
            node_position = no.node_position
            edge_key = no.edge_value
            plot = cv.PlotEdges()
            plot.inputs.in_files = tmpname
            plot.inputs.position_key = node_position
            plot.inputs.edge_key = edge_key
            plot.run()
        
class PlotLabelsByPhrase(Action):
    tooltip = "Plot labels"
    description = "Plots node labels that contain the entered text (e.g. occipital)"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):
        from cnetwork_action import NodeLabelByPhraseParameter
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = NodeLabelByPhraseParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            import tempfile
            import networkx as nx
            import nipype.interfaces.connectomeviewer as cv
            
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            network = no.netw[no.graph]['name']
            graph = cfile.obj.get_by_name(network).data
            tmpname = '/tmp/' + network + '.pck'
            nx.write_gpickle(graph, tmpname)
            node_position = no.node_position
            node_label_key = no.node_label
            phrase = no.phrase
            plot = cv.PlotLabelsByPhrase()
            plot.inputs.in_files = tmpname
            plot.inputs.position_key = node_position
            plot.inputs.label_key = node_label_key
            plot.inputs.phrase = phrase
            plot.run()
        
class PlotNodes(Action):
    tooltip = "Plot Nodes"
    description = "Plots nodes from a selected network"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):
        from cnetwork_action import NodeParameter
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = NodeParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            import tempfile
            import networkx as nx
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            network = no.netw[no.graph]['name']
            graph = cfile.obj.get_by_name(network).data
            tmpname = '/tmp/' + network + '.pck'
            nx.write_gpickle(graph, tmpname)
            node_position = no.node_position
            #node_position = no.scalar_key
            import nipype.interfaces.connectomeviewer as cv
            plot = cv.PlotNodes()
            plot.inputs.in_files = tmpname
            plot.inputs.position_key = node_position
            plot.run()


class NetworkVizTubes(Action):
    tooltip = "Show 3D Network with Tubes"
    description = "Show 3D Network with Tubes and colorcoded Nodes"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import threedviz2

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(threedviz2)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)


class NetworkReport(Action):
    tooltip = "Network Report"
    description = "Network Report"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import reportlab

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(reportlab)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class WriteGEXF(Action):
    tooltip = "Write Gephi GEXF file"
    description = "Write Gephi GEXF file"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import writegexf

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(writegexf)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class CorticoCortico(Action):
    tooltip = "Extract cortico-cortico fibers"
    description = "Extract cortico-cortico fibers"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import corticocortico

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(corticocortico)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)


class NipypeBet(Action):
    tooltip = "Brain extraction using BET"
    description = "Brain extraction using BET"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import nipypebet

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(nipypebet)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)


class ShowTracks(Action):
    tooltip = "Show tracks between two regions"
    description = "Show tracks between two regions"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import ctrackedge

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(ctrackedge)
        f.close()
        
        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class XNATPushPull(Action):
    tooltip = "Push and pull files from and to XNAT Server"
    description = "Push and pull files from and to XNAT Server"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from scripts import pushpull

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(pushpull)
        f.close()

        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class ComputeNBS(Action):
    tooltip = "Compute NBS"
    description = "Compute NBS"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

#        from cnetwork_nbs_action import NBSNetworkParameter, NBSMoreParameter
        from scripts import nbsscript
#        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
#
#        no = NBSNetworkParameter(cfile)
#        no.edit_traits(kind='livemodal')
#
#        if (len(no.selected1) == 0 or len(no.selected2) == 0):
#            return
#
#        mo = NBSMoreParameter(cfile, no.selected1[0], no.selected2[0])
#        mo.edit_traits(kind='livemodal')
#
#        import datetime as dt
#        a=dt.datetime.now()
#        ostr = '%s%s%s' % (a.hour, a.minute, a.second)
        
#        if not (len(no.selected1) == 0 or len(no.selected2) == 0):
#            # if cancel, not create surface
#            # create a temporary file
#            import tempfile
#            myf = tempfile.mktemp(suffix='.py', prefix='my')
#            f=open(myf, 'w')
#            f.write(nbsscript % (str(no.selected1),
#                                 mo.first_edge_value,
#                                 str(no.selected2),
#                                 mo.second_edge_value,
#                                 mo.THRES,
#                                 mo.K,
#                                 mo.TAIL,
#                                 ostr))
#            f.close()
#
#            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

        import tempfile
        myf = tempfile.mktemp(suffix='.py', prefix='my')
        f=open(myf, 'w')
        f.write(nbsscript)
        f.close()
    
        self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)


class ShowNetworks(Action):
    tooltip = "Create a 3D Network"
    description = "Create a 3D Network"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from cnetwork_action import NetworkParameter
        from scripts import netscript
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = NetworkParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            # if cancel, not create surface
            # create a temporary file
            import tempfile
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            f=open(myf, 'w')
            f.write(netscript % (no.netw[no.graph]['name'],
                                  no.node_position,
                                  no.edge_value,
                                  no.node_label))
            f.close()
            
            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class ConnectionMatrix(Action):
    tooltip = "Show connection matrix"
    description = "Show connection matrix"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from cnetwork_action import MatrixNetworkParameter
        from scripts import conmatrix
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = MatrixNetworkParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            # if cancel, not create surface
            # create a temporary file
            import tempfile
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            f=open(myf, 'w')
            f.write(conmatrix % (no.netw[no.graph]['name'],
                                  no.node_label))
            f.close()
            
            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class SimpleConnectionMatrix(Action):
    tooltip = "Show simple connection matrix"
    description = "Show simple connection matrix"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):

        from cnetwork_action import MatrixEdgeNetworkParameter
        from scripts import conmatrixpyplot
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
        
        no = MatrixEdgeNetworkParameter(cfile)
        no.edit_traits(kind='livemodal')

        if not no.netw[no.graph]['name'] == "None":
            # if cancel, not create surface
            # create a temporary file
            import tempfile
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            f=open(myf, 'w')
            f.write(conmatrixpyplot % (no.netw[no.graph]['name'],
                                  no.edge_label))
            f.close()

            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

class ShowSurfaces(Action):
    """ Open a new file in the text editor
    """
    tooltip = "Create a surface"
    description = "Create a surface"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):
        
        from csurface_action import SurfaceParameter
        from scripts import surfscript
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
                
        so = SurfaceParameter(cfile)
        so.edit_traits(kind='livemodal')
        
        if not so.pointset_da[so.pointset]['name'] == "None":
            # if cancel, not create surface
            # create a temporary file
            import tempfile
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            f=open(myf, 'w')
            if so.labels_da[so.labels].has_key('da_idx'):
                labels = so.labels_da[so.labels]['da_idx']
            else:
                labels = 0
            f.write(surfscript % (so.pointset_da[so.pointset]['name'],
                                  so.pointset_da[so.pointset]['da_idx'],
                                  so.faces_da[so.faces]['name'], 
                                  so.faces_da[so.faces]['da_idx'],
                                  so.labels_da[so.labels]['name'],
                                  labels))
            f.close()
            
            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)


class ShowVolumes(Action):
    """ Open a new file in the text editor
    """
    tooltip = "Create a volume"
    description = "Create a volume"

    # The WorkbenchWindow the action is attached to.
    window = Any()

    def perform(self, event=None):
        
        from cvolume_action import VolumeParameter
        from scripts import volslice
        cfile = self.window.application.get_service('cviewer.plugins.cff2.cfile.CFile')
                
        so = VolumeParameter(cfile)
        so.edit_traits(kind='livemodal')
        
        if True: #not so.pointset_da[so.pointset]['name'] == "None":
            # if cancel, not create surface
            # create a temporary file
            import tempfile
            myf = tempfile.mktemp(suffix='.py', prefix='my')
            f=open(myf, 'w')
            f.write(volslice % so.volumes[so.myvolume]['name'])
            f.close()
            
            self.window.workbench.edit(File(myf), kind=TextEditor,use_existing=False)

