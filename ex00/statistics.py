from typing import Any, Union

def ft_mean(args: list) -> float:
    '''Calculate mean'''
    if len(args) > 0:
        result:float = sum(list(args)) / len(args)
    else:
        result:float = 0.0
    return result

def ft_median(args: list) -> Union[int, float]:
    '''Calculate median'''
    sorted_args:list = sorted(args)
    result:Union[int, float] = sorted_args[int(len(sorted_args) / 2)]
    return result

def ft_quartile(args: list) -> list:
    '''Calculate quartile'''
    result:list = []
    return result


def ft_std(args: list):
    '''Calculate std'''
    pass


def ft_var(args: list):
    '''Calculate var'''
    pass


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''
Takes *args a quantity of unknown number and make the Mean, Median,
Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
ask.
    '''
    order_functions:dict = {'mean': ft_mean, 'median': ft_median, 'quartile': ft_quartile, 'std': ft_std, 'var': ft_var}
    results:dict = dict()
    validated_orders:list = list(filter(lambda x: x in order_functions.keys(), kwargs.values()))
    for order in validated_orders:
        if len(args) == 0:
            print('ERROR')
        else:
            results[order] = order_functions[order](list(args))

    list(map(lambda x: print('{} : {}'.format(x, str(results[x]))), results.keys()))
