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

	parser = argparse.ArgumentParser(description='Process some integers.')
	
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False,
						  help="Verbose mode.")
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
	parser.add_argument("-b", "--backgrounds", dest="backgrounds", action="append", default=[],
						  help="backgrounds to plot.")
	parser.add_argument("-e", "--dilepton", dest="dileptons", action="append", default=[],
						  help="dilepton combinations to plot.")

	#~ p = ROOT.TProof.Open("")


	args = parser.parse_args()
	if len(args.backgrounds) == 0:
		args.backgrounds = backgroundLists.default
	if len(args.dileptons) == 0:
		args.dileptons = ["SF","OF","EE","MuMu"]

	if args.plot == "":
		args.plot = plotLists.default
		

	for plot in args.plot:
		for dilepton in args.dileptons:
			config = dataMCConfig.dataMCConfig(plot,region=args.region[0],runName=args.runRange[0],plotData=args.data,plotMC=args.mc,normalizeToData=args.norm,plotRatio=args.ratio,signals=args.signals,backgrounds=args.backgrounds)
			
			plotDataMC.plotDataMC(config,dilepton)
	
main()
