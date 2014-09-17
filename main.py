"""
Main module of the Speedometer app.
"""

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock, mainthread
from plyer import gps

from speed import Speed
from settingsjson import settings_json


class RootLayout(FloatLayout):
    pass


class SpeedometerApp(App):

    gps_speed = NumericProperty(0.0)
    highest_speed = NumericProperty(0.0)
    gps_status = StringProperty()
    highest_speed_float = 0.00

    def reset_highest_speed(self):
        self.highest_speed = 0.00
        self.highest_speed_float = 0.00

    def build_config(self, config):
        config.setdefaults('preferences', {'unit': 'km/h'})

    def build_settings(self, settings):
        settings.add_json_panel('Speed preferences',
                                self.config,
                                data=settings_json)

    def gps_start(self):
        self.gps_status = 'Loading gps status'
        self.gps_root.start()

    def gps_stop(self):
        self.gps_status = ''
        self.gps_root.stop()

    def build(self):
        self.use_kivy_settings = False
        self.gps_root = gps
        try:
            self.gps_root.configure(on_location=self.on_location,
                                    on_status=self.on_status)
            return RootLayout()
        except NotImplementedError:
            popup = Popup(title="GPS Error",
                          content=Label(
                              text="GPS not configured...")).open()
            Clock.schedule_once(lambda d: popup.dismiss(), 3)

    @mainthread
    def on_location(self, **kwargs):
        speed = Speed(float(kwargs['speed']))
        if speed > self.highest_speed_float:
            self.highest_speed_float = speed
        self.gps_speed = speed.kmh
        self.highest_speed = Speed(self.highest_speed_float).kmh

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        self.gps_stop()
        return True

if __name__ == '__main__':
    SpeedometerApp().run()
