from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window

from random import randint


class Particle(Widget):
    v_x = NumericProperty(0)  # скорости x и y + размер шарика
    v_y = NumericProperty(0)
    particle_size = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Particle, self).__init__(**kwargs)
        self.particle_size = randint(20, 80)
        self.v_x = randint(-1, 1) * 0.5
        self.v_y = randint(-1, 1) * 0.5

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

        if self.x < 0 or self.right > Window.width:
            self.v_x *= -1
        if self.y < 0 or self.top > Window.height:
            self.v_y *= -1


class ParticleBackground(Widget):
    def __init__(self, **kwargs):
        super(ParticleBackground, self).__init__(**kwargs)
        self.particles = []
        Clock.schedule_once(self.create_particles, 0.1)

    def create_particles(self, dt):
        for i in range(12):
            particle = Particle()
            particle.x = randint(0, int(Window.width - 80))
            particle.y = randint(0, int(Window.height - 80))
            self.particles.append(particle)
            self.add_widget(particle)
        Clock.schedule_once(self.update_particles, 1 / 65)

    def update_particles(self, dt):
        for particle in self.particles:
            particle.x += particle.velocity_x * dt
            particle.y += particle.velocity_y * dt
