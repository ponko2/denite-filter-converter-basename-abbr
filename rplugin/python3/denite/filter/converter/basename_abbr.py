from os.path import split

from denite.base.filter import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'converter/basename_abbr'
        self.description = 'convert candidate abbr to basename'

    def filter(self, context):
        for candidate in context['candidates']:
            dirname, basename = split(candidate['word'])
            if basename:
                candidate['abbr'] = ' '.join([basename, dirname])
        return context['candidates']
