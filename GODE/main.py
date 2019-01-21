from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class UI(BoxLayout):
    def new(self):
        print("NEW")
    
    def open(self):
        print("Open")
    
    def save(self):
        print("Save")
        
    def saveAs(self):
        print("save As")
        
   
class GODEApp(App):

    def build(self):
        return UI()


if __name__ == '__main__':
    GODEApp().run()
