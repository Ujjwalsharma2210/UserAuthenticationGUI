from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

import json


class LoginScreen(Screen):
    def onLoginClick(self):
        print("_______**TRIED TO LOGIN**_______")
        if self.ids["identification"].text == "username" and self.ids["password"].text == "password":
            self.manager.current = "AccountPage"
            print("Logger ID : {0}".format(self.ids["identification"].text))
        else:
            self.identification.text = ""
            self.password.text = ""


class AccountScreen(Screen):
    pass


class AddAccountScreen(Screen):
    def onAddAccountClick(self):
        data = {}
        with open('credentials.json') as f:
            data = json.load(f)

        # data['user'] = self.ids["newIdentification"].text
        # data['password'] = self.ids["newPassword"].text

        with open('credentials.json', 'a') as f:
            json.dump(data, f)

        self.newIdentification.text = ""
        self.newPassword.text = ""

        self.manager.current = "LoginPage"


class ScreenManager(ScreenManager):
    pass


kv = Builder.load_file("mainFile.kv")


class Main(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Main().run()