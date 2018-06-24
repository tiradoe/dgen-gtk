import gi
from pathlib import Path

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.roms import RomManager

class RomsView():
    def __init__(self):
        self.home_path = str(Path.home())
        self.rom_dir = "%s/Games/Genesis/" % self.home_path
        self.rom_manager = RomManager()
        self.row_name = "ROMS"

        self.generate_view()



    def generate_view(self):
        if self.rom_dir != "":
            roms = self.rom_manager.getRomList(self.rom_dir)
        else:
            roms = Gtk.ListStore(str,str,str)

        rom_list = Gtk.TreeView(roms)

        for i, col_title in enumerate(["Title", "Publisher", "Filename"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            column.set_sort_column_id(i)
            rom_list.append_column(column)

        selected_row = rom_list.get_selection()
        rom_info = [selected_row, self.rom_dir]

        rom_list.connect("row_activated", self.rom_manager.start_dgen, rom_info)

        return rom_list
