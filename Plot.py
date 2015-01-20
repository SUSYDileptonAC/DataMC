#!/usr/bin/env python

import sys
sys.path.append('cfg/')
from frameworkStructure import pathes
sys.path.append(pathes.basePath)

import ROOT
import numpy as np


#~ from defs import ThePlots
attic = []

from ROOT import TMath

import argparse	
import dataMCConfig
import plotDataMC
	
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
	parser.add_argument("-p", "--plot", dest="plot", nargs=1, default="",
						  help="plot to plot.")
	parser.add_argument("-r", "--runRange", dest="runRange", nargs=1, default="",
						  help="name of run range.")
	parser.add_argument("-n", "--norm", action="store_true", dest="norm", default=False,
						  help="normalize to data.")
	parser.add_argument("-a", "--ratio", dest="ratio", default=False,
						  help="plot ratio plot")
	parser.add_argument("-c", "--signal", dest="signals", action="append", default=[],
						  help="signals to plot.")
	parser.add_argument("-b", "--backgrounds", dest="backgrounds", action="append", default=[],
						  help="backgrounds to plot.")
	parser.add_argument("-e", "--dilepton", dest="dileptons", action="append", default=[],
						  help="dilepton combinations to plot.")
	parser.add_argument("-u", "--usetrigger", dest="trigger", default=False,
						  help="use trigger emulation.")	
	parser.add_argument("-t", "--topreweighting", dest="top", default=False,
						  help="use top reweighting.")	
	parser.add_argument("-w", "--preliminary", dest="preliminary", default=False,
						  help="plot is preliminary.")	
	parser.add_argument("-x", "--private", dest="private", default=False,
						  help="plot is private work.")	
	parser.add_argument("-f", "--forPAS", dest="forPAS", default=False,
						  help="plot is for PAS.")	
	parser.add_argument("-z", "--forTWIKI", dest="forTWIKI", default=False,
						  help="plot is for TWIKI.")	

	args = parser.parse_args()
	if len(args.backgrounds) == 0:
		args.backgrounds = ["Rare","SingleTop","TTJets_SpinCorrelations","Diboson","DrellYanTauTau","DrellYan"]
	if len(args.dileptons) == 0:
		args.dileptons = ["SF","OF","EE","MuMu"]
	print args.backgrounds	
	for dilepton in args.dileptons:
		config = dataMCConfig.dataMCConfig(args.plot[0],region=args.region[0],runName=args.runRange[0],plotData=args.data,plotMC=args.mc,normalizeToData=args.norm,plotRatio=args.ratio,signals=args.signals,useTriggerEmulation=args.trigger,personalWork=args.private,preliminary=args.preliminary,forPAS=args.forPAS,forTWIKI=args.forTWIKI,backgrounds=args.backgrounds)
		
		plotDataMC.plotDataMC(config,dilepton)
	
main()
