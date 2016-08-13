import sys
from frameworkStructure import pathes
from locations import locations
from defs import getRegion, getPlot, getRunRange, Backgrounds

import ROOT
from helpers import readTrees, getDataHist, TheStack, totalNumberOfGeneratedEvents, Process
class dataMCConfig:
		
		
	plotData = True
	plotMC	= True
	normalizeToData = False
	plotRatio = True
	plotSignal = False
	
	plot = None
	region = None
	runRange = None
	dataSetPath = ""
	backgrounds = []
		
	def __init__(self,plot,region="SignalInclusive",runName = "Run2015_25ns",plotData=True,plotMC=True,normalizeToData=False,plotRatio=True,signals=None,backgrounds = []):
		sys.path.append(pathes.basePath)
		
		self.dataSetPath = locations.dataSetPath
		self.runRange = getRunRange(runName)
		
		self.selection = getRegion(region)
		
		self.plot = getPlot(plot)
		self.plot.addRegion(self.selection)
		self.plot.cleanCuts()
		self.plot.cuts = self.plot.cuts % self.runRange.runCut
		
		self.plotData = plotData
		self.plotMC = plotMC
		self.normalizeToData = normalizeToData
		self.plotRatio = plotRatio
		self.signals = signals
		if len(self.signals) > 0:
			self.plotSignal = True
		self.backgrounds = backgrounds
		
		from corrections import rSFOF	
		self.rSFOF = rSFOF
		
