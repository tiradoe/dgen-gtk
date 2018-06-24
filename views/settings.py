import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SettingsView():
    def __init__(self):
        self.generate_view()


    def generate_view(self):
        settings_box = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
        )

        file_chooser_label = Gtk.Label("Choose ROM directory: ")
        choose_romdir_button = Gtk.FileChooserButton()

        settings_box.pack_start(file_chooser_label, True, True, 0)
        settings_box.pack_start(choose_romdir_button, False, False, 0)

        return settings_box
