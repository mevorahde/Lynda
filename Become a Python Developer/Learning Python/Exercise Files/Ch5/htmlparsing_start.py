# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encounter comment: {}".format(data))
        pos = self.getpos()
        print("\tAt line: {} position {}".format(pos[0], pos[1]))

    def handle_startendtag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encounter tag: {}".format(tag))
        pos = self.getpos()
        print("\tAt line: {} position {}".format(pos[0], pos[1]))

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encounter tag: {}".format(tag))
        pos = self.getpos()
        print("\tAt line: {} position {}".format(pos[0], pos[1]))

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encounter data: {}".format(data))
        pos = self.getpos()
        print("\tAt line: {} position {}".format(pos[0], pos[1]))


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

    print("Meta tags found: {}".format(metacount))

if __name__ == "__main__":
    main();
