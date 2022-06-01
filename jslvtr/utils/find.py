# absolute import
from jslvtr.utils.commons.file_operations import save_to_file
# relative import - TRY TO AVOID
# from .commons.file_operations import save_to_file

# this is bad! python thinks it's an absolute import!
# from commons.file_operations import save_to_file


def find_in(iterable, expected):
    for i in iterable:
        if iterable[i] == expected:
            return i
    raise ItemNotFoundError(f'{expected} not found in provided iterable.')


class ItemNotFoundError(Exception):
    pass


print(__name__)
