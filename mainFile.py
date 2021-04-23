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


def write_json(data, filename='credentials.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


class LoginScreen(Screen):

    def clearCredentials(self, usern, passw):
        usern = ""
        passw = ""

    def logIn(self):

        self.manager.current = "AccountPage"

        # clears the text entered by user
        self.identification.text = ""
        self.password.text = ""

    def addUser(self, username, password):

        with open('credentials.json', 'r') as json_file:
            data = json.load(json_file)

        isUser = True

        while isUser:
            for user in data['userAccounts']:
                if user['username'] == username:
                    print("____User Found____")

                    if user['password'] == password:
                        print("Correct password entered!!")
                        isUser = False
                        self.logIn()
                        break
                    else:
                        print("Incorrect username or password!!")

                else:
                    continue

            break

    def onLoginClick(self):
        print("_______**TRIED TO LOGIN**_______")

        # checks if the entered username and password are present in json file
        self.addUser(self.identification.text, self.password.text)

        # with open('credentials.json', 'r') as json_file:
        #     data = json.load(json_file)

        # isUser = True
        # while isUser:
        #     for user in data['userAccounts']:
        #         if user['username'] == self.identification.text:
        #             print("____User Found____")
        #
        #             if user['password'] == self.password.text:
        #                 print("Correct password entered!!")
        #                 self.logIn()
        #                 isUser = False
        #             else:
        #                 print("Incorrect password!!")
        #
        #         else:
        #             print("____User Not Found____")
        #             isUser = False


class AccountScreen(Screen):
    def logOut(self):
        self.manager.current = "LoginPage"


class AddAccountScreen(Screen):
    def onAddAccountClick(self):

        # Exit if either id or password is empty
        if self.ids["newIdentification"].text == "" or self.ids["newPassword"].text == "":
            self.manager.current = "LoginPage"
        else:
            # adding new id and password to json file
            with open('credentials.json') as json_file:
                data = json.load(json_file)

                temp = data['userAccounts']

                y = {"username": self.ids["newIdentification"].text,
                     "password": self.ids["newPassword"].text}

                temp.append(y)

            write_json(data)

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
