__author__ = 'Ashwin'

def fibo_init():
    fibos = [1,2]
    lastfibo = 1
    currfibo = 2
    return fibos, lastfibo, currfibo


def fibo_update(lastfibo, currfibo):
    newfibo = currfibo + lastfibo
    lastfibo = currfibo
    currfibo = newfibo
    return lastfibo, currfibo


def fibos_til_value(value_ceil):
    fibos, lastfibo, currfibo = fibo_init()
    while(currfibo < value_ceil):
        lastfibo, currfibo = fibo_update(lastfibo, currfibo)
        fibos.append(currfibo)
    return fibos

def fibos_til_count(count_ceil):
    fibos, lastfibo, currfibo = fibo_init()
    while(len(fibos) < count_ceil):
        lastfibo, currfibo = fibo_update(lastfibo, currfibo)
        fibos.append(currfibo)
    return fibos
