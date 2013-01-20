"""Just start up the game

Copyright (C) 2004 John Bauman
License: GPL v2
"""
import riskgui
import riskengine

# riskengine.debugging = 1
riskengine.setupdebugging()
riskengine.openworldfile("world.zip")
riskengine.loadterritories()
riskgui.setupdata()
riskgui.rungame()
