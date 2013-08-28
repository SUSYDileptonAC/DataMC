#!/usr/bin/env python

cutStrings = {"SignalForward":"weight*(chargeProduct < 0 && pt1 > 20 && pt2 > 20 && abs(eta1)<2.4  && abs(eta2) < 2.4 && TMath::Max(abs(eta1),abs(eta2)) > 1.4 && p4.M() > 20  && deltaR > 0.3 && ((met > 150  && nJets >=2)||( met > 100 && nJets >=3))&& runNr < 201657 && !(runNr >= 198049 && runNr <= 198522))",
				"SignalCentral":"weight*(chargeProduct < 0 && pt1 > 20 && pt2 > 20 && abs(eta1)<1.4  && abs(eta2) < 1.4 && p4.M() > 20 && deltaR > 0.3 && ((met > 150  && nJets >=2)||( met > 100 && nJets >=3))&& runNr < 201657 && !(runNr >= 198049 && runNr <= 198522))",
				"Inclusive":"weight*(chargeProduct < 0 && pt1 > 20 && pt2 > 20 && abs(eta1)<1.4  && abs(eta2) < 1.4 && !(abs(eta1) > 1.4 && abs(eta1) < 1.6) && !(abs(eta2) > 1.4 && abs(eta2) < 1.6) && p4.M() > 20 && deltaR > 0.3 && runNr < 201657 && !(runNr >= 198049 && runNr <= 198522))",
			}

yMax = {"SignalForward": 5000,
		"SignalCentral": 10000,
		"Inclusive":100000

}

label = {"SignalCentral": "Signal Region |#eta^{lep}| < 1.4",
		"SignalForward": "Signal Region one |#eta^{lep}| > 1.4",
		"Inclusive": "|#eta^{lep}| < 1.4"


}
	
def getFilePathsAndSampleNames(path,Run2011=False):
	"""
	helper function
	path: path to directory containing all sample files

	returns: dict of smaple names -> path of .root file (for all samples in path)
	"""
	result = []
	from glob import glob
	from re import match
	result = {}
	if Run2011:
		for filePath in glob("%s/sw428*.root"%path):

			
			sampleName = match(".*sw428v.*\.cutsV18SignalHighPt.*\.(.*).root", filePath).groups()[0]			
			#for the python enthusiats: yield sampleName, filePath is more efficient here :)
			result[sampleName] = filePath		
	else:
		for filePath in glob("%s/sw532*.root"%path):
			
			sampleName = match(".*sw532v.*\.processed.*\.(.*).root", filePath).groups()[0]			
			#for the python enthusiats: yield sampleName, filePath is more efficient here :)
			result[sampleName] = filePath
	return result

def totalNumberOfGeneratedEvents(path,Run2011=False):
	"""
	path: path to directory containing all sample files

	returns dict samples names -> number of simulated events in source sample
	        (note these include events without EMu EMu EMu signature, too )
	"""
	from ROOT import TFile
	result = {}
	#~ print path
	if Run2011:
			
		for sampleName, filePath in getFilePathsAndSampleNames(path,Run2011).iteritems():
			rootFile = TFile(filePath, "read")
			result[sampleName] = rootFile.FindObjectAny("analysis paths").GetBinContent(1)
	else:
		for sampleName, filePath in getFilePathsAndSampleNames(path).iteritems():
			#~ print filePath
			rootFile = TFile(filePath, "read")
			result[sampleName] = rootFile.FindObjectAny("analysis paths").GetBinContent(1)				
	return result

