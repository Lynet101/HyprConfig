import pandas as pd

class data_prep():
    def __init__(self):
        self.file_content=[]
        self.open_file()
        self.cleanup_data()


    def open_file(self):
        with open("/home/slindau/.config/hypr/hyprland.conf") as f:
            for line in f:
                self.file_content.append(line)

    def cleanup_data(self):
        for ind, i in enumerate(self.file_content):
            if i.startswith("#"):
                self.file_content.pop(ind)

class data_segmenter:
    def __init__(self, data):
        self.data = data
        self.bind()
    
    def bind(self):
        binds_list = []
        for i in self.data:
            if i.startswith("bind") or i.startswith("binde"):
                binds_list.append(i.replace("binde", "e|,").replace("bindm", "m|,").replace("bind", "n|,").replace("=", "").replace("\n", ""))
        self.binds = pd.DataFrame([i.split(',') for i in binds_list], columns=['Bind Class', 'Main Key(s)', 'Second Key(s)', 'Command', 'Argument(s)'])

def main():
    raw_data = data_prep().file_content
    segmented_data=data_segmenter(raw_data)
    
    binds=segmented_data.binds
    print(binds)
    
if __name__ == '__main__':
    main()