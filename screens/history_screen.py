from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from models.watering_history import HistoryManager


class HistoryScreen(Screen):
    def on_enter(self):
        self.load_history()

    def load_history(self):
        try:
            manager = HistoryManager()
            history_data = manager.get_all_records()
            self.display_history(history_data)
        except Exception as e:
            print(f"Ошибка в load_history: {e}")
            self.ids.history_container.clear_widgets()
            label = Label(
                text='Ошибка загрузки истории',
                color=[0.7, 0.7, 0.7, 1],
                font_size='16sp'
            )
            self.ids.history_container.add_widget(label)

    def display_history(self, history_data):
        self.ids.history_container.clear_widgets()

        if not history_data:
            label = Label(
                text='История полива пуста',
                color=[0.7, 0.7, 0.7, 1],
                font_size='16sp'
            )
            self.ids.history_container.add_widget(label)
            return

        for record in history_data:
            history_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=60,
                padding=10,
                spacing=10
            )

            date_box = BoxLayout(orientation='vertical')
            date_label = Label(
                text=record.date,
                color=[1, 1, 1, 1],
                font_size='14sp',
                bold=True
            )
            time_label = Label(
                text=record.time,
                color=[0.8, 0.8, 0.8, 1],
                font_size='12sp'
            )
            date_box.add_widget(date_label)
            date_box.add_widget(time_label)

            plant_box = BoxLayout(orientation='vertical')
            plant_label = Label(
                text=record.plant,
                color=[1, 1, 1, 1],
                font_size='14sp'
            )
            status_label = Label(
                text=record.status,
                color=[0.2, 0.8, 0.6, 1],
                font_size='12sp'
            )
            plant_box.add_widget(plant_label)
            plant_box.add_widget(status_label)

            history_item.add_widget(date_box)
            history_item.add_widget(plant_box)

            self.ids.history_container.add_widget(history_item)
