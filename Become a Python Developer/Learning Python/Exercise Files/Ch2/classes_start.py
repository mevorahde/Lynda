#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("my_class method1")

    def method2(self, some_string):
        print("my_class method2 " + some_string)


class secondClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("secondClass method1")

  def method2(self):
    print ("secondClass method2")


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = secondClass()
    c2.method1()
    c2.method2()


if __name__ == "__main__":
    main()
