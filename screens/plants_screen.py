from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class PlantsScreen(Screen):
    def on_enter(self):
        self.load_plants()

    def load_plants(self):
        try:
            from models.plant import PlantManager
            manager = PlantManager()
            plants_data = manager.get_all_plants()
            self.display_plants(plants_data)
        except Exception as e:
            self.ids.plants_container.clear_widgets()
            label = Label(
                text='Ошибка загрузки данных',
                color=[0.7, 0.7, 0.7, 1],
                font_size='16sp'
            )
            self.ids.plants_container.add_widget(label)

    def display_plants(self, plants_data):
        self.ids.plants_container.clear_widgets()

        for plant in plants_data:
            plant_card = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=180,
                padding=15,
                spacing=10
            )

            title_layout = BoxLayout(orientation='horizontal')
            name_label = Label(
                text=plant.name,
                color=[1, 1, 1, 1],
                font_size='18sp',
                bold=True,
                size_hint_x=0.7
            )
            type_label = Label(
                text=plant.type,
                color=[0.2, 0.8, 0.6, 1],
                font_size='14sp',
                size_hint_x=0.3
            )
            title_layout.add_widget(name_label)
            title_layout.add_widget(type_label)

            desc_label = Label(
                text=plant.description,
                color=[0.9, 0.9, 0.9, 1],
                font_size='12sp',
                text_size=(None, None),
                halign='left',
                valign='top'
            )
            desc_label.bind(texture_size=desc_label.setter('size'))

            watering_layout = BoxLayout(orientation='horizontal', height=30)
            watering_label = Label(
                text='Полив:',
                color=[0.7, 0.7, 0.7, 1],
                font_size='12sp',
                size_hint_x=0.3
            )
            watering_info = Label(
                text=plant.watering,
                color=[1, 1, 1, 1],
                font_size='12sp',
                size_hint_x=0.7
            )
            watering_layout.add_widget(watering_label)
            watering_layout.add_widget(watering_info)

            features_label = Label(
                text=f"Особенности: {plant.features}",
                color=[0.8, 0.8, 0.8, 1],
                font_size='11sp'
            )

            plant_card.add_widget(title_layout)
            plant_card.add_widget(desc_label)
            plant_card.add_widget(watering_layout)
            plant_card.add_widget(features_label)

            self.ids.plants_container.add_widget(plant_card)