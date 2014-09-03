from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from plyer import gps


class Root(FloatLayout):
    pass


class Speedometer(App):

    gps_speed = StringProperty("Speed...")
    highest_speed = StringProperty("Highest speed")
    gps_status = StringProperty('Click Start to get GPS speed updates')
    highest_speed_float = 0.0

    def gps_start(self):
        self.gps_root.start()

    def gps_stop(self):
        self.gps_root.stop()

    def build(self):
        self.gps_root = gps
        try:
            self.gps_root.configure(on_location=self.on_location,
                                    on_status=self.on_status)
        except NotImplementedError:
            popup = Popup(title="GPS Error",
                          content=Label(
                              text="GPS not configured...")).open()
            Clock.schedule_once(lambda d: popup.dismiss(), 3)
        return Root()

    @mainthread
    def on_location(self, **kwargs):
        speed = float(kwargs['speed']) * 3.6
        if speed > self.highest_speed_float:
            self.highest_speed_float = speed
        self.gps_speed = "Speed: {:.2f} km/h".format(speed)
        self.highest_speed = "Highest speed: {:.2f} km/h".format(
            self.highest_speed_float)

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

if __name__ == '__main__':
    Speedometer().run()
