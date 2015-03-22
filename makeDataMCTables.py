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
	inclusivePkls = loadPickles("shelves/Inclusive_Mll*.pkl")
	ttBarDileptonPkls = loadPickles("shelves/ttBarDilepton*_Mll*.pkl")
	SignalHighMETPkls = loadPickles("shelves/SignalCentral_Mll*.pkl")
	SignalLowMETPkls = loadPickles("shelves/SignalForward_Mll*.pkl")
	#~ print argv[1]
	print inclusivePkls
	if argv[1] == "ttBarDilepton":
		lowMassSF = loadPickles("shelves/%sSF_Mll_edgeMass_%s_SF.pdf.pkl"%(argv[1],period))
		lowMassOF = loadPickles("shelves/%sOF_Mll_edgeMass_%s_OF.pdf.pkl"%(argv[1],period))
		highMassSF = loadPickles("shelves/%sSF_Mll_highMass_%s_SF.pdf.pkl"%(argv[1],period))
		highMassOF = loadPickles("shelves/%sOF_Mll_highMass_%s_OF.pdf.pkl"%(argv[1],period))
	elif argv[1] == "SignalCentral":
		lowMassSF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%period)
		lowMassOF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%period)
		highMassSF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%period)
		highMassOF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%period)
	elif argv[1] == "SignalForward":
		lowMassSF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%period)
		lowMassOF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%period)
		highMassSF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%period)
		highMassOF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%period)		
	else:
		lowMassSF = loadPickles("shelves/%s_Mll_edgeMass_%s_SF.pdf.pkl"%(argv[1],period))
		lowMassOF = loadPickles("shelves/%s_Mll_edgeMass_%s_OF.pdf.pkl"%(argv[1],period))
		highMassSF = loadPickles("shelves/%s_Mll_highMass_%s_SF.pdf.pkl"%(argv[1],period))
		highMassOF = loadPickles("shelves/%s_Mll_highMass_%s_OF.pdf.pkl"%(argv[1],period))
	

	tableTemplate =r"""
\begin{tabular}{l|c|c|c|c}
\hline
\hline 
& \multicolumn{2}{c|}{Same Flavor} & \multicolumn{2}{c}{Opposite Flavor}\\
& low mass & high mass & low mass & high mass \\
\hline
%s
\end{tabular}
"""
	print highMassOF


	lineTemplateData = r"%s & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d \\"+"\n"
	lineTemplate = r"%s & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d\\"+"\n"
	if argv[1] == "Inclusive":
		lineTemplateRatio = r"%s & $(%.1f\pm%.1f)%s $  & $(%.1f\pm%.1f)%s $ &$(%.1f\pm%.1f)%s $ & $(%.1f\pm%.1f)%s $ \\"+"\n"
	else:
		lineTemplateRatio = r"%s & $(%.0f\pm%.0f)%s $  & $(%.0f\pm%.0f)%s $ &$(%.0f\pm%.0f)%s $ & $(%.0f\pm%.0f)%s $ \\"+"\n"

	table =""
	
	#~ print lowMassSF["DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"]["val"]
	name = "Madgraph t#bar{t}"
	table += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	name = "Single t"
	table += lineTemplateData%("single-top",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
	name = "WW,WZ,ZZ"	
	table += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	name = "Other SM"
	table += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	table += "\\hline\n"
	name = "Total Background"
	table += lineTemplateData%("Total MC Simulation",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	table += "\\hline\n"	

	name = "Data"
	table += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	table += "\\hline\n"
	name1 = "Data" 
	name2 = "Total Background"		
	#~ table += lineTemplateData%("(Data-MC)/Data",(float(lowMassSF[name1]["val"]-lowMassSF[name2]["val"]))/lowMassSF[name1]["val"],((float(lowMassSF[name1]["err"])/lowMassSF[name1]["val"]))**2+(float(lowMassSF[name2]["err"])/lowMassSF[name2]["val"])**2)**0.5,(float(highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"],((float(highMassSF[name1]["err"])/highMassSF[name1]["val"])**2+(float(highMassSF[name2]["err"])/highMassSF[name2]["val"])**2)**0.5,(float(lowMassOF[name1]["val"]-lowMassOF[name2]["val"]))/lowMassOF[name1]["val"],((float(lowMassOF[name1]["err"])/lowMassOF[name1]["val"])**2+(float(lowMassOF[name2]["err"])/lowMassOF[name2]["val"])**2)**0.5,(float(thighMassOF[name1]["val"]-highMassOF[name2]["val"]))/highMassOF[name1]["val"],((float(highMassOF[name1]["err"])/highMassOF[name1]["val"])**2+(float(highMassOF[name2]["err"])/highMassOF[name2]["val"])**2)**0.5)
	table += lineTemplateRatio%("(Data-MC)/Data",((lowMassSF[name1]["val"]-lowMassSF[name2]["val"])/lowMassSF[name1]["val"])*100,(((lowMassSF[name1]["err"]/lowMassSF[name1]["val"])**2+(lowMassSF[name2]["err"]/lowMassSF[name2]["val"])**2)**0.5)*100,"\\%",((highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"])*100,(((highMassSF[name1]["err"]/highMassSF[name1]["val"])**2+(highMassSF[name2]["err"]/highMassSF[name2]["val"])**2)**0.5)*100,"\\%",((lowMassOF[name1]["val"]-lowMassOF[name2]["val"])/lowMassOF[name1]["val"])*100,(((lowMassOF[name1]["err"]/lowMassOF[name1]["val"])**2+(lowMassOF[name2]["err"]/lowMassOF[name2]["val"])**2)**0.5)*100,"\\%",((highMassOF[name1]["val"]-highMassOF[name2]["val"])/highMassOF[name1]["val"])*100,(((highMassOF[name1]["err"]/highMassOF[name1]["val"])**2+(highMassOF[name2]["err"]/highMassOF[name2]["val"])**2)**0.5)*100,"\\%")
	table += "\\hline\n"
	table += "\\hline\n"	
	#~ print table
	#~ print float(lowMassSF[name1]["val"]-lowMassSF[name2]["val"])/lowMassSF[name1]["val"]
	
	if argv[1] == "Signal":
		
		lowMassSF = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_SF.pdf.pkl"%period)
		lowMassOF = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_OF.pdf.pkl"%period)
		highMassSF = loadPickles("shelves/SignalForward_Mll_highMass_%s_SF.pdf.pkl"%period)
		highMassOF = loadPickles("shelves/SignalForward_Mll_highMass_%s_OF.pdf.pkl"%period)

		table2 =""
		
		#~ print lowMassSF["DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"]["val"]
		name = "Madgraph t#bar{t}"
		table2 += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
		name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
		table2 += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		name = "DY+jets (#tau#tau)"
		table2 += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		name = "Single t"
		table2 += lineTemplateData%("single-top",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
		name = "WW,WZ,ZZ"	
		table2 += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		name = "Other SM"
		table2 += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		table2 += "\\hline\n"
		name = "Total Background"
		table2 += lineTemplateData%("Total MC Simulation",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		table2 += "\\hline\n"	

		name = "Data"
		table2 += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		table2 += "\\hline\n"
		name1 = "Data" 
		name2 = "Total Background"		
		#~ table += lineTemplateData%("(Data-MC)/Data",(float(lowMassSF[name1]["val"]-lowMassSF[name2]["val"]))/lowMassSF[name1]["val"],((float(lowMassSF[name1]["err"])/lowMassSF[name1]["val"]))**2+(float(lowMassSF[name2]["err"])/lowMassSF[name2]["val"])**2)**0.5,(float(highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"],((float(highMassSF[name1]["err"])/highMassSF[name1]["val"])**2+(float(highMassSF[name2]["err"])/highMassSF[name2]["val"])**2)**0.5,(float(lowMassOF[name1]["val"]-lowMassOF[name2]["val"]))/lowMassOF[name1]["val"],((float(lowMassOF[name1]["err"])/lowMassOF[name1]["val"])**2+(float(lowMassOF[name2]["err"])/lowMassOF[name2]["val"])**2)**0.5,(float(thighMassOF[name1]["val"]-highMassOF[name2]["val"]))/highMassOF[name1]["val"],((float(highMassOF[name1]["err"])/highMassOF[name1]["val"])**2+(float(highMassOF[name2]["err"])/highMassOF[name2]["val"])**2)**0.5)
		table2 += lineTemplateRatio%("(Data-MC)/Data",((lowMassSF[name1]["val"]-lowMassSF[name2]["val"])/lowMassSF[name1]["val"])*100,(((lowMassSF[name1]["err"]/lowMassSF[name1]["val"])**2+(lowMassSF[name2]["err"]/lowMassSF[name2]["val"])**2)**0.5)*100,"\\%",((highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"])*100,(((highMassSF[name1]["err"]/highMassSF[name1]["val"])**2+(highMassSF[name2]["err"]/highMassSF[name2]["val"])**2)**0.5)*100,"\\%",((lowMassOF[name1]["val"]-lowMassOF[name2]["val"])/lowMassOF[name1]["val"])*100,(((lowMassOF[name1]["err"]/lowMassOF[name1]["val"])**2+(lowMassOF[name2]["err"]/lowMassOF[name2]["val"])**2)**0.5)*100,"\\%",((highMassOF[name1]["val"]-highMassOF[name2]["val"])/highMassOF[name1]["val"])*100,(((highMassOF[name1]["err"]/highMassOF[name1]["val"])**2+(highMassOF[name2]["err"]/highMassOF[name2]["val"])**2)**0.5)*100,"\\%")
		table2 += "\\hline\n"
		table2 += "\\hline\n"
		
		tableTemplate =r"""
\begin{tabular}{l|c|c|c|c}
\hline
\hline 
Signal Central & \multicolumn{2}{c|}{Same Flavor} & \multicolumn{2}{c}{Opposite Flavor}\\
& low mass & high mass & low mass & high mass \\
\hline
%s
\end{tabular}
"""
		tableTemplate2 = r"""
\begin{tabular}{l|c|c|c|c}
\hline
\hline 
Signal Forward & \multicolumn{2}{c|}{Same Flavor} & \multicolumn{2}{c}{Opposite Flavor}\\
& low mass & high mass & low mass & high mass \\
\hline
%s
\end{tabular}
"""	
		saveTable(tableTemplate%(table), "DataMC_StatOnly_%s_%s_Central"%(argv[1],period))
		saveTable(tableTemplate2%(table2), "DataMC_StatOnly_%s_%s_Forward"%(argv[1],period))
		lowMassSF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%period)
		lowMassOF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%period)
		highMassSF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%period)
		highMassOF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%period)			
	else:
		saveTable(tableTemplate%(table), "DataMC_StatOnly_%s"%argv[1])
	
	table =""
	otherUncertainties= 0.06726812023536856
	totalSystematics = 0 
	#~ print lowMassSF["DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"]["val"]
	name = "Madgraph t#bar{t}"
	table += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))	
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))		
	name = "Single t"
	table += lineTemplateData%("Single t",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))		
	name = "WW,WZ,ZZ"
	table += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				
	name = "Other SM"	
	table += lineTemplateData%("Other SM",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				


	table += "\\hline\n"
	name = "Total Background"
	table += lineTemplateData%("Total MC simulation",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				
	totalSystematicsLowMassSF = getSystUncert(name,lowMassSF,otherUncertainties)
	totalSystematicsHighMassSF = getSystUncert(name,highMassSF,otherUncertainties) 
	totalSystematicsLowMassOF = getSystUncert(name,lowMassOF,otherUncertainties) 
	totalSystematicsHighMassOF = getSystUncert(name,highMassOF,otherUncertainties) 
	table += "\\hline\n"	
	name = "Data"
	table += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	table += "\\hline\n"
	name1 = "Data" 
	name2 = "Total Background"
	table += lineTemplateRatio%("(Data-MC)/Data",((lowMassSF[name1]["val"]-lowMassSF[name2]["val"])/lowMassSF[name1]["val"])*100,(((lowMassSF[name1]["err"]/lowMassSF[name1]["val"])**2+(lowMassSF[name2]["err"]/lowMassSF[name2]["val"])**2+ (totalSystematicsLowMassSF/lowMassSF[name2]["val"])**2)**0.5)*100,"\\%",((highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"])*100,(((highMassSF[name1]["err"]/highMassSF[name1]["val"])**2+(highMassSF[name2]["err"]/highMassSF[name2]["val"])**2 + (totalSystematicsHighMassSF/highMassSF[name2]["val"])**2)**0.5)*100,"\\%",((lowMassOF[name1]["val"]-lowMassOF[name2]["val"])/lowMassOF[name1]["val"])*100,(((lowMassOF[name1]["err"]/lowMassOF[name1]["val"])**2+(lowMassOF[name2]["err"]/lowMassOF[name2]["val"])**2 + (totalSystematicsLowMassOF/lowMassOF[name2]["val"])**2)**0.5)*100,"\\%",((highMassOF[name1]["val"]-highMassOF[name2]["val"])/highMassOF[name1]["val"])*100,(((highMassOF[name1]["err"]/highMassOF[name1]["val"])**2+(highMassOF[name2]["err"]/highMassOF[name2]["val"])**2 + (totalSystematicsHighMassOF/highMassOF[name2]["val"])**2)**0.5)*100,"\\%")
	table += "\\hline\n"
	table += "\\hline\n"					
	#~ print table
	
	if argv[1] == "Signal":
		
		lowMassSF = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_SF.pdf.pkl"%period)
		lowMassOF = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_OF.pdf.pkl"%period)
		highMassSF = loadPickles("shelves/SignalForward_Mll_highMass_%s_SF.pdf.pkl"%period)
		highMassOF = loadPickles("shelves/SignalForward_Mll_highMass_%s_OF.pdf.pkl"%period)

		table2 =""
		otherUncertainties= 0.06726812023536856
		totalSystematics = 0 
		#~ print lowMassSF["DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"]["val"]
		name = "Madgraph t#bar{t}"
		table2 += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))	
		name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
		table2 += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))	
		name = "DY+jets (#tau#tau)"
		table2 += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))		
		name = "Single t"
		table2 += lineTemplateData%("Single t",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))		
		name = "WW,WZ,ZZ"
		table2 += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				
		name = "Other SM"	
		table2 += lineTemplateData%("Other SM",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				


		table2 += "\\hline\n"
		name = "Total Background"
		table2 += lineTemplateData%("Total MC simulation",lowMassSF[name]["val"],getSystUncert(name,lowMassSF,otherUncertainties),highMassSF[name]["val"],getSystUncert(name,highMassSF,otherUncertainties),lowMassOF[name]["val"],getSystUncert(name,lowMassOF,otherUncertainties),highMassOF[name]["val"],getSystUncert(name,highMassOF,otherUncertainties))				
		totalSystematicsLowMassSF = getSystUncert(name,lowMassSF,otherUncertainties)
		totalSystematicsHighMassSF = getSystUncert(name,highMassSF,otherUncertainties) 
		totalSystematicsLowMassOF = getSystUncert(name,lowMassOF,otherUncertainties) 
		totalSystematicsHighMassOF = getSystUncert(name,highMassOF,otherUncertainties)
		table2 += "\\hline\n"	
		name = "Data"
		table2 += lineTemplateData%(name,lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		table2 += "\\hline\n"
		name1 = "Data" 
		name2 = "Total Background"
		table2 += lineTemplateRatio%("(Data-MC)/Data",((lowMassSF[name1]["val"]-lowMassSF[name2]["val"])/lowMassSF[name1]["val"])*100,(((lowMassSF[name1]["err"]/lowMassSF[name1]["val"])**2+(lowMassSF[name2]["err"]/lowMassSF[name2]["val"])**2+ (totalSystematicsLowMassSF/lowMassSF[name2]["val"])**2)**0.5)*100,"\\%",((highMassSF[name1]["val"]-highMassSF[name2]["val"])/highMassSF[name1]["val"])*100,(((highMassSF[name1]["err"]/highMassSF[name1]["val"])**2+(highMassSF[name2]["err"]/highMassSF[name2]["val"])**2 + (totalSystematicsHighMassSF/highMassSF[name2]["val"])**2)**0.5)*100,"\\%",((lowMassOF[name1]["val"]-lowMassOF[name2]["val"])/lowMassOF[name1]["val"])*100,(((lowMassOF[name1]["err"]/lowMassOF[name1]["val"])**2+(lowMassOF[name2]["err"]/lowMassOF[name2]["val"])**2 + (totalSystematicsLowMassOF/lowMassOF[name2]["val"])**2)**0.5)*100,"\\%",((highMassOF[name1]["val"]-highMassOF[name2]["val"])/highMassOF[name1]["val"])*100,(((highMassOF[name1]["err"]/highMassOF[name1]["val"])**2+(highMassOF[name2]["err"]/highMassOF[name2]["val"])**2 + (totalSystematicsHighMassOF/highMassOF[name2]["val"])**2)**0.5)*100,"\\%")
		table2 += "\\hline\n"
		table2 += "\\hline\n"
		
		tableTemplate =r"""
\begin{tabular}{l|c|c|c|c}
\hline
\hline 
Signal Central & \multicolumn{2}{c|}{Same Flavor} & \multicolumn{2}{c}{Opposite Flavor}\\
& low mass & high mass & low mass & high mass \\
\hline
%s
\end{tabular}
"""
		tableTemplate2=r"""
\begin{tabular}{l|c|c|c|c}
\hline
\hline 
Signal Forward & \multicolumn{2}{c|}{Same Flavor} & \multicolumn{2}{c}{Opposite Flavor}\\
& low mass & high mass & low mass & high mass \\
\hline
%s
\end{tabular}
"""	
		saveTable(tableTemplate%(table), "DataMC_%s_%s_Central"%(argv[1],period))
		saveTable(tableTemplate%(table2), "DataMC_%s_%s_Forward"%(argv[1],period))
	else:
		saveTable(tableTemplate%(table), "DataMC_%s_%s"%(argv[1],period))

	tableTemplate = """
\\begin{table}[hbtp]
 \\renewcommand{\\arraystretch}{1.3}
 \setlength{\\belowcaptionskip}{6pt}
 \scriptsize
 \centering
 \caption{Comparison of the  observed event yields in the signal regions to SM simulation.
     The statistical and systematic uncertainties are added in quadrature, except for the flavor-symmetric backgrounds.
     Low-mass refers to $20 < \mll < 70$\GeV, on-\Z to  $81 < \mll < 101$\GeV and high-mass to $\mll > 120$\GeV.
     }
  \label{tab:DataMCFull}
  \\begin{tabular}{l| cc | cc | cc}
    							& \multicolumn{2}{c}{Low-mass} & \multicolumn{2}{c}{On-\Z} & \multicolumn{2}{c}{High-mass} \\\\ \n
    \hline
                                &  Central        & Forward  &  Central  & Forward   &  Central        & Forward \\\\ \n
    \hline
%s

  \end{tabular}
\end{table}


"""


	lowMassSFCentral = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%period)
	lowMassOFCentral = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%period)
	highMassSFCentral = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%period)
	highMassOFCentral = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%period)
	onZSFCentral = loadPickles("shelves/SignalCentral_Mll_zMass_%s_SF.pdf.pkl"%period)
	onZOFCentral = loadPickles("shelves/SignalCentral_Mll_zMass_%s_OF.pdf.pkl"%period)
	lowMassSFForward = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_SF.pdf.pkl"%period)
	lowMassOFForward = loadPickles("shelves/SignalForward_Mll_edgeMass_%s_OF.pdf.pkl"%period)
	highMassSFForward = loadPickles("shelves/SignalForward_Mll_highMass_%s_SF.pdf.pkl"%period)
	highMassOFForward = loadPickles("shelves/SignalForward_Mll_highMass_%s_OF.pdf.pkl"%period)
	onZSFForward = loadPickles("shelves/SignalForward_Mll_zMass_%s_SF.pdf.pkl"%period)
	onZOFForward = loadPickles("shelves/SignalForward_Mll_zMass_%s_OF.pdf.pkl"%period)

	lineTemplateData = r"%s & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d \\"+"\n"


	lineTemplateRatio = r"%s & $(%.0f\pm%.0f)%s $  & $(%.0f\pm%.0f)%s $ &$(%.0f\pm%.0f)%s $ & $(%.0f\pm%.0f)%s $ &$(%.0f\pm%.0f)%s $ & $(%.0f\pm%.0f)%s $ \\"+"\n"	
	table = ""
	name = "Madgraph t#bar{t}"
	table += lineTemplateData%("\\ttbar",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	name = "Single t"
	table += lineTemplateData%("Single t",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	name = "WW,WZ,ZZ"
	table += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	name = "Other SM"	
	table += lineTemplateData%("Other SM",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	


	table += "\\hline\n"
	name = "Total Background"
	table += lineTemplateData%("Total MC simulation",lowMassSFCentral[name]["val"],getSystUncert(name,lowMassSFCentral,otherUncertainties),lowMassSFForward[name]["val"],getSystUncert(name,lowMassSFForward,otherUncertainties),onZSFCentral[name]["val"],getSystUncert(name,onZSFCentral,otherUncertainties),onZSFForward[name]["val"],getSystUncert(name,onZSFForward,otherUncertainties),highMassSFCentral[name]["val"],getSystUncert(name,highMassSFCentral,otherUncertainties),highMassSFForward[name]["val"],getSystUncert(name,highMassSFForward,otherUncertainties))	
	totalSystematicsLowMassSFCentral = getSystUncert(name,lowMassSFCentral,otherUncertainties)
	totalSystematicsHighMassSFCentral = getSystUncert(name,highMassSFCentral,otherUncertainties) 
	totalSystematicsOnZSFCentral = getSystUncert(name,onZSFCentral,otherUncertainties) 
	totalSystematicsLowMassSFForward = getSystUncert(name,lowMassSFForward,otherUncertainties)
	totalSystematicsHighMassSFForward = getSystUncert(name,highMassSFForward,otherUncertainties) 
	totalSystematicsOnZSFForward = getSystUncert(name,onZSFForward,otherUncertainties) 

	table += "\\hline\n"	
	name = "Data"
	table += lineTemplateData%(name,lowMassSFCentral[name]["val"],lowMassSFCentral[name]["err"],lowMassSFForward[name]["val"],lowMassSFForward[name]["err"],onZSFCentral[name]["val"],onZSFCentral[name]["err"],onZSFForward[name]["val"],onZSFForward[name]["err"],highMassSFCentral[name]["val"],highMassSFCentral[name]["err"],highMassSFForward[name]["val"],highMassSFForward[name]["err"])
	table += "\\hline\n"
	name1 = "Data" 
	name2 = "Total Background"
	table += lineTemplateRatio%("(Data-MC)/Data",((lowMassSFCentral[name1]["val"]-lowMassSFCentral[name2]["val"])/lowMassSFCentral[name1]["val"])*100,(((lowMassSFCentral[name1]["err"]/lowMassSFCentral[name1]["val"])**2+(lowMassSFCentral[name2]["err"]/lowMassSFCentral[name2]["val"])**2+ (totalSystematicsLowMassSFCentral/lowMassSFCentral[name2]["val"])**2)**0.5)*100,"\\%",((lowMassSFForward[name1]["val"]-lowMassSFForward[name2]["val"])/lowMassSFForward[name1]["val"])*100,(((lowMassSFForward[name1]["err"]/lowMassSFForward[name1]["val"])**2+(lowMassSFForward[name2]["err"]/lowMassSFForward[name2]["val"])**2+ (totalSystematicsLowMassSFForward/lowMassSFForward[name2]["val"])**2)**0.5)*100,"\\%",((onZSFCentral[name1]["val"]-onZSFCentral[name2]["val"])/onZSFCentral[name1]["val"])*100,(((onZSFCentral[name1]["err"]/onZSFCentral[name1]["val"])**2+(onZSFCentral[name2]["err"]/onZSFCentral[name2]["val"])**2+ (totalSystematicsOnZSFCentral/onZSFCentral[name2]["val"])**2)**0.5)*100,"\\%",((onZSFForward[name1]["val"]-onZSFForward[name2]["val"])/onZSFForward[name1]["val"])*100,(((onZSFForward[name1]["err"]/onZSFForward[name1]["val"])**2+(onZSFForward[name2]["err"]/onZSFForward[name2]["val"])**2+ (totalSystematicsOnZSFForward/onZSFForward[name2]["val"])**2)**0.5)*100,"\\%",((highMassSFCentral[name1]["val"]-highMassSFCentral[name2]["val"])/highMassSFCentral[name1]["val"])*100,(((highMassSFCentral[name1]["err"]/highMassSFCentral[name1]["val"])**2+(highMassSFCentral[name2]["err"]/highMassSFCentral[name2]["val"])**2+ (totalSystematicsHighMassSFCentral/highMassSFCentral[name2]["val"])**2)**0.5)*100,"\\%",((highMassSFForward[name1]["val"]-highMassSFForward[name2]["val"])/highMassSFForward[name1]["val"])*100,(((highMassSFForward[name1]["err"]/highMassSFForward[name1]["val"])**2+(highMassSFForward[name2]["err"]/highMassSFForward[name2]["val"])**2+ (totalSystematicsHighMassSFForward/highMassSFForward[name2]["val"])**2)**0.5)*100,"\\%")	

	saveTable(tableTemplate%(table), "DataMC_AllSignalRegion_%s"%(period))
	
	
	
	
	
	tableTemplate = """
\\begin{table}[hbtp]
 \\renewcommand{\\arraystretch}{1.3}
 \setlength{\\belowcaptionskip}{6pt}
 \centering
 \caption{Event yields in the signal region in simulation for both SF and OF lepton pairs. The OF yield is multiplied with \Rsfof and the uncertainty on the OF yields includes the systematic uncertainty on \Rsfof.}
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
	SFCentral = loadPickles("shelves/SignalCentral_Mll_%s_SF.pdf.pkl"%period)
	OFCentral = loadPickles("shelves/SignalCentral_Mll_%s_OF.pdf.pkl"%period)
	SFForward = loadPickles("shelves/SignalForward_Mll_%s_SF.pdf.pkl"%period)
	OFForward = loadPickles("shelves/SignalForward_Mll_%s_OF.pdf.pkl"%period)
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
	correctionErr = rSFOF.central.errMC
	correctionForwardErr = rSFOF.forward.errMC
	#~ correction = 0.5*(rMuE.central.valMC + 1. / rMuE.central.valMC)*rSFOFTrig.central.val
	#~ correctionForward = 0.5*(rMuE.forward.valMC + 1. / rMuE.forward.valMC)*rSFOFTrig.forward.val
	#~ correctionErr = rSFOFFact.central.SF.err
	#~ correctionForwardErr = rSFOFFact.forward.SF.err
	#~ correction = 1.0
	#~ correctionForward = 1.0
	table = ""
	name = "Madgraph t#bar{t}"
	table += lineTemplateData%("\\ttbar",SFCentral[name]["val"],SFCentral[name]["err"],OFCentral[name]["val"]*correction,(OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2)**0.5 ,SFCentral[name]["val"]-OFCentral[name]["val"]*correction,((SFCentral[name]["err"])**2 + (OFCentral[name]["err"]**2 + (OFCentral[name]["val"]*correctionErr)**2))**0.5,SFForward[name]["val"],SFForward[name]["err"],OFForward[name]["val"]*correctionForward,(OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2)**0.5,SFForward[name]["val"]-OFForward[name]["val"]*correctionForward,((SFForward[name]["err"])**2 + (OFForward[name]["err"]**2 + (OFForward[name]["val"]*correctionForwardErr)**2))**0.5)	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
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
