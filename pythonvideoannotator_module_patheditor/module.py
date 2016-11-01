import cv2, os
from pysettings import conf
from PyQt4 import QtCore, QtGui
from pythonvideoannotator.utils.tools import list_folders_in_path
from pythonvideoannotator.models.objects import Objects

from pyforms.Controls import ControlDockWidget

class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()

		self._right_docker          = ControlDockWidget('Objects list',side=ControlDockWidget.SIDE_RIGHT, order=0, margin=5)        
		self._right_details         = ControlDockWidget('Details',side=ControlDockWidget.SIDE_RIGHT, order=1, margin=5)        
		
		self._right_docker.value    = self._objects_window = Objects(parent=self)
		#self._right_docker.hide()
		#self._right_details.hide()

	
		self.mainmenu.insert(2,
			{'Windows': [
				{'Objects': self.__show_objects_list_evt, 'icon':conf.ANNOTATOR_ICON_OBJECT }
			]}
		)

	def __show_objects_list_evt(self):
		self._right_docker.show()
		self._right_details.show()

	def onPlayerClick(self, event, x, y): 
		self._objects_window.player_on_click(event, x, y)


	def process_frame(self, frame):
		"""
		Function called before render each frame
		"""
		self._objects_window.draw(frame, self._player.video_index)
		return frame

	def add_object_evt(self, obj): 	 	pass
	def remove_object_evt(self, obj): 	pass

	def add_dataset_evt(self, dataset):    pass
	def remove_dataset_evt(self, dataset): pass
	

	def add_chart(self, name, data):  	 self._time.add_chart(name, data)

	
	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	
	def save(self, data, project_path=None):
		data = super(Module, self).save(data, project_path)
		
		objects_path = os.path.join(project_path, 'objects')
		if not os.path.exists(objects_path): os.makedirs(objects_path)
		
		return self._objects_window.save(data, objects_path)


	def load(self, data, project_path=None):
		data = super(Module, self).load(data, project_path)

		objects_path = os.path.join(project_path, 'objects')
		self._objects_window.load(data, objects_path)


	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################
	
	@property
	def objects(self): return self._objects_window.objects

	@property
	def details(self): return self._right_details.value
	@details.setter
	def details(self, value): self._right_details.value = value
