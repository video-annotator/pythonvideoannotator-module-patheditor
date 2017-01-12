import cv2, os
from pysettings import conf
from PyQt4 import QtCore, QtGui
from pyforms.Controls 						import ControlDockWidget
from pythonvideoannotator.utils.tools 		import list_folders_in_path
from pythonvideoannotator_models_gui.models import Project
from pythonvideoannotator_models_gui.dialogs import Dialog

class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()

		self._right_docker          = ControlDockWidget('Videos list',side=ControlDockWidget.SIDE_LEFT, order=0, margin=5)        
		self._right_details         = ControlDockWidget('Details',side=ControlDockWidget.SIDE_RIGHT, order=1, margin=5)        
		
		self._right_docker.value    = self._project
		#self._right_docker.hide()
		#self._right_details.hide()

		self.mainmenu[2]['Windows'].append({'Videos': self.__show_objects_list_event, 'icon':conf.ANNOTATOR_ICON_MOVIES })
		
	def __show_objects_list_event(self):
		self._right_docker.show()
		self._right_details.show()

	def on_player_click_event(self, event, x, y): 
		self._project.player_on_click(event, x, y)


	def process_frame_event(self, frame):
		"""
		Function called before render each frame
		"""
		if self._player.video_index is not None: 
			self._project.draw(frame, self._player.video_index)
		return frame

	def add_graph(self, name, data):  	 	self._time.add_graph(name, data)



	
	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	
	def save(self, data, project_path=None):
		data = super(Module, self).save(data, project_path)
		self._project.save(data, project_path)
		return data


	def load(self, data, project_path=None):
		super(Module, self).load(data, project_path)
		self._project.load(data, project_path)
	

	def save_project(self, project_path=None):
		super(Module, self).save_project(self._project.directory if project_path is None else project_path)



	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################
	
	@property
	def objects(self): return self._project.objects

	@property
	def details(self): return self._right_details.value
	@details.setter
	def details(self, value): self._right_details.value = value
