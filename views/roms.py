import gi
from pathlib import Path

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.roms import RomManager

class RomsView():
    def __init__(self, main_window):
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

        main_window.stack.add_named(tree_view, row_name)

        tree_view.show()
        main_window.stack.set_visible_child(tree_view)
