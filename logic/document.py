class Document(object):

    def __init__(self, title: str = 'title', author: str = 'author', theme: str = 'theme', leaves: str = 'Leaves',
                 last_author: str = 'Last_author'):
        self._title = title
        self._author = author
        self._last_author = last_author
        self._theme = theme
        self._leaves = leaves

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author

    @property
    def last_author(self) -> str:
        return self._last_author

    @last_author.setter
    def last_author(self, last_author: str):
        self._last_author = last_author

    @property
    def theme(self) -> str:
        return self._theme

    @theme.setter
    def theme(self, theme: str):
        self._theme = theme

    @property
    def leaves(self) -> str:
        return self._leaves

    @leaves.setter
    def leaves(self, leaves: str):
        self._theme = leaves

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4})'.format(self._title, self._author, self._theme, self._leaves,
                                                  self._last_author)


if __name__ == '__main__':
    lib = Document(title="Hola", author="kevin", theme="accion", leaves="100", last_author="martinez")
    print(lib)

