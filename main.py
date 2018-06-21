import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from models.roms import RomManager
from views.roms import RomsView
from views.settings import SettingsView

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dgen")

        if Gdk.Screen.get_default().get_height() < 800:
            self.maximize()
        else:
            self.set_size_request(950, 700)

        main_box = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL,
        )
        left_sidebar = self.sidebar()
        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        content_window = self.content_window()

        left_sidebar.get_style_context().add_class("bg")

        main_box.pack_start(left_sidebar, False, False, 0)
        main_box.pack_start(separator, False, False, 0)
        main_box.pack_start(content_window, True, True, 0)

        self.load_css()
        self.add(main_box)

        roms_view = RomsView(self)
        Gtk.Window.set_title(self,"Dgen - ROMS")


    def sidebar(self):
        left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.listbox.connect("row_activated", self._on_select_row)

        rom_manager = RomManager()
        roms_row = Gtk.ListBoxRow(name="roms")
        roms_label = Gtk.Label("ROMS")
        roms_row.add(roms_label)
        self.listbox.add(roms_row)
        roms_row.get_style_context().add_class("side-options")

        settings_row = Gtk.ListBoxRow(name="settings")
        settings_label = Gtk.Label("Settings")
        settings_row.add(settings_label)
        self.listbox.add(settings_row)
        settings_row.get_style_context().add_class("side-options")

        left_box.add(self.listbox)

        return left_box


    def content_window(self):
        content_box = Gtk.ScrolledWindow()

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_transition_duration(500)
        content_box.add(self.stack)

        return content_box


    def _on_select_row(main_window, listbox, row):
        if row:
            row_name = row.get_child().get_text()
            Gtk.Window.set_title(main_window,"Dgen - %s" % row_name)

            if row_name == "ROMS":
                rom_view = RomsView(main_window)

            elif row_name == "Settings":
                settings_view = SettingsView(main_window)


    def load_css(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        screen = Gdk.Screen.get_default()
        context = Gtk.StyleContext()
        context.add_provider_for_screen(screen, css_provider,
                                Gtk.STYLE_PROVIDER_PRIORITY_USER)



win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
