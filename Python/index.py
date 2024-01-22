'''Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
 returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
returns 'Bart'

namelist([])
returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

behaviours(user stories) 
solution 1'''
def format_names(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                 names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

# Example Usage
name_list = [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}]
result = format_names(name_list)
print(result)
# Output: 'Alice, Bob & Charlie'


#solution 2
def namelist(names):
    onlyName = []
    for item in names:
        onlyName.append(item.get('name'))

    if len(onlyName) == 0 :
        return ""
    elif len(onlyName) == 1:
        return onlyName[0]
    elif len(onlyName) == 2:
        return ' & '.join(onlyName)
    else:
        partOne = onlyName[0:len(onlyName)-2]
        partTwo = onlyName[len(onlyName)-2 : len(onlyName)]
        p1 = ', '.join(partOne)
        p2 = ' & '.join(partTwo)
        p = [p1, p2]
        return ', '.join(p)
