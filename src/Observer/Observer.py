from ..Listener import IListener

class Observer():
    def __init__(self):
        self.__listeners: list[IListener] = []
        pass

    def subscribe(self, s):
        if s not in self.__listeners:
            self.__listeners.append(s)
    
    def unsubscribe(self, s):
        if s in self.__listeners:
            self.__listeners.remove(s)
    
    def notify(self):
        for s in self.__listeners:
            s.update()
