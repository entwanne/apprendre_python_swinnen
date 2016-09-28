INDEX = 'index'

def get_index():
    with open(INDEX, 'r') as index:
        return [l.rstrip() for l in index]

def get_source_files(moder='r', modew='w'):
    for filename in get_index():
        with open(filename, moder) as f:
            content = yield f
        if content is not None:
            with open(filename, modew) as f:
                f.write(content)
            yield # send()

source_files = get_source_files()
