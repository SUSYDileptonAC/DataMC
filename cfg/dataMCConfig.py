import sys
from frameworkStructure import pathes
from locations import locations
from defs import getRegion, getPlot, getRunRange, Backgrounds

import ROOT
from helpers import readTrees, getDataHist, TheStack, totalNumberOfGeneratedEvents, Process
class dataMCConfig:
		
		
	plotData = True
	plotMC	= True
	plotSyst = False
	normalizeToData = False
	plotRatio = True
	plotSignal = False
	useTriggerEmulation = False 	
	DontScaleTrig = False 
	personalWork = True
	doTopReweighting = True
	preliminary = True
	forPAS = False
	forTWIKI = False
	
	plot = None
	region = None
	runRange = None
	dataSetPath = ""
	theoUncert = 0.
	backgrounds = []
		
	def __init__(self,plot,region="SignalInclusive",runName = "Full2012",plotData=True,plotMC=True,normalizeToData=False,plotRatio=True,signals=None,useTriggerEmulation=False,personalWork=False,doTopReweighting=False,preliminary=True,forPAS=False,forTWIKI=False,backgrounds = [],produceTheoUncert=False,dontScaleTrig=False,plotSyst=False):
		sys.path.append(pathes.basePath)
		
		self.dataSetPath = locations.dataSetPath
		if dontScaleTrig:
			self.dataSetPath = locations.dataSetPathTrigger
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
		if self.signals is not None:
			self.plotSignal = True
		self.backgrounds = backgrounds
		self.useTriggerEmulation = useTriggerEmulation
		self.personalWork = personalWork
		self.preliminary = preliminary
		self.doTopReweighting = doTopReweighting
		self.forPAS = forPAS
		self.forTWIKI = forTWIKI
		self.DontScaleTrig = dontScaleTrig
		
		
		from corrections import rSFOF	
		self.rSFOF = rSFOF
		
		if produceTheoUncert:
			
			sampleList = ["TTJets","TTJets_MatchingUp","TTJets_MatchingDown","TTJets_ScaleUp","TTJets_ScaleDown","TTJets_MassUp","TTJets_MassDown"]
			
			treesEE = readTrees(self.dataSetPath,"EE")
			treesEM = readTrees(self.dataSetPath,"EMu")
			treesMM = readTrees(self.dataSetPath,"MuMu")
					
			eventCounts = totalNumberOfGeneratedEvents(self.dataSetPath)	
			numbers = {}
			for sample in sampleList:
				process = Process(getattr(Backgrounds,sample),eventCounts)
			
				histoEE = TheStack([process],self.runRange.lumi,self.plot,treesEE,"None",1.0,1.0,1.0).theHistogram		
				histoMM = TheStack([process],self.runRange.lumi,self.plot,treesMM,"None",1.0,1.0,1.0).theHistogram
				histoEM = TheStack([process],self.runRange.lumi,self.plot,treesEM,"None",1.0,1.0,1.0).theHistogram	
				
				numbers[sample] = histoEE.Integral() + histoMM.Integral() + histoEM.Integral()
				
			
			scaleErr = max(abs(numbers["TTJets"]-numbers["TTJets_ScaleUp"]),abs(numbers["TTJets"]-numbers["TTJets_ScaleDown"])) / numbers["TTJets"]			
			matchingErr = max(abs(numbers["TTJets"]-numbers["TTJets_MatchingUp"]),abs(numbers["TTJets"]-numbers["TTJets_MatchingDown"])) / numbers["TTJets"]			
			massErr = max(abs(numbers["TTJets"]-numbers["TTJets_MassUp"]),abs(numbers["TTJets"]-numbers["TTJets_MassDown"])) / numbers["TTJets"]			
	
			self.theoUncert = (scaleErr**2 + matchingErr**2 + massErr**2)**0.5
