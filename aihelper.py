"""This is a risk game, playable over the internet.

Copyright (C) 2004 John Bauman
License: GPL v2
"""
import riskengine


def TIsFront(t, pl=None):
    if pl is None: pl = riskengine.currentplayer
    if t.player != pl:
        return 0
    if not [x for x in t.neighbors if x.player != pl]:
        return 0
    return 1


def TPressure(t, pl=None):
    if pl is None: pl = riskengine.currentplayer
    return sum([i.armies for i in t.neighbors if i.player != pl])


def TWeakestFront(t, pl=None):
    if pl is None: pl = riskengine.currentplayer
    if t is None: return None
    arms = 1000
    terr = None
    for i in t.neighbors:
        if i.player != pl:
            if i.armies < arms:
                arms = i.armies
                terr = i
    return terr


def TStrongestFront(terr, player=None):
    if player is None: player = riskengine.currentplayer
    arms = -1
    terrout = None
    for i in terr.neighbors:
        if i.player != player:
            if i.armies > arms:
                arms = i.armies
                terrout = i
    return terrout


def TFrontsCount(terr, player=None):
    if player is None: player = riskengine.currentplayer
    return len([x for x in riskengine.territories.values() if x.player != player])


def TIsMine(terr):
    return terr.player == riskengine.currentplayer


def TOwner(terr):
    return terr.player


def TArmies(terr):
    if terr:
        return terr.armies
    else: 
        return 0


def TIsBordering(terr, terr2):
    return terr.neighboring(terr2)


def toplayer(player):
    if isinstance(player, riskengine.Territory):
        return player.player
    else:
        return player


def PHuman(player):
    player = toplayer(player)
    return not player.ai


def PArmiesCount(player):
    player = toplayer(player)
    return sum([t.armies for t in riskengine.territories.values() if t.player == player])


def PNewArmies(player):
    player = toplayer(player)
    return player.freeArmies


def CAnalysis(con, pl=None):
    if pl is None:
        pl = riskengine.currentplayer
    
    myterrs = [t for t in con.territories if t.player == pl]
    enemyterrs = [t for t in con.territories if t.player != pl and t.player is not None]
    myarmy = sum([t.armies for t in myterrs])
    theirarmy = sum([t.armies for t in enemyterrs])
    return len(myterrs), myarmy, len(enemyterrs), theirarmy


def UMessage(*args):
    riskengine.logai("".join([str(arg) for arg in args]))
