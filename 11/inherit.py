from myfile import MyFile


class TextFile(MyFile):

    @property
    def contents(self):
        return open(self.get_fname(), 'rt').read()

    @contents.setter
    def contents(self, value):
        if not value.endswith("\n"):
            value += "\n"
        open(self.get_fname(), 'at').write(value)


class BinFile(MyFile):

    @property
    def contents(self):
        return open(self.get_fname(), 'rb').read().decode()

    @contents.setter
    def contents(self, value):
        if isinstance(value, int):
            out = struct.pack("i", value)
        open(self.get_fname(), 'ab').write(value.encode())


if __name__ == '__main__':
    import os
    script_dir = os.path.dirname(__file__)
    file1path = os.path.join(script_dir, 'file1.txt')
    file1 = TextFile(file1path)
    print(file1, len(file1))
    print(file1.contents)
    file1.contents = "blah"
    print(file1.contents)
    file2path = os.path.join(script_dir, 'file2.dat')
    file2 = BinFile(file2path)
    print(file2, len(file2))
    print(file2.contents)
    file2.contents = "blah"
    print(file2.contents)
