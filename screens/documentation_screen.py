from kivy.uix.screenmanager import Screen
import webbrowser


class DocumentationScreen(Screen):
    def open_tech_docs(self):
        """Через webbrowser реализация перехода к доке проекта"""
        print("Открытие технической документации")

    def open_presentation(self):
        print("Открытие презентации проекта")
