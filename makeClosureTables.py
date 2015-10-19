#!/usr/bin/env python
import sys
sys.path.append('cfg/')
from frameworkStructure import pathes
sys.path.append(pathes.basePath)

from corrections import rSFOFTrig, rSFOFFact, rMuE, rSFOF

def saveTable(table, name):
	tabFile = open("tab/table_%s.tex"%name, "w")
	tabFile.write(table)
	tabFile.close()

	#~ print table
	

def getSystUncert(name,shelve,scaleErr):
	
	err = (shelve[name]["err"]**2+shelve[name]["xSec"]**2+shelve[name]["theo"]**2+max(shelve[name]["jesUp"],shelve[name]["jesDown"])**2+max(shelve[name]["pileUpUp"],shelve[name]["pileUpDown"])**2+max(shelve[name]["topWeightUp"],shelve[name]["topWeightDown"])**2+(scaleErr*shelve[name]["val"])**2)**0.5
	return err			  


def main():
	from sys import argv
	from helpers import loadPickles
	#~ allPkls = loadPickles("shelves/*.pkl")
	period = argv[2]

	
	
	
	
	tableTemplate = """
\\begin{table}[hbtp]
 \\renewcommand{\\arraystretch}{1.3}
 \setlength{\\belowcaptionskip}{6pt}
 \centering
 \caption{Event yields in the signal region in simulation for both SF and OF lepton pairs. The OF yield is multiplied with \Rsfof. The quoted uncertainties are those of the MC counts in the signal region only.}
  \label{tab:MCClosure}
  \\begin{tabular}{l| ccc | ccc }
    							& \multicolumn{3}{c|}{Central} & \multicolumn{3}{c}{Forward} \\\\ \n
    \hline
								&  SF        & OF  &  SF-OF  & SF   &  OF        & SF-OF \\\\ \n
    \hline
%s

  \end{tabular}
\end{table}


"""	

	#~ SFCentral = loadPickles("shelves/SignalCentral_Mll_NoTriggerScaling_%s_SF.pdf.pkl"%period)
	#~ OFCentral = loadPickles("shelves/SignalCentral_Mll_NoTriggerScaling_%s_OF.pdf.pkl"%period)
	#~ SFForward = loadPickles("shelves/SignalForward_Mll_NoTriggerScaling_%s_SF.pdf.pkl"%period)
	#~ OFForward = loadPickles("shelves/SignalForward_Mll_NoTriggerScaling_%s_OF.pdf.pkl"%period)
	SFCentral = loadPickles("shelves/SignalCentral_Mll_TriggerEmulation_%s_SF.pdf.pkl"%period)
	OFCentral = loadPickles("shelves/SignalCentral_Mll_TriggerEmulation_%s_OF.pdf.pkl"%period)
	SFForward = loadPickles("shelves/SignalForward_Mll_TriggerEmulation_%s_SF.pdf.pkl"%period)
	OFForward = loadPickles("shelves/SignalForward_Mll_TriggerEmulation_%s_OF.pdf.pkl"%period)
	#~ SFCentral = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%period)
	#~ OFCentral = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%period)
	#~ SFForward = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_SF.pdf.pkl"%period)
	#~ OFForward = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_OF.pdf.pkl"%period)
	#~ SFCentral = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%period)
	#~ OFCentral = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%period)
	#~ SFForward = loadPickles("shelves/SignalForward_Mll_highMass_%s_SF.pdf.pkl"%period)
	#~ OFForward = loadPickles("shelves/SignalForward_Mll_highMass_%s_OF.pdf.pkl"%period)

	lineTemplateData = r"%s & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d \\"+"\n"
	correction = rSFOF.central.valMC
	correctionForward = rSFOF.forward.valMC
	#~ correctionErr = rSFOF.central.errMC
	correctionErr = 0.
	#~ correctionForwardErr = rSFOF.forward.errMC
	correctionForwardErr = 0.
	#~ correction = 0.5*(rMuE.central.valMC + 1. / rMuE.central.valMC)*rSFOFTrig.central.val
	#~ correctionForward = 0.5*(rMuE.forward.valMC + 1. / rMuE.forward.valMC)*rSFOFTrig.forward.val
	#~ correctionErr = rSFOFFact.central.SF.err
	#~ correctionForwardErr = rSFOFFact.forward.SF.err
	#~ correction = 1.0
	#~ correctionForward = 1.0
	table = ""
	name = "Powheg t#bar{t}"
	table += lineTemplateData%("\\ttbar",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5 ,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "DY+jets"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "Single t"
	table += lineTemplateData%("Single t",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "WW,WZ,ZZ"
	table += lineTemplateData%("WW, \\Z{}\\Z, W\\Z",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "Other SM"	
	table += lineTemplateData%("Other SM",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	


	table += "\\hline\n"
	name = "Total Background"
	table += lineTemplateData%("Total MC simulation",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	

	saveTable(tableTemplate%(table), "MC_SFOF_%s"%(period))	
main()
