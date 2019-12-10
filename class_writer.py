import binascii

class jcompiler:
    CLASS_TAG = binascii.unhexlify('07')
    UTF_TAG = binascii.unhexlify('01')
    JAVA8HEADER = binascii.unhexlify('cafebabe00000034')
    const_pool_size = 1


    def open_file(self, target):
        self.target_file = open(target, "wb")

    def close_file(self):
        self.target_file.close()

    def writeHeader(self):
        if not self.target_file.closed:
            target_file.write(self.JAVA8HEADER)

    def gen_class(self, name):
        self.const_pool_size += 1
        result = self.CLASS_TAG + self.const_pool_size.to_bytes(2, byteorder="big")
        result = self.UTF_TAG + len(name).to_bytes(2, byteorder="big")
        for element in name:
            toadd = ord(element).to_bytes(1, byteorder="big")
            result += toadd
            print(toadd)
        self.const_pool_size += 1
        if not self.target_file.closed:
            self.target_file.write(result)

compiler = jcompiler()
compiler.open_file("testclass")
compiler.gen_class("helloworld")

