from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image


class BackButton(ButtonBehavior, Label):
    pass


class RoundedButton(ButtonBehavior, Label):
    pass


class ImageButton(ButtonBehavior, Image):
    pass