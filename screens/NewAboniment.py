from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition


class NewAb(Screen):

    def create(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'clients'