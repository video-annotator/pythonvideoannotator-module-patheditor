import csv, cv2, os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel


class PathEditorObject2d(object):

	def __init__(self, objects_set):
		super(PathEditorObject2d, self).__init__(objects_set)

		self.create_tree_nodes()
		

	def create_path_dataset(self): 
		path = super(PathEditorObject2d, self).create_path_dataset()
		self.mainwindow.add_dataset_evt(path)
		return path

	######################################################################
	### AUX FUNCTIONS ####################################################
	######################################################################

	def create_tree_nodes(self):
		self.treenode = self.tree.createChild(self.name, icon=conf.ANNOTATOR_ICON_OBJECT )
		self.tree.addPopupMenuOption(
			label='Create a path dataset', 
			functionAction=self.create_path_dataset, 
			item=self.treenode, icon=conf.ANNOTATOR_ICON_TIMELINE
		)
		self.treenode.win = self
		
		

	def create_motion_tree_nodes(self):
		
		self.treenode_motion = self.tree.createChild('Motion', icon=conf.ANNOTATOR_ICON_PATH, parent=self.treenode )
		variation_treenode 	 = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_motion )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_variation_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_motion.obj = variation_treenode.obj = self


	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property 
	def tree(self): return self.objects_set._tree