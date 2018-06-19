import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from models.roms import RomManager
from pathlib import Path

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

        self.load_rom_view()
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


    def _on_select_row(self, listbox, row):
        if row:
            row_name = row.get_child().get_text()
            Gtk.Window.set_title(self,"Dgen - %s" % row_name)

            if row_name == "ROMS":
                self.load_rom_view()

            elif row_name == "Settings":
                self.load_settings_view()


    def load_rom_view(self):
        home_path = str(Path.home())
        rom_dir = "%s/Games/Genesis/" % home_path
        rom_manager = RomManager()
        row_name = "ROMS"

        if rom_dir != "":
            roms = rom_manager.getRomList(rom_dir)
        else:
            roms = Gtk.ListStore(str,str,str)

        tree_view = Gtk.TreeView(roms)

        for i, col_title in enumerate(["Title", "Publisher", "Filename"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            column.set_sort_column_id(i)
            tree_view.append_column(column)

        selected_row = tree_view.get_selection()
        rom_info = [selected_row, rom_dir]

        tree_view.connect("row_activated", rom_manager.start_dgen, rom_info)

        self.stack.add_named(tree_view, row_name)

        tree_view.show()
        self.stack.set_visible_child(tree_view)


    def load_settings_view(self):
        row_name = "Settings"
        settings_box = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
        )

        file_chooser_label = Gtk.Label("Choose ROM directory: ")
        choose_romdir_button = Gtk.FileChooserButton()

        settings_box.pack_start(file_chooser_label, True, True, 0)
        settings_box.pack_start(choose_romdir_button, False, False, 0)

        self.stack.add_named(settings_box, row_name)

        settings_box.show()
        self.stack.set_visible_child(settings_box)


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
