from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import requests
import json

class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class SettingScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")

class MainApp(App):
    my_friend_id =1
    def Build(self):
        return GUI

    def on_start(self):
        #get databsae data
        result = requests.get("https://friendly-fitness-f5791.firebaseio.com/"+str(self.my_friend_id)+".json")
        print("was it ok?",result.ok)
        data = json.loads(result.content.decode())
        print(data)

        workouts = data['workouts'][1:]
        for workout in workouts:
            print(workout['workout_image'])
            print(workout['units'])
        #populate workout grid in home screen

    def change_screen(self,screen_name):
        #get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name

if __name__ == '__main__':
    MainApp().run()