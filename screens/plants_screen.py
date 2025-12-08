from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


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
            print(f"Ошибка загрузки растений: {e}")
            self.ids.plants_container.clear_widgets()
            label = Label(
                text='Ошибка загрузки данных',
                color=[0.7, 0.7, 0.7, 1],
                font_size='16sp'
            )
            self.ids.plants_container.add_widget(label)

    def display_plants(self, plants_data):
        self.ids.plants_container.clear_widgets()

        add_button = Button(
            text='+ Добавить новое растение',
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=[0.2, 0.6, 0.4, 1],
            color=[1, 1, 1, 1],
            font_size='16sp',
            bold=True,
            on_press=self.go_to_add_plant
        )
        self.ids.plants_container.add_widget(add_button)

        separator = BoxLayout(size_hint_y=None, height=10)
        self.ids.plants_container.add_widget(separator)

        if not plants_data:
            empty_label = Label(
                text='Растения не найдены. Добавьте первое растение!',
                color=[0.7, 0.7, 0.7, 1],
                font_size='16sp',
                size_hint_y=None,
                height=100
            )
            self.ids.plants_container.add_widget(empty_label)
            return

        screen_width = Window.width - 30  # минус padding

        for plant in plants_data:
            plant_card = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=200,
                padding=15,
                spacing=5
            )

            title_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)

            name_label = Label(
                text=plant.name,
                color=[1, 1, 1, 1],
                font_size='18sp',
                bold=True,
                size_hint_x=0.6,
                text_size=(screen_width * 0.6 - 10, None),
                halign='left',
                valign='middle',
                shorten=True,
                shorten_from='right'
            )

            type_label = Label(
                text=plant.type,
                color=[0.2, 0.8, 0.6, 1],
                font_size='14sp',
                size_hint_x=0.4,
                text_size=(screen_width * 0.4 - 10, None),
                halign='right',
                valign='middle',
                shorten=True,
                shorten_from='right'
            )

            title_layout.add_widget(name_label)
            title_layout.add_widget(type_label)

            desc_label = Label(
                text=plant.description,
                color=[0.9, 0.9, 0.9, 1],
                font_size='13sp',
                size_hint_y=None,
                text_size=(screen_width, None),
                halign='left',
                valign='top',
                shorten=False
            )
            desc_label.bind(texture_size=self.update_desc_height)

            # Полив
            watering_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=25)
            watering_label = Label(
                text='Полив:',
                color=[0.7, 0.7, 0.7, 1],
                font_size='13sp',
                bold=True,
                size_hint_x=0.3
            )
            watering_info = Label(
                text=plant.watering,
                color=[1, 1, 1, 1],
                font_size='13sp',
                size_hint_x=0.7,
                text_size=(screen_width * 0.7 - 10, None),
                halign='left',
                valign='middle',
                shorten=True,
                shorten_from='right'
            )
            watering_layout.add_widget(watering_label)
            watering_layout.add_widget(watering_info)

            features_label = Label(
                text=f"Особенности: {plant.features}",
                color=[0.8, 0.8, 0.8, 1],
                font_size='12sp',
                size_hint_y=None,
                text_size=(screen_width, None),
                halign='left',
                valign='top',
                shorten=False
            )
            features_label.bind(texture_size=self.update_features_height)

            plant_card.add_widget(title_layout)
            plant_card.add_widget(desc_label)
            plant_card.add_widget(watering_layout)
            plant_card.add_widget(features_label)

            self.ids.plants_container.add_widget(plant_card)

    def update_desc_height(self, instance, value):
        """Обновляет высоту виджета описания в зависимости от текста"""
        if instance.texture_size[1]:
            instance.height = min(instance.texture_size[1], 80)

    def update_features_height(self, instance, value):
        """Обновляет высоту виджета особенностей в зависимости от текста"""
        if instance.texture_size[1]:
            instance.height = min(instance.texture_size[1], 60)

    def go_to_add_plant(self, instance):
        self.manager.current = 'add_plant'