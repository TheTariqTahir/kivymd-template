from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.metrics import dp, sp
# import requests

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from kivymd.uix.list import ThreeLineListItem
# from kivymd.uix.label import MDLabel
# from kivymd.uix.menu import MDDropdownMenu
# from kivymd.uix.picker import MDDatePicker
# from kivymd.uix.list import TwoLineIconListItem,TwoLineListItem
# from kivymd.uix.label import MDLabel

from kivy.core.window import Window
Window.size = 360,600

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'




import requests



class WelcomeScreen(Screen):
    pass


class MainPage(Screen):
    pass


class AboutPage(Screen):
    pass


class ProfilePage(Screen):
    pass


sm = ScreenManager()

sm.add_widget(WelcomeScreen(name='WelcomeScreen'))
sm.add_widget(MainPage(name='MainPage'))
sm.add_widget(AboutPage(name='AboutPage'))
sm.add_widget(ProfilePage(name='ProfilePage'))


class LoginApp(MDApp):
    def build(self):
        self.helper = Builder.load_file("helpers.kv")
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Light"
        return self.helper


    def toggle_nav(self):
            self.root.ids.nav_drawer.set_state('toggle')


    def show_dialog(self, title, text):
        title = title
        text = text
        cancel_btn_username_dialouge = MDFlatButton(
            text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title=text, text=text, size_hint=(
            0.7, 0.2), buttons=[cancel_btn_username_dialouge])
        self.dialog.open()

    def close_dialog(self, obj):
            self.dialog.dismiss()
    


LoginApp().run()
