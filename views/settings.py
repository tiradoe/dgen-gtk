import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SettingsView():
    def __init__(self):
        self.generate_view()


    def generate_view(self):
        romdir_box = Gtk.Box()
        fullscreen_box = Gtk.Box(spacing=50)
        settings_grid = Gtk.Grid()

        file_chooser_label = Gtk.Label("Choose ROM directory: ")
        choose_romdir_button = Gtk.FileChooserButton()

        fullscreen_label = Gtk.Label("Start in fullscreen")
        fullscreen_checkbox = Gtk.CheckButton()

        romdir_box.pack_start(file_chooser_label, True, True, 0)
        romdir_box.pack_end(choose_romdir_button, True, True, 0)

        fullscreen_box.pack_start(fullscreen_label, True, True, 0)
        fullscreen_box.pack_end(fullscreen_checkbox, True, True, 0)

        settings_grid.add(romdir_box)
        settings_grid.attach_next_to(fullscreen_box, romdir_box, Gtk.PositionType.BOTTOM,1,2)
        settings_grid.attach_next_to(fullscreen_box, romdir_box, Gtk.PositionType.BOTTOM,1,2)


        #settings_grid.attach_next_to(
        #        fullscreen_label,
        #        file_chooser_label,
        #        Gtk.PositionType.BOTTOM,
        #        1,
        #        1
        #)
        #settings_grid.attach_next_to(
        #        fullscreen_checkbox,
        #        fullscreen_label,
        #        Gtk.PositionType.RIGHT,
        #        1,
        #        1)




        return settings_grid
