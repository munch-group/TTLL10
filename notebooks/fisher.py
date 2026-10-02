import sys
import scipy.stats

def fisher_test(one, other, background, min_dist=None, return_counts=False):

    a, b = one, other
    a, b, background = set(a), set(b), set(background)

    not_in_background = a.union(b).difference(background)
    if not_in_background:
        print(f'Removed {len(not_in_background)} genes not in background set', file=sys.stderr)
    if min_dist is not None:
        try:
            a = one._distance_prune(other, *min_dist)
        except AttributeError as e:
            print('Distance pruning only works for GeneList objects.')
            raise e
        
    M = len(background) 
    N = len(background.intersection(a))
    n = len(background.intersection(b))
    x = len(background.intersection(a).intersection(b))
    table = [[  x,           n - x          ],
            [ N - x,        M - (n + N) + x]]
    if return_counts:
        return float(scipy.stats.fisher_exact(table, alternative='greater').pvalue), table
    return float(scipy.stats.fisher_exact(table, alternative='greater').pvalue)  