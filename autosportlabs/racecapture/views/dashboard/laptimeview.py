import kivy
kivy.require('1.8.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from utils import kvFind

Builder.load_file('autosportlabs/racecapture/views/dashboard/laptimeview.kv')

class LaptimeView(Screen):

    def __init__(self, **kwargs):
        super(LaptimeView, self).__init__(**kwargs)
        self.initView()

    def initView(self):
        pass
