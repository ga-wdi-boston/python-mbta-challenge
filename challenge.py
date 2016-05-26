red_line = ['south station', 'park st', 'kendall', 'central', 'harvard', 'porter', 'davis', 'alewife']
green_line = ['haymarket', 'government center', 'park st', 'bolyston', 'arlington', 'copley']
orange_line = ['north station', 'haymarket', 'park st', 'state', 'downtown crossing', 'chinatown', 'back bay', 'forest hills']

def totalStops(startLine, startStop, endLine, endStop):
    if startLine == endLine:
        result = abs(startLine.index(startStop) - endLine.index(endStop))
        print(result)
        return result
    else:
        startLength = abs(startLine.index(startStop) - startLine.index('park st'))
        endLength = abs(endLine.index('park st') - endLine.index(endStop))
        result = startLength + endLength
        print(result)
        return result
