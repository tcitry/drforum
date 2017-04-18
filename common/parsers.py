import logging
from rest_framework.parsers import BaseParser

logger = logging.getLogger(__name__)


class PrintParser(BaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        data = stream.read()
        print('*' * 40)
        print(data)
        print('*' * 40)
