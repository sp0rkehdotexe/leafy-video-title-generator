#!/usr/bin/env python
# Leafy Video Title Generator
#
# Author: sp0rk 7/1/16

"""Leafy Video Title Generator creates randomized Leafy-like titles"""   

import random

def leafyVideoTitleGenerator():
    first = [
        'absolute worst',
        'angriest',
        'biggest',
        'creepiest',
        'cringiest',
        'funniest',
        'maddest',
        'most awkward',
        'most desperate',
        'most dirty',
        'most disgusting',
        'most erotic',
        'most fabulous',
        'most hardcore',
        'most insane',
        'most miserable',
        'most offensive',
        'most psychotic',
        'most racist',
        'most savage',
        'most terrifying',
        'nastiest',
        'saddest',
        'scariest',
        'sexiest',
        'unhappiest'
    ]

    middle = [
        'anime girl',
        'cyberbully',
        'dad',
        'diss track',
        'emo man',
        'enraged feminist',
        'feminist',
        'frozen animation',
        'gamer girl',
        'girl',
        'girls',
        'guy',
        'kid',
        'kkk member',
        'man',
        'manchild',
        'minecraft animation',
        'music video',
        'pedophile',
        'pimp',
        'pussy slayer',
        'rapper',
        'vegan',
        'video',
        'woman',
        'youtuber'
    ]

    last = [
        'ever',
        'ever exposes me',
        'ever to be witnessed',
        'ever to live on planet earth',
        'on all of youtube',
        'on planet earth',
        'on planet earth ever',
        'on the entire internet',
        'on the entire internet ever',
        'on the internet',
        'on the internet wants me',
        'on this entire website',
        'on youtube',
        'on youtube ever',
        'on youtube rages at me',
        'on youtube roasts me',
        'to be created on the internet',
        'to ever be created',
        'to ever live',
        'to ever live in the entire universe',
        'to ever live in this world',
        'to ever live on the entire planet earth',
        'to ever live roasts me',
        'to ever live wants to literally kill me',
        'to ever make a youtube video',
        'to ever touch the internet'
    ]

    results = "the " + first[random.randrange(0, len(first))] + " "  + middle[random.randrange(0, len(middle))] + " "  + last[random.randrange(0, len(last))]
    return str.upper(results)

def main():
    print leafyVideoTitleGenerator()
    
if __name__ == '__main__':
  main()