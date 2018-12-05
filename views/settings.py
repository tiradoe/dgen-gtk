import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.settings import SettingsManager

class SettingsView():
    def __init__(self):
        self.user_settings = SettingsManager().get_user_settings()


    def generate_view(self):
        settings_box = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
        )

        file_chooser_label = Gtk.Label("Choose ROM directory: ")
        choose_romdir_button = Gtk.FileChooserButton()
        choose_romdir_button.set_action(Gtk.FileChooserAction.SELECT_FOLDER)

       	label = Gtk.Label()

        #for setting, value in self.user_settings.items():
        #    print(setting, value)


        label.set_text(self.user_settings['rom_directory'])
        label.set_justify(Gtk.Justification.LEFT)

        settings_box.pack_start(file_chooser_label, False, False, 0)
        settings_box.pack_start(choose_romdir_button, False, False, 0)
        settings_box.pack_start(label, False, False, 0)

        return settings_box
