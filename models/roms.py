import os
import re
import subprocess

from os.path import isfile, join
from .pyrominfo import RomInfo
from .pyrominfo import genesis
from gi.repository import Gtk

class RomManager():
    def getRomList(self, rom_dir):
        """ Returns list with Title and Publisher for each ROM in
            provided directory."""

        rom_files = [file for file in os.listdir(rom_dir) if isfile(join(rom_dir, file))]
        rom_list = []

        for rom in rom_files:
            props = RomInfo.parse(rom_dir + rom)
            if props:
                rom_list.append([
                    self.format_title(props["title"], rom),
                    props["publisher"],
                    rom,
                ])
            else:
                rom_list.append([
                    rom,
                    "Unknown",
                    rom,
                ])

        rom_list = sorted(rom_list, key=self.getKey)

        #Convert data to ListStore
        roms_list_store = Gtk.ListStore(str, str, str)

        for rom in rom_list:
            roms_list_store.append(list(rom))

        return roms_list_store


    def getKey(self, item):
        return item[0]


    def format_title(self, title, rom):
        """ROM headers tend to have all caps and/or
            extra spaces in the title. This cleans them
            up before listing"""
        if title != "":
            title = title.title()
            title = re.sub(' +',' ',title)
        else:
            title = rom

        return title


    def start_dgen(self, tree_view, path, column, rom_info):
        options = "-f"
        rom_dir = rom_info[1]
        model, row = rom_info[0].get_selected()

        if row is not None:
            rom = str(model[row][2])
            subprocess.call(["dgen",options, "%s%s" % (rom_dir, rom)])
        else:
            return "File not found"
