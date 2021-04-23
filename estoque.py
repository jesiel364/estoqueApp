from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

class Gerenciador(ScreenManager):
	pass
class Cadastro1(Screen):
	pass
class Cadastro2(Screen):
	pass
class Cadastro3(Screen):
	pass





class Estoque(App):
	
	def build(self):
		Window.clearcolor = (89/255, 74/255, 92/255, 1)
		#Window.size = (740,1720)
		return Builder.load_string('''
Gerenciador:
	Cadastro1:
	Cadastro2:
	Cadastro3:

<Cadastro1>:
	name: 'tela1'
	FloatLayout:
		size_hint: .8, .8
		pos_hint: {'center_x': .5, 'center_y': .5}

		canvas:
			Color:
				rgba: (202/255, 30/255, 173/255, 0.5)
			Rectangle:
				size: self.size
				pos: self.pos
				source: 'bg.jpg'

		Label:
			text: 'Erros'
			color: (109/255, 121/255, 198/255, 1)
			font_size: 30
			pos_hint: {'center_x': .5, 'y': .4}

		Button:
			text: '->'
			on_release: app.root.current = 'tela2'
			text:
			pos_hint: {'center_x': .5, 'y': .2}
			size_hint: .5,.1
			
		TextInput:
			font_size: '25sp'
			size: .6, .1
			size_hint: .5,.1
			pos_hint: {'center_x': .5, 'y': .5}

<Cadastro2>:
	name: 'tela2'
	FloatLayout:
		size_hint: .8, .8
		pos_hint: {'center_x': .5, 'center_y': .5}

		canvas:
			Color:
				rgba: (202/255, 30/255, 173/255, 0.5)
			Rectangle:
				size: self.size
				pos: self.pos
				source: 'bg.jpg'

		Label:
			text: 'Reposições'
			color: (109/255, 121/255, 198/255, 1)
			font_size: 30
			pos_hint: {'center_x': .5, 'y': .4}

		Button:
			on_release: app.root.current = 'tela3'
			text:
			pos_hint: {'center_x': .5, 'y': .2}
			size_hint: .5,.1

<Cadastro3>:
	name: 'tela3'
	FloatLayout:
		size_hint: .8, .8
		pos_hint: {'center_x': .5, 'center_y': .5}

		canvas:
			Color:
				rgba: (202/255, 30/255, 173/255, 0.5)
			Rectangle:
				size: self.size
				pos: self.pos
				source: 'bg.jpg'

		Label:
			text: 'Data'
			color: (109/255, 121/255, 198/255, 1)
			font_size: 30
			pos_hint: {'center_x': .5, 'y': .4}

		Button:
			on_release: app.root.current = 'tela1'
			text:
			pos_hint: {'center_x': .5, 'y': .2}
			size_hint: .5,.1

''')

Estoque().run()