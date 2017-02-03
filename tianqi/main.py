# -*- coding: utf-8 -*-
'''
Container Example
==============

This example shows how to add a container to our screen.
A container is simply an empty place on the screen which
could be filled with any other content from a .kv file.
'''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown
import sqlite3

import os
import kivy
kivy.require('1.8.0')
from kivy.core.window import Window

Window.size = (1120, 630)


class Ecrans():
	pass

class RootWidget(BoxLayout):
	'''Create a controller that receives a custom widget from the kv lang file.
	Add an action to be called from a kv file.
	'''

	container = ObjectProperty(None)

class MainApp(App):

	def build(self):
		'''This method loads the root.kv file automatically

<<<<<<< HEAD
		:rtype: none
		'''
		# loading the content of root.kv
		self.root = Builder.load_file('view/root.kv')	
		self.wall = Builder.load_file('view/wall_builder_screen.kv')
		
	#Get all name of walls 
=======
    def build(self):
        '''This method loads the root.kv file automatically

        :rtype: none
        '''
        # loading the content of root.kv
        self.root = Builder.load_file('view/root.kv')

>>>>>>> b7b191d3518ef2348e22a80dcbab63fe41436549
	def get_all_wall_name(self):
	
		values = []
		conn = sqlite3.connect('data.db')
		cursor = conn.execute("SELECT name from WALL")

		for row in cursor:
			values.append(row[0]) 
		conn.close()
		
		print "Operation done successfully";
		
		#self.wall.spinner.text = values
		#self.wall.spinner.values = wall.spinner.values[0]
		return values
		
	#Get first name of walls 
	def get_first_wall_name(self):
	
		values = []
		conn = sqlite3.connect('data.db')
		cursor = conn.execute("SELECT name from WALL")

		for row in cursor:
			values.append(row[0]) 
		conn.close()
		
		print "Operation done successfully";
		return values[0]

	def next_screen(self, screen):
		'''Clear container and load the given screen object from file in kv
		folder.

		:param screen: name of the screen object made from the loaded .kv file
		:type screen: str
		:rtype: none
		'''

		filename = screen + '.kv'
		# unload the content of the .kv file
		# reason: it could have data from previous calls
		Builder.unload_file('view/' + filename)
		# clear the container
		self.root.container.clear_widgets()
		# load the content of the .kv file
		screen = Builder.load_file('view/' + filename)
		# add the content of the .kv file to the container
		self.root.container.add_widget(screen)


if __name__ == '__main__':
	'''Start the application'''
	MainApp().run()
