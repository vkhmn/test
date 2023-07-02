import json
import os


class Meta:
    def __init__(self, params=None):
        if self._validate_params(params):
            self.params = params

    def _check_url_length(self):
        """Length must be less 4000 symbols"""
        return True

    def _create_url(self):
        return ''

    def _validate_params(self, params):
        return True

    def get_curl(self):
        return 'Get info from META'

    def __str__(self):
        return repr(self.params)


def main():
    while True:
        filename = input('Enter filename with params: ')
        if os.path.exists(filename):
            break
        print(f'File <{filename}> not exists!')

    with open(filename) as f:
        try:
            res = json.load(f)
        except json.decoder.JSONDecodeError:
            print('Bad JSON file')
            main()
        else:
            meta = Meta(params=res)
            print(meta.get_curl())
            print(meta)


if __name__ == '__main__':
    main()

