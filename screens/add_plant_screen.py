from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from models.plant import Plant, PlantManager


class AddPlantScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plant_manager = PlantManager()

        self.name_ti = None
        self.type_ti = None
        self.description_ti = None
        self.watering_ti = None
        self.features_ti = None

        self.create_form()

    def create_form(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title_label = Label(
            text='Добавить новое растение',
            font_size='24sp',
            bold=True,
            color=[1, 1, 1, 1],
            size_hint_y=0.1
        )

        scroll = ScrollView()
        form_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))

        name_layout, self.name_ti = self.create_text_input('Название растения*', hint_text='Например: Монстера')
        type_layout, self.type_ti = self.create_text_input('Тип растения*',
                                                           hint_text='Например: Декоративный, Цветущий')
        desc_layout, self.description_ti = self.create_text_area('Описание растения*', hint_text='Опишите растение...')
        watering_layout, self.watering_ti = self.create_text_area('Режим полива*',
                                                                  hint_text='Например: Умеренный полив 2 раза в неделю')
        features_layout, self.features_ti = self.create_text_area('Особенности ухода*',
                                                                  hint_text='Требования к свету, влажности и т.д.')

        form_layout.add_widget(name_layout)
        form_layout.add_widget(type_layout)
        form_layout.add_widget(desc_layout)
        form_layout.add_widget(watering_layout)
        form_layout.add_widget(features_layout)

        scroll.add_widget(form_layout)

        # Кнопки
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.15)

        cancel_btn = Button(
            text='Отмена',
            background_color=[0.8, 0.2, 0.2, 1],
            bold=True,
            font_size='16sp',
            color=[1, 1, 1, 1],
            on_press=self.go_back
        )

        save_btn = Button(
            text='Сохранить',
            background_color="#0aff9f",
            bold=True,
            font_size='16sp',
            color=[1, 1, 1, 1],
            on_press=self.save_plant
        )

        buttons_layout.add_widget(cancel_btn)
        buttons_layout.add_widget(save_btn)

        main_layout.add_widget(title_label)
        main_layout.add_widget(scroll)
        main_layout.add_widget(buttons_layout)

        self.add_widget(main_layout)

    def create_text_input(self, label_text, hint_text=''):
        layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=80)

        label = Label(
            text=label_text,
            font_size='14sp',
            bold=True,
            color=[0.9, 0.9, 0.9, 1],
            size_hint_y=None,
            height=30
        )

        text_input = TextInput(
            multiline=False,
            hint_text=hint_text,
            background_color=[0.1, 0.1, 0.1, 1],
            foreground_color=[1, 1, 1, 1],
            cursor_color=[1, 1, 1, 1],
            size_hint_y=None,
            height=40
        )

        layout.add_widget(label)
        layout.add_widget(text_input)
        return layout, text_input  # Возвращаем и layout, и text_input

    def create_text_area(self, label_text, hint_text=''):
        layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=120)

        label = Label(
            text=label_text,
            font_size='14sp',
            bold=True,
            color=[0.9, 0.9, 0.9, 1],
            size_hint_y=None,
            height=30
        )

        text_input = TextInput(
            multiline=True,
            hint_text=hint_text,
            background_color=[0.1, 0.1, 0.1, 1],
            foreground_color=[1, 1, 1, 1],
            cursor_color=[1, 1, 1, 1],
            size_hint_y=None,
            height=80
        )

        layout.add_widget(label)
        layout.add_widget(text_input)
        return layout, text_input

    def go_back(self, instance):
        self.manager.current = 'plants'
        self.clear_form()

    def clear_form(self):
        if self.name_ti:
            self.name_ti.text = ''
        if self.type_ti:
            self.type_ti.text = ''
        if self.description_ti:
            self.description_ti.text = ''
        if self.watering_ti:
            self.watering_ti.text = ''
        if self.features_ti:
            self.features_ti.text = ''

    def save_plant(self, instance):
        name = self.name_ti.text.strip() if self.name_ti else ''
        plant_type = self.type_ti.text.strip() if self.type_ti else ''
        description = self.description_ti.text.strip() if self.description_ti else ''
        watering = self.watering_ti.text.strip() if self.watering_ti else ''
        features = self.features_ti.text.strip() if self.features_ti else ''

        if not all([name, plant_type, description, watering, features]):
            self.show_error('Все поля обязательны для заполнения!')
            return

        existing_plant = self.plant_manager.get_plant_by_name(name)
        if existing_plant:
            self.show_error(f'Растение "{name}" уже существует!')
            return

        new_plant = {
            "name": name,
            "type": plant_type,
            "description": description,
            "watering": watering,
            "features": features
        }

        self.plant_manager.plants.append(Plant(**new_plant))
        self.plant_manager.save_plants()

        self.show_success(f'Растение "{name}" успешно добавлено!')
        self.clear_form()
        self.manager.current = 'plants'
        self.manager.get_screen('plants').on_enter()

    def show_error(self, message):
        print(f"Ошибка: {message}")

    def show_success(self, message):
        print(f"Успешно: {message}")