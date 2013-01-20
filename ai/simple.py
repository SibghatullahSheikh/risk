import riskengine
import riskgui
import random
from aihelper import *
from turbohelper import *


def Assignment(player):
    freeplaces = filter(lambda x:x.player is None, riskengine.territories.values())
    if (freeplaces):
        return freeplaces[0]
    else:
        return None


def Placement(player):
    MaxRatio = 0
    Tto = None
    for t in riskengine.territories.values():
        if TIsFront(t):
            Ratio = TPressure(t) * 1.0 / t.armies
            if Ratio > MaxRatio:
                MaxRatio = Ratio
                Tto = t
    return Tto


def Attack(player):
    if player.conqueredTerritory == 1:
        return None,None
    FromTerr = None
    ToTerr = None
    MaxRatio = 0
    for t in riskengine.territories.values():
        if TIsFront(t) and t.armies > 1:
            te = TWeakestFront(t)
            ratio = t.armies * 1.0 / te.armies
            if ratio > MaxRatio:
                MaxRatio = ratio
                FromTerr = t
                ToTerr = te
    return FromTerr, ToTerr


def Occupation(player,t1,t2):
    if TIsFront(t1) and TIsFront(t2):
        return (t1.armies - t2.armies) // 2
    if TIsFront(t1):
        return 0
    
    return t1.armies - 1


def Fortification(player):
    FromTerr = None
    ToTerr = None
    Armies = None
    
    MaxArmy = 1
    for t in riskengine.territories.values():
        if t.player == player and not TIsFront(t):
            if t.armies > MaxArmy:
                MaxArmy = t.armies
                FromTerr = t
                
    if FromTerr is None:
        return None, None, 0
        
    for t in FromTerr.neighbors:
        if TIsFront(t):
            ToTerr = t
            break
    
    if ToTerr is None:
        for t in FromTerr.neighbors:
            if t.player == player:
                ToTerr = t
                break
    
    return FromTerr, ToTerr, FromTerr.armies - 1
