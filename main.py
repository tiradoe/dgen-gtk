#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from models.roms import RomManager
from views.roms import RomsView
from views.settings import SettingsView

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        if Gdk.Screen.get_default().get_height() < 800:
            self.maximize()
        else:
            self.set_size_request(950, 700)

        main_box = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
        )

        rom_view = RomsView().generate_view()
        settings_view = SettingsView().generate_view()

        content_window = self.content_window()
        content_window.add_titled(rom_view, "rom_view", "ROMS")
        content_window.add_titled(settings_view, "settings_view", "Settings")

        header_bar = self.header_bar(content_window)
        self.set_titlebar(header_bar)


        main_box.pack_start(content_window, True, True, 0)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(main_box)

        self.add(scrolled_window)


    def header_bar(self, content_window):
        tab_switcher = Gtk.StackSwitcher(can_focus=False)
        tab_switcher.set_stack(content_window)

        header_bar = Gtk.HeaderBar()
        header_bar.set_custom_title(tab_switcher)
        header_bar.set_show_close_button(True)

        return header_bar


    def content_window(self):
        content_box = Gtk.Stack()

        content_box.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        content_box.set_transition_duration(500)

        return content_box


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
