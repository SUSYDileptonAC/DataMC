#!/usr/bin/env python



def saveTable(table, name):
	tabFile = open("tab/table_%s.tex"%name, "w")
	tabFile.write(table)
	tabFile.close()

	#~ print table
	


				  


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
	elif argv[1] == "Signal":
		lowMassSF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_SF.pdf.pkl"%region)
		lowMassOF = loadPickles("shelves/SignalCentral_Mll_edgeMass_%s_OF.pdf.pkl"%region)
		highMassSF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_SF.pdf.pkl"%region)
		highMassOF = loadPickles("shelves/SignalCentral_Mll_highMass_%s_OF.pdf.pkl"%region)
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
	print lowMassSF


	lineTemplateData = r"%s & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d & %d$\pm$%d \\"+"\n"
	lineTemplate = r"%s & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d & %d$\pm$%d$\pm$%d\\"+"\n"
	if argv[1] == "Inclusive":
		lineTemplateRatio = r"%s & $(%.1f\pm%.1f)%s $  & $(%.1f\pm%.1f)%s $ &$(%.1f\pm%.1f)%s $ & $(%.1f\pm%.1f)%s $ \\"+"\n"
	else:
		lineTemplateRatio = r"%s & $(%.0f\pm%.0f)%s $  & $(%.0f\pm%.0f)%s $ &$(%.0f\pm%.0f)%s $ & $(%.0f\pm%.0f)%s $ \\"+"\n"

	table =""
	
	#~ print lowMassSF["DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"]["val"]
	name = "Madgraph t#bar{t} w/ SC"
	table += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
	name = "single-top"
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
		name = "Madgraph t#bar{t} w/ SC"
		table2 += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])	
		name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
		table2 += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		name = "DY+jets (#tau#tau)"
		table2 += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],lowMassSF[name]["err"],highMassSF[name]["val"],highMassSF[name]["err"],lowMassOF[name]["val"],lowMassOF[name]["err"],highMassOF[name]["val"],highMassOF[name]["err"])
		name = "single-top"
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
	name = "Madgraph t#bar{t} w/ SC"
	table += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
	name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
	table += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
	name = "DY+jets (#tau#tau)"
	table += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)			
	name = "single-top"
	table += lineTemplateData%("single-top",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)			
	name = "WW,WZ,ZZ"	
	table += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)			
	name = "Other SM"	
	table += lineTemplateData%(name,lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)		


	table += "\\hline\n"
	name = "Total Background"
	table += lineTemplateData%("Total MC simulation",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
	totalSystematicsLowMassSF = (lowMassSF[name]["xSec"]**2+(max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"]))**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5 
	#~ print totalSystematicsLowMassSF/lowMassSF[name]["val"]
	#~ print lowMassSF[name]["xSec"]
	#~ print  max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])
	#~ print 0.06726812023536856
	totalSystematicsHighMassSF = (highMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5 
	totalSystematicsLowMassOF = (lowMassOF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5 
	totalSystematicsHighMassOF = (highMassOF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5 
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
		name = "Madgraph t#bar{t} w/ SC"
		table2 += lineTemplateData%("\\ttbar",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
		name = "DY+jets (e^{+}e^{-},#mu^{+}#mu^{-})"
		table2 += lineTemplateData%("\\DYjets (\\EE,\\MM)",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
		name = "DY+jets (#tau#tau)"
		table2 += lineTemplateData%("\\DYjets $(\\tau \\tau)$",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
		name = "single-top"
		table2 += lineTemplateData%("single-top",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)	
		name = "WW,WZ,ZZ"	
		table2 += lineTemplateData%("\\PW\\PW, \\Z{}\\Z, \\PW\\Z",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)		
		name = "Other SM"	
		table2 += lineTemplateData%(name,lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)		


		table2 += "\\hline\n"
		name = "Total Background"
		table2 += lineTemplateData%("Total SM simulation",lowMassSF[name]["val"],(lowMassSF[name]["err"]**2+lowMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5,highMassSF[name]["val"],(highMassSF[name]["err"]**2+highMassSF[name]["xSec"]**2+max(highMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5,lowMassOF[name]["val"],(lowMassOF[name]["err"]**2+lowMassOF[name]["xSec"]**2+max(lowMassOF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5,highMassOF[name]["val"],(highMassOF[name]["err"]**2+highMassOF[name]["xSec"]**2+max(highMassOF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5)			
		totalSystematicsLowMassSF = (lowMassSF[name]["xSec"]**2+(max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"]))**2+(0.06726812023536856*lowMassSF[name]["val"])**2)**0.5 
		#~ print totalSystematicsLowMassSF/lowMassSF[name]["val"]
		#~ print lowMassSF[name]["xSec"]
		#~ print  max(lowMassSF[name]["jesUp"],lowMassSF[name]["jesDown"])
		#~ print 0.06726812023536856
		totalSystematicsHighMassSF = (highMassSF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],highMassSF[name]["jesDown"])**2+(0.06726812023536856*highMassSF[name]["val"])**2)**0.5 
		totalSystematicsLowMassOF = (lowMassOF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],lowMassOF[name]["jesDown"])**2+(0.06726812023536856*lowMassOF[name]["val"])**2)**0.5 
		totalSystematicsHighMassOF = (highMassOF[name]["xSec"]**2+max(lowMassSF[name]["jesUp"],highMassOF[name]["jesDown"])**2+(0.06726812023536856*highMassOF[name]["val"])**2)**0.5
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


main()
