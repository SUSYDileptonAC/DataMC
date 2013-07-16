#!/usr/bin/env python

import ROOT
import numpy as np

from ConfigParser import ConfigParser
from defs import Region
from defs import Regions
from defs import Plot
#~ from defs import ThePlots
attic = []

from ROOT import TMath

	
	
def main():
	
	from sys import argv
	
	from ROOT import TCanvas, TPad, TH1F, TH1I, THStack, TLegend, TMath
	import ratios
	from defs import Backgrounds
	from defs import Backgrounds2011
	from defs import Signals
	from defs import mainConfig
	from defs import defineMyColors
	from defs import myColors
	from defs import Plot	
	from defs import getRegion
	
	from setTDRStyle import setTDRStyle
	
	from helpers import *
	from plotDataMC import plotDataMC		
	from compareTTbar import compareTTbar		
	from SFvsOF import SFvsOF		
	from compareReco2011 import compareReco2011
	from defs import Region, runRanges, thePlots		
	#~ path = "/media/data/DATA/sw532v0470/"
	path = argv[1]
	if mainConfig.useTriggerEmulation:
		path = "/media/data/DATA/TriggerTrees/"
	if mainConfig.useVectorTrees:
		path = "/media/data/DATA/VectorTrees"
	
	if mainConfig.plot2011:
		path = "/media/data/DATA/2011MC"
	print "Using Trees from path:"
	print path
	
	logScale = True
	
	if argv[3] == "AN":
		region = getRegion("Region")
		logScale = region.logY
		plots = thePlots.generalPlots	
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)			
			plot.cleanCuts()			
			#~ plotDataMC(path,plot,"SF",logScale,"Inclusive")
			#~ plotDataMC(path,plot,"OF",logScale,"Inclusive")
			#~ plotDataMC(path,plot,"EE",logScale,"Inclusive")
			#~ plotDataMC(path,plot,"MuMu",logScale,"Inclusive")
			plot.cuts = tempCutString
			plot.filename = tempFileName
		plots = thePlots.anPlotsMetStudyPlotsInclusive
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
#			plot.addRegion(region)			
#			plot.cleanCuts()				
#			plotDataMC(path,plot,"SF",logScale,"Inclusive")
#			plotDataMC(path,plot,"OF",logScale,"Inclusive")		
			plot.cuts = tempCutString	
			plot.filename = tempFileName
		region = getRegion("bTagControl")
		logScale = region.logY	
		plots = thePlots.anPlotsbTagControl	
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
#			plot.addRegion(region)			
#			plot.cleanCuts()				
#			plotDataMC(path,plot,"SF",logScale,"bTagControl")
#			plotDataMC(path,plot,"OF",logScale,"bTagControl")
			plot.cuts = tempCutString
			plot.filename = tempFileName
		region = getRegion("SignalBarrel")
		logScale = region.logY
		plots = thePlots.generalPlots	
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)			
			plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalBarrel")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalBarrel")
			#~ plotDataMC(path,plot,"EE",logScale,"SignalBarrel")
			#~ plotDataMC(path,plot,"MuMu",logScale,"SignalBarrel")
			plot.cuts = tempCutString
			plot.filename = tempFileName
		region = getRegion("SignalForward")
		logScale = region.logY
		plots = thePlots.generalPlots		
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)			
			plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalForward")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalForward")
			#~ plotDataMC(path,plot,"EE",logScale,"SignalForward")
			#~ plotDataMC(path,plot,"MuMu",logScale,"SignalForward")
			plot.cuts = tempCutString
			plot.filename = tempFileName
		region = getRegion("SignalHighMET")
		logScale = region.logY
		plots = thePlots.anPlotsMetStudyPlotsHighMET	
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)			
			plot.cleanCuts()				
			plotDataMC(path,plot,"SF",logScale,"SignalHighMET")
			plotDataMC(path,plot,"OF",logScale,"SignalHighMET")
			plot.cuts = tempCutString
			plot.filename = tempFileName
		plots = thePlots.anPlotsCompareTTbar													
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)			
			plot.cleanCuts()				
			compareTTbar(path,plot,"SF",logScale)
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString	
			plot.filename = tempFileName

		region = getRegion("ttBarDileptonSF")
		logScale = region.logY
		plots = thePlots.generalPlots
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)
			#~ plot.cleanCuts()
			#~ plotDataMC(path,plot,"SF",logScale,"ttBarDileptonSF")
			#~ plotDataMC(path,plot,"EE",logScale,"ttBarDileptonEE")
			#~ plotDataMC(path,plot,"MuMu",logScale,"ttBarDileptonMuMu")
			#~ compareTTbar(path,plot,"SF",logScale)
			#~ compareTTbar(path,plot,"OF",logScale)
			#~ plot.cuts = tempCutString		
			#~ plot.filename = tempFileName			

		region = getRegion("ttBarDileptonOF")
		logScale = region.logY
		plots = thePlots.generalPlots
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()			
			#~ plotDataMC(path,plot,"OF",logScale,"ttBarDileptonOF")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		
			
	if argv[3] == "PAS":
		#~ region = getRegion("Region")
		#~ logScale = region.logY
		#~ 
		#~ plots = thePlots.pasPlotsInclusive
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()			
			#~ plotDataMC(path,plot,"SF",logScale,"Inclusive")
			#~ plotDataMC(path,plot,"OF",logScale,"Inclusive")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		#~ region = getRegion("bTagControl")
		#~ logScale = region.logY
		#~ 
		#~ plots = thePlots.pasPlotsbTagControl
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()			
			#~ plotDataMC(path,plot,"SF",logScale,"bTagControl")
			#~ plotDataMC(path,plot,"OF",logScale,"bTagControl")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
			#~ 
		region = getRegion("ttBarDileptonSF")
		logScale = region.logY
		plots = thePlots.pasPlotsCompareTTbarHighMET
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			compareTTbar(path,plot,"SF",logScale)
			#~ compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString		
			plot.filename = tempFileName			
		#~ 
		#~ plots = thePlots.pasPlotsbTagControl
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()			
			#~ plotDataMC(path,plot,"SF",logScale,"ttBarDileptonSF")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
			#~ 
		region = getRegion("ttBarDileptonOF")
		logScale = region.logY
		#~ 
		#~ plots = thePlots.pasPlotsbTagControl
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()			
			#~ plotDataMC(path,plot,"OF",logScale,"ttBarDileptonOF")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
			
		plots = thePlots.pasPlotsCompareTTbarHighMET
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			#~ compareTTbar(path,plot,"SF",logScale,"ttBarDileptonSF")
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString		
			plot.filename = tempFileName				
			
		region = getRegion("SignalHighMET")
		logScale = region.logY
		#~ plots = thePlots.pasPlotsHighMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalHighMET")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalHighMET")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		plots = thePlots.pasPlotsCompareTTbarHighMET
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			compareTTbar(path,plot,"SF",logScale)
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString		
			plot.filename = tempFileName	
		#~ plots = thePlots.pasPlotsSFvsOFHighMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)
			#~ plot.cleanCuts()
			#~ SFvsOF(path,plot,"OF",logScale,compareSFvsOF=True)
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName	
		region = getRegion("SignalHighMETBarrel")
		logScale = region.logY
		#~ plots = thePlots.pasPlotsHighMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalHighMETBarrel")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalHighMETBarrel")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		plots = thePlots.pasPlotsCompareTTbarHighMET
		for plot in plots:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			compareTTbar(path,plot,"SF",logScale)
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString		
			plot.filename = tempFileName	
		#~ plots = thePlots.pasPlotsSFvsOFHighMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)
			#~ plot.cleanCuts()
			#~ SFvsOF(path,plot,"OF",logScale,compareSFvsOF=True)
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName						
		region = getRegion("SignalLowMET")
		logScale = region.logY
		#~ plots = thePlots.pasPlotsLowMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalLowMET")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalLowMET")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		#~ plots = plots
		for plot in thePlots.pasPlotsCompareTTbarLowMET:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			compareTTbar(path,plot,"SF",logScale)
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString	
			plot.filename = tempFileName
		#~ plots = thePlots.pasPlotsSFvsOFLowMET			
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)
			#~ plot.cleanCuts()
			#~ SFvsOF(path,plot,"OF",logScale,compareSFvsOF=True)			
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName	
		region = getRegion("SignalLowMETFullEta")
		logScale = region.logY
		#~ plots = thePlots.pasPlotsLowMET
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)			
			#~ plot.cleanCuts()				
			#~ plotDataMC(path,plot,"SF",logScale,"SignalLowMETFullEta")
			#~ plotDataMC(path,plot,"OF",logScale,"SignalLowMETFullEta")
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName
		#~ plots = plots
		for plot in thePlots.pasPlotsCompareTTbarLowMET:
			tempCutString = plot.cuts
			tempFileName = plot.filename
			plot.addRegion(region)
			plot.cleanCuts()
			compareTTbar(path,plot,"SF",logScale)
			compareTTbar(path,plot,"OF",logScale)
			plot.cuts = tempCutString	
			plot.filename = tempFileName
		#~ plots = thePlots.pasPlotsSFvsOFLowMET			
		#~ for plot in plots:
			#~ tempCutString = plot.cuts
			#~ tempFileName = plot.filename
			#~ plot.addRegion(region)
			#~ plot.cleanCuts()
			#~ SFvsOF(path,plot,"OF",logScale,compareSFvsOF=True)			
			#~ plot.cuts = tempCutString	
			#~ plot.filename = tempFileName				
		
		
	
	else:
		region = getRegion(argv[3])
			
		for plot in thePlots.plots:
				
			plot.addRegion(region)
			logScale = region.logY
			plot.cleanCuts()
			if "OF" in argv[3]:
				dileptons = ["OF"]
			elif "SF" in argv[3]:
				dileptons = ["SF","EE","MuMu"]
			else:
				#~ dileptons = ["SF","OF","EE","MuMu"]
				dileptons = ["OF"]
			for dilepton in dileptons:
				if argv[2] == "CompareTTbar":
					compareTTbar(path,plot,dilepton,logScale)
					#~ compareTTbar(path,plot,dilepton,logScale)
				elif argv[2] == "DataMC":
					plotDataMC(path,plot,dilepton,logScale,argv[3])
					#~ plotDataMC(path,plot,dilepton,logScale,argv[3])
				elif argv[2] == "DataMC2011":
					plotDataMC(path,plot,dilepton,logScale,region,Run2011=True)
					#~ plotDataMC(path,plot,dilepton,logScale,region,Run2011=True)
				elif argv[2] == "DataMC201153X":
					plotDataMC(path,plot,dilepton,logScale,region,Run201153X=True)
					#~ plotDataMC(path,plot,dilepton,logScale,region,Run201153X=True)
				elif argv[2] == "CompareReco2011":
					compareReco2011(path,plot,dilepton,logScale)
					#~ compareReco2011(path,plot,dilepton,logScale)
			if argv[2] == "CompareReco2011SFvsOF":
				compareReco2011(path,plot,"OF",logScale,doSFvsOF=True)
			elif argv[2] == "SFvsOF":
				SFvsOF(path,plot,"OF",logScale,compareSFvsOF=True)
			elif argv[2] == "SFvsOF2011":
				SFvsOF(path,plot,"OF",logScale,compare2011=True,compareSFvsOF=False)
			elif argv[2] == "SFvsOFFlavourSeperated":
				SFvsOF(path,plot,"OF",logScale,compareSFvsOFFlavourSeperated=True,compareSFvsOF=False)
		
	

	
main()
