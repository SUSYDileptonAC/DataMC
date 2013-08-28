#!/usr/bin/env python

cutStrings = {"SignalForward":"weight*(chargeProduct < 0 && pt1 > 20 && pt2 > 20 && abs(eta1)<2.4  && abs(eta2) < 2.4 && TMath::Max(abs(eta1),abs(eta2)) > 1.4 && p4.M() > 20  && deltaR > 0.3 && ((met > 150  && nJets >=2)||( met > 100 && nJets >=3))&& runNr < 201657 && !(runNr >= 198049 && runNr <= 198522))",
				"SignalCentral":"weight*(chargeProduct < 0 && pt1 > 20 && pt2 > 20 && abs(eta1)<1.4  && abs(eta2) < 1.4 && p4.M() > 20 && p4.M() < 70 && deltaR > 0.3 && ((met > 150  && nJets >=2)||( met > 100 && nJets >=3))&& runNr < 201657 && !(runNr >= 198049 && runNr <= 198522))",
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
	
	region = argv[1]
	cutString = cutStrings[region]
	baseCut = "pt1 > 20 && pt2 > 20 && p4.M() > 20 && abs(eta1) < 2.4 && abs(eta2) < 2.4"
	pathRawNew = "/home/jan/Trees/sw532v0474/%s"
	pathRaw = "/home/jan/Trees/sw532v0470/%s"
	events = totalNumberOfGeneratedEvents(pathRaw%"")
	samples = {#"TTJets_madgraph_Summer12":"sw532v0474.processed.TTJets_MGDecays_madgraph_Summer12.root",
				#~ "SUSY_CMSSM_4500_188_Summer12":"sw532v0470.processed.SUSY_CMSSM_4500_188_Summer12.root",
				#~ "SUSY_CMSSM_4580_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4580_202_Summer12.root",
				#~ "SUSY_CMSSM_4610_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4610_202_Summer12.root",
				"SUSY_CMSSM_4640_202_Summer12":"sw532v0470.processed.SUSY_CMSSM_4640_202_Summer12.root",
				#~ "SUSY_CMSSM_4700_216_Summer12":"sw532v0470.processed.SUSY_CMSSM_4700_216_Summer12.root",
				}
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
		
		
		
		#~ copiedTreeEEBase = treeEE.CopyTree(baseCut)
		#~ copiedTreeMMBase = treeMuMu.CopyTree(baseCut)
		#~ numSF = copiedTreeEEBase.GetEntries() + copiedTreeMMBase.GetEntries()		
		#~ print "Acceptance x Efficiency for 2 SF leptons (pt > 20, mll > 20, eta < 2.4):"
		#~ print "%d / %d = %.4f"%(numSF,events[index],numSF/events[index])
		
		
		copiedTreeEE = treeEE.CopyTree(cutStrings[region])
		copiedTreeMM = treeMuMu.CopyTree(cutStrings[region])
		copiedTreeEM = treeEMu.CopyTree(cutStrings[region])
		
		numSFCopied = copiedTreeEE.GetEntries() + copiedTreeMM.GetEntries()
		
		print "Acceptance x Efficiency for 2 SF leptons in signal region:"
		print "%d / %d = %.4f"%(numSFCopied,events[index],numSFCopied/events[index])	
		print "OF events %d"%copiedTreeEM.GetEntries()	

	
main()
