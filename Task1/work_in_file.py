from Task1.parser import soup_json

filename = 'comments.txt'

class File:
    filename
    def __init__(self, filename, soup_json):
        self.filename = filename
        self.json_text = soup_json

    def fileWrite(self):
        with open(self.filename, 'a') as file_object:
            file_object.write(f'{self.json_text}')
            print("message write to file")

    def fileOpen(self):
        with open(self.filename) as file_object:
            lines = file_object.readlines()

        for line in lines:
            print(line.rstrip())


if __name__ == "__main__":
    d = File(filename, soup_json)
    d.fileWrite()
    # d.fileOpen()