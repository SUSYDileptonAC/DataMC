#!/usr/bin/env python

import sys
sys.path.append('cfg/')
from frameworkStructure import pathes
sys.path.append(pathes.basePath)

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(True)
import numpy as np


#~ from defs import ThePlots
attic = []

from ROOT import TMath

import argparse	
import dataMCConfig
import plotDataMC

from centralConfig import plotLists,backgroundLists
	
def main():

	parser = argparse.ArgumentParser(description='Data MC comparison tool')
	
	parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", default=False,
						  help="Switch verbose mode off. Do not show cut values and samples on the console whenever a histogram is created")
	parser.add_argument("-d", "--data", action="store_true", dest="data", default=False,
						  help="plot data points.")
	parser.add_argument("-m", "--mc", action="store_true", dest="mc", default=False,
						  help="plot mc backgrounds.")
	parser.add_argument("-s", "--selection", dest = "region" , nargs=1, default=["Inclusive"],
						  help="selection which to apply.")
	parser.add_argument("-p", "--plot", dest="plot", nargs=1, default="",
						  help="plot to plot.")
	parser.add_argument("-r", "--runRange", dest="runRange", nargs=1, default=["Run2015_25ns"],
						  help="name of run range.")
	parser.add_argument("-n", "--norm", action="store_true", dest="norm", default=False,
						  help="normalize to data.")
	parser.add_argument("-a", "--ratio", action="store_true", dest="ratio", default=False,
						  help="plot ratio plot")
	parser.add_argument("-S", "--signal", dest="signals", action="append", default=[],
						  help="signals to plot.")
	parser.add_argument("-t", "--stackSignal", dest="stackSignal", action="store_true", default=False,
						  help="stack the signal to the background if signal is plotted.")
	parser.add_argument("-b", "--backgrounds", dest="backgrounds", action="append", default=[],
						  help="backgrounds to plot.")
	parser.add_argument("-e", "--dilepton", dest="dileptons", action="append", default=[],
						  help="dilepton combinations to plot.")

	#~ p = ROOT.TProof.Open("")


	args = parser.parse_args()
	if len(args.backgrounds) == 0:
		args.backgrounds = backgroundLists.default
	if len(args.dileptons) == 0:
		args.dileptons = ["SF","OF"]

	if args.plot == "":
		args.plot = plotLists.default
		
	if args.quiet:
		verbose = False
	else:
		verbose = True
	
	if not args.mc and not args.data and args.signals == []:
		print "Nothing to be done since neither MC nor data is to be plotted"
		print "Run with -d for data and -m for MC bkg or add a signal sample with -S"
		sys.exit()
			
	if args.ratio and (not args.mc or not args.data):
		print "Can only plot a ratio if both data (-d) and MC (-m) are used"
		sys.exit()
		
	if args.norm and not args.mc:
		print "MC needs to be in the plot to be normalized to data"
		sys.exit()	
		
	if args.stackSignal and not args.mc:
		print "Can not stack signal on background MC if MC is not plotted"
		sys.exit()	
		
	if args.stackSignal and args.signals == []:
		print "Need a signal to stack"
		sys.exit()	

	for plot in args.plot:
		for dilepton in args.dileptons:
			config = dataMCConfig.dataMCConfig(plot,verbose=verbose,region=args.region[0],runName=args.runRange[0],plotData=args.data,plotMC=args.mc,normalizeToData=args.norm,plotRatio=args.ratio,signals=args.signals,stackSignal=args.stackSignal,backgrounds=args.backgrounds)
			
			plotDataMC.plotDataMC(config,dilepton)
	
main()
