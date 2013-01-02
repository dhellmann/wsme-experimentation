import json
import requests

base_url = 'http://127.0.0.1:8080/'
strings_url = base_url + 'strings'
pairs_url = base_url + 'pairs'


def show_results(r):
    print 'URL :', r.url
    print 'TEXT:', repr(r.text)
    print 'JSON:', repr(r.json())
    print


print 'HTTP GET Strings, using indexes'
r = requests.get(strings_url,
                 params={'input[0]': 'a',
                         'input[1]': 'b',
                         })
show_results(r)


print 'HTTP GET Pairs, using indexes'
r = requests.get(pairs_url,
                 params={'input[0].left': 'a',
                         'input[0].right': 'A',
                         'input[1].left': 'b',
                         'input[1].right': 'B',
                         })
show_results(r)


print 'HTTP GET Strings, without indexes, one'
r = requests.get(strings_url,
                 params={'input': 'a'},
                 )
show_results(r)


print 'HTTP GET Strings, without indexes, multiple'
r = requests.get(strings_url,
                 params={'input': ['a', 'b'],
                         })
show_results(r)


print 'HTTP GET Strings, without indexes, multiple, list (BROKEN)'
r = requests.get(strings_url,
                 params=[('input', 'a'),
                         ('input', 'b'),
                         ])
show_results(r)

print 'HTTP GET Pairs, without indexes, separate lists'
r = requests.get(pairs_url,
                 params={'input.left': ['a', 'b'],
                         'input.right': ['A', 'B'],
                         })
show_results(r)

print 'HTTP GET Pairs, without indexes, hand-encoded'
r = requests.get(pairs_url +
                 '?input.left=a&input.right=A&input.left=b&input.right=B')
show_results(r)

print 'HTTP GET Pairs, without indexes, tuples (BROKEN)'
r = requests.get(pairs_url,
                 params=[('input.left', 'a'),
                         ('input.right', 'A'),
                         ('input.left', 'b'),
                         ('input.right', 'B'),
                         ],
                 )
show_results(r)

print 'HTTP GET Pairs, without indexes, nested dicts (BROKEN)'
r = requests.get(pairs_url,
                 params={'input': [{'left': 'a',
                                    'right': 'A'},
                                   {'left': 'b',
                                    'right': 'B',
                                    }],
                         })
show_results(r)

print 'HTTP GET Pairs, without indexes, nested dicts, 2 (BROKEN)'
r = requests.get(pairs_url,
                 params={'input[0]': {'left': 'a',
                                      'right': 'A'},
                         'input[1]': {'left': 'b',
                                      'right': 'B',
                                      },
                         })
show_results(r)
