from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView

from backend_call import get_check_for_calls, get_update_after_call


class ThreeLineListItemAligned(ThreeLineListItem):
    def __init__(self, halign, **kwargs):
        super(ThreeLineListItemAligned, self).__init__(**kwargs)
        self.ids._lbl_primary.halign = halign
        self.ids._lbl_secondary.halign = halign
        self.ids._lbl_tertiary.halign = halign


class DemoApp(MDApp):

    @staticmethod
    def update_just_called(item: ThreeLineListItemAligned):
        get_update_after_call(item.text)

    def build(self):
        screen = Screen()

        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList(spacing=10, md_bg_color=(0, 0, 0, 1))
        df = get_check_for_calls()
        for name in df.index:
            items = ThreeLineListItemAligned(
                text=name,
                secondary_text=f"due since {df.loc[name, 'due_since']} days",
                tertiary_text=f"last call {df.loc[name, 'last_call']}",
                size=(50, 50), size_hint=(1, None),
                bg_color=(0.5, 0.5, 0.5, 1),
                text_color=(1, 1, 1, 1),
                halign="center",
                on_release=self.update_just_called
            )

            # icons = IconLeftWidget(icon="android")
            # items = OneLineIconListItem(text=str(i) + ' item')
            # items.add_widget(icons)
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)
        return screen


DemoApp().run()
