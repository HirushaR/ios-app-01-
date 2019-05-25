from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    pass
class SettingScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")

class MainApp(App):
    def Build(self):
        return GUI

    def change_screen(self,screen_name):
        #get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name

if __name__ == '__main__':
    MainApp().run()