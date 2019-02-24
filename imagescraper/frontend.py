# import Kivy
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import subprocess

# from process_images import *

def combineKeywords(keywords):
        ret = ''
        for i, word in enumerate(keywords):
            ret += word
            if i != len(keywords)-1:
                ret+=','
        return ret

class MyApp(App):
# layout

    def build(self):
        self.keywords = []
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)

        self.lbl1 = Label(text="These are your keywords: ")
        layout.add_widget(self.lbl1)

        self.txt1 = TextInput(text='Enter your command here', multiline=False)
        self.txt1.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.txt1)

        btn2 = Button(text="Submit")
        btn2.bind(on_press=self.submitKeywords)
        layout.add_widget(btn2)

        return layout

    # button click function
    def buttonClicked(self, btn):
        self.keywords.append(self.txt1.text)
        self.lbl1.text = "These are your keywords: " + combineKeywords(self.keywords)

    def on_enter(instance, value):
        print('User pressed enter in', instance)
        value = ""
        print instance.txt1.text
        instance.txt1.text = ""
        # process_images(['ball', 'swim'])

    def submitKeywords(self, btn):
        
        # print "hi"
        for key in self.keywords:
            print key

        subprocess.call(["python", "process_images.py", combineKeywords(self.keywords)])
        subprocess.call(["python", "mosaic.py", "image.jpg", "images/"])


# run app
if __name__ == "__main__":
    MyApp().run()
 # join all items in a list into 1 big string