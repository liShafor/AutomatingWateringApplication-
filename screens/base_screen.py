# # Базовый класс экрана
# from kivy.uix.screenmanager import Screen
# from kivy.properties import StringProperty, ObjectProperty
#
#
# class BaseScreen(Screen):
#     title = StringProperty("")
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.app = None
#
#     def on_enter(self):
#         print(f"Открыт экран: {self.name}")
#
#     def on_leave(self):
#         pass
#
#     def navigation_to(self, screen_name, direction='left'):
#         if self.manager:
#             self.manager.switch_to(screen_name, direction)
