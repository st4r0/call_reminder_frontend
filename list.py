from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from backend_call import get_check_for_calls


class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)


class Menu(Screen):
    view = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        Clock.schedule_once(self.create_scrollview)

    def create_scrollview(self, dt):
        element_names = [f"{i}" for i in get_check_for_calls().index]
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))

        for element_name in element_names:
            layout.add_widget(Button(text=element_name, size=(50, 50), size_hint=(1, None),
                                     background_color=(0.5, 0.5, 0.5, 1), color=(1, 1, 1, 1)))
        scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scrollview.add_widget(layout)
        self.view.add_widget(scrollview)


Builder.load_file("debug.kv")


class MyApp(App):

    def build(self):
        return AppScreenManager()


if __name__ == '__main__':
    MyApp().run()
