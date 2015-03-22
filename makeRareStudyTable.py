import sys
sys.path.append('cfg/')
from frameworkStructure import pathes
sys.path.append(pathes.basePath)

import os
import pickle

from messageLogger import messageLogger as log

import math
from math import sqrt
from array import array

import argparse	


import ROOT
from ROOT import TCanvas, TEfficiency, TPad, TH1F, TH1I, THStack, TLegend, TMath, TGraphAsymmErrors, TF1, gStyle
ROOT.gROOT.SetBatch(True)

from defs import getRegion, getPlot, getRunRange, Backgrounds

from setTDRStyle import setTDRStyle
from helpers import readTrees, getDataHist, TheStack, totalNumberOfGeneratedEvents, Process

from corrections import rSFOF, rEEOF, rMMOF, rMuE, rSFOFTrig, rSFOFFact, triggerEffs
from centralConfig import regionsToUse, runRanges, backgroundLists, plotLists, systematics, mllBins
import corrections



from locations import locations


def saveTable(table, name):
	tabFile = open("tab/table_%s.tex"%name, "w")
	tabFile.write(table)
	tabFile.close()

	#~ print table


def getHistograms(path,plot,runRange,isMC,backgrounds,region=""):

	treesEE = readTrees(path,"EE")
	treesEM = readTrees(path,"EMu")
	treesMM = readTrees(path,"MuMu")
		
	
	
	if isMC:
		
		eventCounts = totalNumberOfGeneratedEvents(path)	
		processes = []
		for background in backgrounds:
			processes.append(Process(getattr(Backgrounds,background),eventCounts))
		histoEE = TheStack(processes,runRange.lumi,plot,treesEE,"None",1.0,1.0,1.0).theHistogram		
		histoMM = TheStack(processes,runRange.lumi,plot,treesMM,"None",1.0,1.0,1.0).theHistogram
		histoEM = TheStack(processes,runRange.lumi,plot,treesEM,"None",1.0,1.0,1.0).theHistogram		
		histoEE.Scale(getattr(triggerEffs,region).effEE.val)
		histoEE.Scale(getattr(triggerEffs,region).effMM.val)	
		histoEM.Scale(getattr(triggerEffs,region).effEM.val)
			
	else:
		histoEE = getDataHist(plot,treesEE)
		histoMM = getDataHist(plot,treesMM)
		histoEM = getDataHist(plot,treesEM)
	
	return histoEE , histoMM, histoEM
	
	

	






	
	
