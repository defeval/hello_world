choice = 'ham'
print({'spam': 1.25,
       'ham': 2.25}[choice])

branch = {'spam': 1.25, 'ham': 2.25}
print(branch.get('spam', 'True choice'))
print(branch.get('eggs', 'Bad choice'))

