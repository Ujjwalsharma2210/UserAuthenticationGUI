
###############################################
#                                             #
#       Author UjjwalSharma 24/04/2020        #
#               Version 1.2                   #
#               					          #
###############################################

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

import uuid
import hashlib


def hash_str(strToBeHashed):
	# uuid is used to generate a random number
	bubb = uuid.uuid4().hex
	return hashlib.sha256(bubb.encode() + strToBeHashed.encode()).hexdigest() + ')' + bubb


def check_str(hashed_str, user_str):
	password, bubb = hashed_str.split(')')
	return password == hashlib.sha256(bubb.encode() + user_str.encode()).hexdigest()


def write_json(data, filename='credentials.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)


class LoginScreen(Screen):

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
			# for user in data['userAccounts']:
			# 	if user['username'] == username:
			# 		print("____User Found____")
			#
			# 		if user['password'] == password:
			# 			print("Correct password entered!!")
			# 			self.logIn()
			# 			break
			# 		else:
			# 			print("Incorrect username or password!!")
			# 	else:
			# 		continue
			#
			# isUser = False
			# break

			for user in data['userAccounts']:
				if check_str(user['username'], username):
					print("____User Found____")

					if check_str(user['password'], password):
						print("Correct password entered!!")
						self.logIn()
						break
					else:
						print("Incorrect username or password!!")
				else:
					continue

			isUser = False
			break

	def onLoginClick(self):
		print("_______**TRIED TO LOGIN**_______")

		# checks if the entered username and password are present in json file
		self.addUser(self.identification.text, self.password.text)


class AccountScreen(Screen):
	def logOut(self):
		self.manager.current = "LoginPage"


class AddAccountScreen(Screen):

	def addAccount(self, username, password):
		# adding new id and password to json file
		with open('credentials.json') as json_file:
			data = json.load(json_file)

			temp = data['userAccounts']

			y = {"username": hash_str(username),
			     "password": hash_str(password)}

			temp.append(y)

		write_json(data)

		print("New user added.")

		self.newIdentification.text = ""
		self.newPassword.text = ""

	def onAddAccountClick(self):

		# Exit if either id or password is empty
		if self.ids["newIdentification"].text == "" or self.ids["newPassword"].text == "":
			self.manager.current = "LoginPage"
		else:
			self.addAccount(self.ids["newIdentification"].text,
			                self.ids["newPassword"].text)

		self.manager.current = "LoginPage"


class ScreenManager(ScreenManager):
	pass


kv = Builder.load_file("mainFile.kv")


class Main(App):
	def build(self):
		return kv


if __name__ == '__main__':
	Main().run()