def main():
	




	backgrounds = backgroundLists.rareStudies
	selections = []
	selections.append(regionsToUse.signal.central.name)	
	selections.append(regionsToUse.signal.forward.name)	
	
			

	path = locations.dataSetPath	






	runRange = getRunRange("Full2012")
	result = {}
	for selectionName in selections:
			
		selection = getRegion(selectionName)

		plot = getPlot("mllPlot")
		plot.addRegion(selection)
		plot.cleanCuts()
		plot.cuts = plot.cuts % runRange.runCut		

		plotSignal = getPlot("mllPlot")

		label =""
		if "Forward" in selection.name:
			label = "forward"
		elif "Central" in selection.name:
			label = "central"
		else:		
			label = "inclusive"

		plotSignal.cleanCuts()
		plotSignal.cuts = plotSignal.cuts % runRange.runCut	
		result[label] = {}
		for background in backgrounds:
			histEE, histMM, histEM = getHistograms(path,plot,runRange,True,[background],label)
			histSF = histEE.Clone("histSF")
			histSF.Add(histMM.Clone())
			errIntSF = ROOT.Double()
			intSF = histSF.IntegralAndError(0,histSF.GetNbinsX()+1,errIntSF)			
			errIntOF = ROOT.Double()
			intOF = histEM.IntegralAndError(0,histEM.GetNbinsX()+1,errIntOF)			
			
			result[label][background] = {}
			result[label][background]["SF"] = {}
			result[label][background]["OF"] = {}
			result[label][background]["SF"]["val"] = float(intSF) 
			result[label][background]["SF"]["err"] = float(errIntSF) 
			result[label][background]["OF"]["val"] = float(intOF) 
			result[label][background]["OF"]["err"] = float(errIntOF)
			
			
	tableTemplate = """
\\begin{table}[hbtp]
 \\renewcommand{\\arraystretch}{1.3}
 \setlength{\\belowcaptionskip}{6pt}
 \centering
 \caption{Comparison of SF and OF yields in simulation for background processes belonging to categories which contain a mixture of flavour-symmetric and Drell--Yan processes in Table~\ref{MCClosure}. The different diboson combinations are shown separately while the category 'Other SM' is split into processes which contain the production of \Z bosons and those who don't. The OF yield is multiplied with \Rsfof and the uncertainty on the OF yields includes the systematic uncertainty on \Rsfof.}
  \label{tab:MCClosureDetails}
  \\begin{tabular}{l| ccc | ccc }
    							& \multicolumn{3}{c|}{Central} & \multicolumn{3}{c}{Forward} \\\\ \n
    \hline
								&  SF        & OF  &  SF-OF  & SF   &  OF        & SF-OF \\\\ \n
    \hline
%s

  \end{tabular}
\end{table}
"""
	lineTemplateData = r"%s & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d \\"+"\n"
	
	correction = rSFOF.central.valMC
	correctionForward = rSFOF.forward.valMC
	correctionErr = rSFOF.central.errMC
	correctionForwardErr = rSFOF.forward.errMC	
	
	table = ""
	name = "WW"
	table += lineTemplateData%(name,result["central"][name]["SF"]["val"],result["central"][name]["SF"]["err"],result["central"][name]["OF"]["val"]*correction,(result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2)**0.5 ,result["central"][name]["SF"]["val"]-result["central"][name]["OF"]["val"]*correction,((result["central"][name]["SF"]["err"])**2 + (result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2))**0.5,result["forward"][name]["SF"]["val"],result["forward"][name]["SF"]["err"],result["forward"][name]["OF"]["val"]*correctionForward,(result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2)**0.5,result["forward"][name]["SF"]["val"]-result["forward"][name]["OF"]["val"]*correctionForward,((result["forward"][name]["SF"]["err"])**2 + (result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2))**0.5)	
	name = "WZ"
	table += lineTemplateData%(name,result["central"][name]["SF"]["val"],result["central"][name]["SF"]["err"],result["central"][name]["OF"]["val"]*correction,(result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2)**0.5,result["central"][name]["SF"]["val"]-result["central"][name]["OF"]["val"]*correction,((result["central"][name]["SF"]["err"])**2 + (result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2))**0.5,result["forward"][name]["SF"]["val"],result["forward"][name]["SF"]["err"],result["forward"][name]["OF"]["val"]*correctionForward,(result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2)**0.5,result["forward"][name]["SF"]["val"]-result["forward"][name]["OF"]["val"]*correctionForward,((result["forward"][name]["SF"]["err"])**2 + (result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2))**0.5)	
	name = "ZZ"
	table += lineTemplateData%(name,result["central"][name]["SF"]["val"],result["central"][name]["SF"]["err"],result["central"][name]["OF"]["val"]*correction,(result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2)**0.5,result["central"][name]["SF"]["val"]-result["central"][name]["OF"]["val"]*correction,((result["central"][name]["SF"]["err"])**2 + (result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2))**0.5,result["forward"][name]["SF"]["val"],result["forward"][name]["SF"]["err"],result["forward"][name]["OF"]["val"]*correctionForward,(result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2)**0.5,result["forward"][name]["SF"]["val"]-result["forward"][name]["OF"]["val"]*correctionForward,((result["forward"][name]["SF"]["err"])**2 + (result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2))**0.5)	
	name = "RareNonZ"
	table += lineTemplateData%("Other SM without Z bosons",result["central"][name]["SF"]["val"],result["central"][name]["SF"]["err"],result["central"][name]["OF"]["val"]*correction,(result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2)**0.5,result["central"][name]["SF"]["val"]-result["central"][name]["OF"]["val"]*correction,((result["central"][name]["SF"]["err"])**2 + (result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2))**0.5,result["forward"][name]["SF"]["val"],result["forward"][name]["SF"]["err"],result["forward"][name]["OF"]["val"]*correctionForward,(result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2)**0.5,result["forward"][name]["SF"]["val"]-result["forward"][name]["OF"]["val"]*correctionForward,((result["forward"][name]["SF"]["err"])**2 + (result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2))**0.5)	
	name = "RareZ"
	table += lineTemplateData%("Other SM with Z bosons",result["central"][name]["SF"]["val"],result["central"][name]["SF"]["err"],result["central"][name]["OF"]["val"]*correction,(result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2)**0.5,result["central"][name]["SF"]["val"]-result["central"][name]["OF"]["val"]*correction,((result["central"][name]["SF"]["err"])**2 + (result["central"][name]["OF"]["err"]**2 + (result["central"][name]["OF"]["val"]*correctionErr)**2))**0.5,result["forward"][name]["SF"]["val"],result["forward"][name]["SF"]["err"],result["forward"][name]["OF"]["val"]*correctionForward,(result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2)**0.5,result["forward"][name]["SF"]["val"]-result["forward"][name]["OF"]["val"]*correctionForward,((result["forward"][name]["SF"]["err"])**2 + (result["forward"][name]["OF"]["err"]**2 + (result["forward"][name]["OF"]["val"]*correctionForwardErr)**2))**0.5)	


	saveTable(tableTemplate%(table), "RareStudy_SFOF_%s"%("Full2012"))		
			 
main()
