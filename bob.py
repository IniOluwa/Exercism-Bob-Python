#
# Skeleton file for the Python "Bob" exercise.
#
import re


def hey(what):
    what = what.encode('utf-8')
    the_phrase = what
    what = re.sub(' ', '', the_phrase, re.I)
    what = what.replace(' ', '')

    if len(what) > 1:
        last = what[len(what) - 1]
        pre_last = what[len(what) - 2]

        if '!' in what and last == '?':
            if what.index('!') < what.index('?'):
                return 'Sure.'
        elif pre_last.isupper() and last == '?':
            return 'Whoa, chill out!'
        elif last == '?':
            return 'Sure.'

        calm = [x for x in what.decode('utf-8', 'ignore') if x.islower()]
        if calm:
            return 'Whatever.'

        if last == '!' or last.isupper():
            return 'Whoa, chill out!'
        else:
            return 'Whatever.'

    else:
        return 'Fine. Be that way!'
