'''Binomial Test
Example of a one-and two-sided binomial test. Taken from Wikipedia
http://en.wikipedia.org/wiki/Binomial_test
'''

'''
Author: Thomas Haslwanter
Date:   July 2013
Ver:    1.0
'''

from scipy import stats

def binomial_test(checkVal):
    '''Binomial Test'''
    
    # Set the parameters
    n = 235
    p = 1/6.
    
    
    # Calculate the on-sided test, i.e. the likelihood that you get the same or more times of "6"
    bd = stats.binom(n,p)
    p_oneTail = bd.sf(checkVal-1)   # how many values are "higher than" checkVal-1
    
    # Calculate the two-sided test, i.e. how many cases "as extreme or more" than the given case are likely to occur by chance:
    p_twoTail = stats.binom_test(checkVal, n, p)
    
    return (p_oneTail, p_twoTail)

#----------------------------------------------------------------------
if __name__ == '__main__':

    checkVal = 51
    p1, p2 = binomial_test(checkVal)
    print(('The chance that you roll {0} or more "6" is {1}, and the chance of an event as extreme as {0} or more rolls is {2}'.format(checkVal, p1, p2)))