import abc

class Database():
    __metaclass__ = abc.ABCMeta
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.con = None

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def select(self,sql):
        pass

    @abc.abstractmethod
    def insert(self,sql):
        pass

    @abc.abstractmethod
    def delete(self,sql):
        pass

    @abc.abstractmethod
    def update(self,sql):
        pass
