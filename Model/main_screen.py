class MainScreenModel:
    def __init__(self):
        self._observer = []

    def notify_observer(self):
        for observer in self._observer:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observer.append(observer)

    def remove_observer(self, observer):
        self._observer.remove(observer)
