class HashTable:
    def __init__(self):
        self.collection={}
    def hash(self,string):
        hashed=0
        for char in string:
            hashed+=ord(char)
        return hashed
    def add(self,key,value):
        hashed=self.hash(key)
        if hashed in self.collection:
            self.collection[hashed][key]=value
        else:
            self.collection[hashed]={key:value}
        return self.collection
    def remove(self,key):
        hashed=self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].pop(key)
    def lookup(self,key):
        hashed=self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]
        else:
            return
obj=HashTable()
obj.add("abc","value")
obj.add("abd","value2")
obj.add("xyz","value3")
obj.remove("abc")
print(obj.lookup("abc"))

