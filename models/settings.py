import gio
#import yaml

class SettingsManager():
    def get_user_settings(self):
        print('Getting settings')
        #with open("dgen_options.yml", 'r') as emulator_settings:
        #    cfg = yaml.load(emulator_settings)

        #return cfg['dgen_settings']


    def set_rom_directory(self):
        print("setRomDirectory")

    def get_rom_directory(self):
        print("getRomDirectory")
