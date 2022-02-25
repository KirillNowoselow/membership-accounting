import os

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.welcome import Welcome
from screens.clients import Clients
from screens.NewAboniment import NewAb
from kivy.core.window import Window
Window.size = (400, 700)


class MembershipAccounting(App):

    def build(self):
        sm = ScreenManager()

        Builder.load_file(os.path.join(os.getcwd(), 'designs', 'NewAboniment.kv'))
        sm.add_widget(NewAb(name='welcome'))



        return sm


if __name__ == '__main__':
    MembershipAccounting().run()
