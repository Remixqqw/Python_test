from abc import ABC, abstractmethod


class BaseSerializer(ABC): # basovii klass serealizatora
    @abstractmethod
    def dumps(self, obj) -> str: #serealizuet v stroku oni ne opredeleni potomu shto oni abstractnii class
        pass

    @abstractmethod
    def loads(self, string: str):  #serealizuet is stroki
        pass

    def dump(self, obj, source_file): #serealizuet v fail
        source_file.write(self.dumps(obj))

    def load(self, source_file): #serealizuet is faila
        return self.loads(source_file.read())
