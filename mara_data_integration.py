import bonobo
def extract():
    yield 'hello'
    yield 'world'

def transform(*args):
    yield tuple(
        map(str.title, args)
    )

def load(*args):
    print(*args)