def main():
	from sys import argv
	from math import exp, sqrt
	import ROOT
	from ROOT import TCanvas, TGraphErrors, TPad, TChain, TH1F, TLegend	
	from setTDRStyle import setTDRStyle
	import ratios
	from helpers import *	
	import math
	if len(argv) > 1:	
		region = argv[1]
	else:
		region = "Inclusive"
	cutString = cutStrings[region]
	baseCut = "pt1 > 20 && pt2 > 20 && p4.M() > 20 && abs(eta1) < 2.4 && abs(eta2) < 2.4"
	pathRawNew = "/home/jan/Trees/sw532v0474/%s"
	pathRaw = "/home/jan/Trees/sw532v0470/%s"
	events = totalNumberOfGeneratedEvents(pathRaw%"")
	samples = {"TTJets_madgraph_Summer12":"sw532v0474.processed.TTJets_MGDecays_Trigger_madgraph_Summer12.root",
				#~ "SUSY_CMSSM_4500_188_Summer12":"sw532v0470.processed.SUSY_CMSSM_4500_188_Summer12.root",
				#~ "SUSY_CMSSM_4580_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4580_202_Summer12.root",
				#~ "SUSY_CMSSM_4610_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4610_202_Summer12.root",
				#~ "SUSY_CMSSM_4640_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4640_202_Summer12.root",
				#~ "SUSY_CMSSM_4700_216_Summer12":"sw532v0470.processed.SUSY_CMSSM_4700_216_Summer12.root",
				}


	
	hCanvas = TCanvas("hCanvas", "Distribution", 800,800)

				
	plotPad = ROOT.TPad("plotPad","plotPad",0,0.3,1,1)
	ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0.,1,0.3)
	setTDRStyle()		
	plotPad.UseCurrentStyle()
	ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	ratioPad.Draw()	
	plotPad.cd()			
	

	legend = TLegend(0.7, 0.55, 0.95, 0.95)
	legend.SetFillStyle(0)
	legend.SetBorderSize(1)

	#~ legend, legendEta = prepareLegends()

	latex = ROOT.TLatex()
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	
				
	print "Calculating Acceptance x Efficiency for %s"%region
	for index, sample in samples.iteritems():
		print "Sample: %s"%index
		print "Number of genererated events: %d"%events[index]
		if "TTJets" in index:
			path = pathRawNew%sample
		else:
			path = pathRaw%sample
		treeEMu = TChain()
		treeEMu.Add("%s/cutsV22DileptonFinalTrees/%sDileptonTree"%(path, "EMu"))
		treeMuMu = TChain()
		treeMuMu.Add("%s/cutsV22DileptonFinalTrees/%sDileptonTree"%(path, "MuMu"))
		treeEE = TChain()
		treeEE.Add("%s/cutsV22DileptonFinalTrees/%sDileptonTree"%(path, "EE"))	
		
		variable = "p4.M()"
		nBins = 28
		firstBin = 20
		lastBin = 300
		histEE = createHistoFromTree(treeEE,variable, cutStrings[region], nBins, firstBin, lastBin, nEvents = -1)
		histMuMu = createHistoFromTree(treeMuMu,variable, cutStrings[region], nBins, firstBin, lastBin, nEvents = -1)
		histEMu = createHistoFromTree(treeEMu,variable, cutStrings[region], nBins, firstBin, lastBin, nEvents = -1)
		
		histEE.Add(histMuMu)

		hCanvas.DrawFrame(firstBin,0,lastBin,yMax[region],"; m_{ll} [GeV] ; Events / 10 GeV" )		
		print histEE.GetEntries()/histEMu.GetEntries()
		histEMu.SetLineColor(ROOT.kBlack)
		histEMu.SetMarkerColor(ROOT.kBlack)
		histEMu.SetFillColor(ROOT.kBlack)
		histEMu.SetFillStyle(3003)
		histEE.SetLineColor(855)
		histEE.SetMarkerColor(855)
		histEE.SetFillColor(855)
		histEE.SetLineWidth(2)
		histEMu.SetLineWidth(2)
		#~ stackSF.theHistogram.Scale(stack.theHistogram.Integral(stack.theHistogram.FindBin(0),stack.theHistogram.FindBin(150))/stackSF.theHistogram.Integral(stackOF.theHistogram.FindBin(0),stackOF.theHistogram.FindBin(150)))
		#~ drawStack.theHistogram.Scale(1.0345147107438015)
		histEE.Draw("samehist")
		histEMu.Draw("samehist")	
		legend.Clear()
		legend.AddEntry(histEE,"t#bar{t} Same Flavour","f")
		legend.AddEntry(histEMu,"t#bar{t} Opposite Flavour","f")	
		legend.Draw("same")
		latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 8 TeV, Simulation")
		latex.DrawLatex(0.6,0.5,label[region])
		
		ratioPad.cd()
		
		ratioGraphs =  ratios.RatioGraph(histEE,histEMu, xMin=firstBin, xMax=lastBin,title="SF / OF",yMin=0.7,yMax=1.3,ndivisions=6,color=ROOT.kBlack,adaptiveBinning=0.25)

		ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
		
		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		ratioPad.RedrawAxis()
		
		hCanvas.Print("fig/Propaganda_%s_Before.pdf"%region)
		
		histEMu.Scale(1.021)
		ratioGraphs =  ratios.RatioGraph(histEE,histEMu, xMin=firstBin, xMax=lastBin,title="SF / OF",yMin=0.7,yMax=1.3,ndivisions=6,color=ROOT.kBlack,adaptiveBinning=0.25)
		ratioGraphs.addErrorBySize("Effs",0.07,color=ROOT.kBlue,add=False,fillStyle=3003)
		ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
		
		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		ratioPad.RedrawAxis()		
		hCanvas.Print("fig/Propaganda_%s_After.pdf"%region)
		
main()
