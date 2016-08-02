#!/usr/bin/env python

import sys
sys.path.append('cfg/')
from frameworkStructure import pathes
sys.path.append(pathes.basePath)

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import numpy as np


#~ from defs import ThePlots
attic = []

from ROOT import TMath

import argparse	
import dataMCConfig
import plotDataMC

from centralConfig import plotLists
	
def main():

	parser = argparse.ArgumentParser(description='Process some integers.')
	
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False,
						  help="Verbose mode.")
	parser.add_argument("-d", "--data", action="store_true", dest="data", default=False,
						  help="plot data points.")
	parser.add_argument("-m", "--mc", action="store_true", dest="mc", default=False,
						  help="plot mc backgrounds.")
	parser.add_argument("-s", "--selection", dest = "region" , nargs=1, default='Region',
						  help="selection which to apply.")
	parser.add_argument("-S", "--plotSyst", action="store_true" , dest="plotSyst", default=False,
						  help="selection which to apply.")
	parser.add_argument("-p", "--plot", dest="plot", nargs=1, default="",
						  help="plot to plot.")
	parser.add_argument("-r", "--runRange", dest="runRange", nargs=1, default="",
						  help="name of run range.")
	parser.add_argument("-n", "--norm", action="store_true", dest="norm", default=False,
						  help="normalize to data.")
	parser.add_argument("-a", "--ratio", action="store_true", dest="ratio", default=False,
						  help="plot ratio plot")
	parser.add_argument("-c", "--signal", dest="signals", action="append", default=[],
						  help="signals to plot.")
	parser.add_argument("-b", "--backgrounds", dest="backgrounds", action="append", default=[],
						  help="backgrounds to plot.")
	parser.add_argument("-e", "--dilepton", dest="dileptons", action="append", default=[],
						  help="dilepton combinations to plot.")
	parser.add_argument("-u", "--usetrigger", action="store_true", dest="trigger", default=False,
						  help="use trigger emulation.")	
	parser.add_argument("-l", "--dontscaletrig", action="store_true", dest="dontscaletrig", default=False,
						  help="don't scale to trigger efficiency'")	
	parser.add_argument("-t", "--topreweighting", action="store_true", dest="top", default=False,
						  help="use top reweighting.")	
	parser.add_argument("-w", "--preliminary", action="store_true", dest="preliminary", default=False,
						  help="plot is preliminary.")	
	parser.add_argument("-x", "--private", action="store_true", dest="private", default=False,
						  help="plot is private work.")	
	parser.add_argument("-f", "--forPAS", action="store_true", dest="forPAS", default=False,
						  help="plot is for PAS.")	
	parser.add_argument("-z", "--forTWIKI", action="store_true", dest="forTWIKI", default=False,
						  help="plot is for TWIKI.")	
	parser.add_argument("-P", "--puWeights", action="store_true", dest="puWeights", default=False,
						  help="do offline PU reweighting.")	

	#~ p = ROOT.TProof.Open("")


	args = parser.parse_args()
	if len(args.backgrounds) == 0:
		#~ args.backgrounds = ["Rare","SingleTop","TTJets","Diboson","DrellYanTauTau","DrellYan"]
		args.backgrounds = ["Rare","SingleTop","TT_Powheg","Diboson","DrellYanTauTau","DrellYan"]
		#~ args.backgrounds = ["TT_Powheg","DrellYanTauTau","DrellYan"]
		#~ args.backgrounds = ["T6bbllslepton"]
	if len(args.dileptons) == 0:
		args.dileptons = ["SF","OF","EE","MuMu"]

	if args.plot == "":
		args.plot = plotLists.default
		

	for plot in args.plot:
		for dilepton in args.dileptons:
			config = dataMCConfig.dataMCConfig(plot,region=args.region[0],runName=args.runRange[0],plotData=args.data,plotMC=args.mc,normalizeToData=args.norm,plotRatio=args.ratio,signals=args.signals,useTriggerEmulation=args.trigger,personalWork=args.private,preliminary=args.preliminary,forPAS=args.forPAS,forTWIKI=args.forTWIKI,backgrounds=args.backgrounds,dontScaleTrig=args.dontscaletrig,plotSyst=args.plotSyst,doPUWeights=args.puWeights,doTopReweighting=args.top)
			
			plotDataMC.plotDataMC(config,dilepton)
	
main()
