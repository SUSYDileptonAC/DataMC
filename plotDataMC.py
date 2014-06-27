def plotDataMC(path,plot,dilepton,logScale,region="Inclusive",Run2011=False,Run201153X=False):
	import gc
	gc.enable()	
	
	from ROOT import TCanvas, TPad, TH1F, TH1I, THStack, TLegend, TMath
	import ratios
	from defs import Backgrounds
	from defs import Backgrounds2011
	from defs import Signals
	from defs import mainConfig
	from defs import defineMyColors
	from defs import myColors	
	from defs import Region
	from defs import Regions
	from defs import Plot
	from setTDRStyle import setTDRStyle
	
	from helpers import *	
	import math
	
	hCanvas = TCanvas("hCanvas", "Distribution", 800,800)
	
	if mainConfig.plotRatio:
		plotPad = ROOT.TPad("plotPad","plotPad",0,0.3,1,1)
		ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0.,1,0.3)
		setTDRStyle()		
		plotPad.UseCurrentStyle()
		ratioPad.UseCurrentStyle()
		plotPad.Draw()	
		ratioPad.Draw()	
		plotPad.cd()
	else:
		plotPad = ROOT.TPad("plotPad","plotPad",0,0,1,1)
		setTDRStyle()
		plotPad.UseCurrentStyle()
		plotPad.Draw()	
		plotPad.cd()	
		
	colors = createMyColors()		



	

	
	
	if Run2011 or Run201153X:
		eventCounts = totalNumberOfGeneratedEvents(path,Run2011=True)
		TTJets = Process(Backgrounds2011.TTJets.subprocesses,eventCounts,Backgrounds2011.TTJets.label,Backgrounds2011.TTJets.fillcolor,Backgrounds2011.TTJets.linecolor,Backgrounds2011.TTJets.uncertainty,1,Run2011=True)	
		Diboson = Process(Backgrounds2011.Diboson.subprocesses,eventCounts,Backgrounds2011.Diboson.label,Backgrounds2011.Diboson.fillcolor,Backgrounds2011.Diboson.linecolor,Backgrounds2011.Diboson.uncertainty,1,Run2011=True)	
		DY = Process(Backgrounds2011.DrellYan.subprocesses,eventCounts,Backgrounds2011.DrellYan.label,Backgrounds2011.DrellYan.fillcolor,Backgrounds2011.DrellYan.linecolor,Backgrounds2011.DrellYan.uncertainty,1,Run2011=True)	
		SingleTop = Process(Backgrounds2011.SingleTop.subprocesses,eventCounts,Backgrounds2011.SingleTop.label,Backgrounds2011.SingleTop.fillcolor,Backgrounds2011.SingleTop.linecolor,Backgrounds2011.SingleTop.uncertainty,1,Run2011=True)			
	else:
		eventCounts = totalNumberOfGeneratedEvents(path)	
		print eventCounts
		TTJets = Process(Backgrounds.TTJets.subprocesses,eventCounts,Backgrounds.TTJets.label,Backgrounds.TTJets.fillcolor,Backgrounds.TTJets.linecolor,Backgrounds.TTJets.uncertainty,1)	
		TT = Process(Backgrounds.TT.subprocesses,eventCounts,Backgrounds.TT.label,Backgrounds.TT.fillcolor,Backgrounds.TT.linecolor,Backgrounds.TT.uncertainty,1)	
		TTJets_SC = Process(Backgrounds.TTJets_SpinCorrelations.subprocesses,eventCounts,Backgrounds.TTJets_SpinCorrelations.label,Backgrounds.TTJets_SpinCorrelations.fillcolor,Backgrounds.TTJets_SpinCorrelations.linecolor,Backgrounds.TTJets_SpinCorrelations.uncertainty,1)	
		TT_MCatNLO = Process(Backgrounds.TT_MCatNLO.subprocesses,eventCounts,Backgrounds.TT_MCatNLO.label,Backgrounds.TT_MCatNLO.fillcolor,Backgrounds.TT_MCatNLO.linecolor,Backgrounds.TT_MCatNLO.uncertainty,1)	
		Diboson = Process(Backgrounds.Diboson.subprocesses,eventCounts,Backgrounds.Diboson.label,Backgrounds.Diboson.fillcolor,Backgrounds.Diboson.linecolor,Backgrounds.Diboson.uncertainty,1)	
		Rare = Process(Backgrounds.Rare.subprocesses,eventCounts,Backgrounds.Rare.label,Backgrounds.Rare.fillcolor,Backgrounds.Rare.linecolor,Backgrounds.Rare.uncertainty,1)	
		DY = Process(Backgrounds.DrellYan.subprocesses,eventCounts,Backgrounds.DrellYan.label,Backgrounds.DrellYan.fillcolor,Backgrounds.DrellYan.linecolor,Backgrounds.DrellYan.uncertainty,1,additionalSelection=Backgrounds.DrellYan.additionalSelection)	
		DYTauTau = Process(Backgrounds.DrellYanTauTau.subprocesses,eventCounts,Backgrounds.DrellYanTauTau.label,Backgrounds.DrellYanTauTau.fillcolor,Backgrounds.DrellYanTauTau.linecolor,Backgrounds.DrellYanTauTau.uncertainty,1,additionalSelection=Backgrounds.DrellYanTauTau.additionalSelection)	
		SingleTop = Process(Backgrounds.SingleTop.subprocesses,eventCounts,Backgrounds.SingleTop.label,Backgrounds.SingleTop.fillcolor,Backgrounds.SingleTop.linecolor,Backgrounds.SingleTop.uncertainty,1)	

	Signal1 = Process(Signals.SimplifiedModel_mB_400_mn2_400_mn1_160.subprocesses,eventCounts,Signals.SimplifiedModel_mB_400_mn2_400_mn1_160.label,Signals.SimplifiedModel_mB_400_mn2_400_mn1_160.fillcolor,Signals.SimplifiedModel_mB_400_mn2_400_mn1_160.linecolor,Signals.SimplifiedModel_mB_400_mn2_400_mn1_160.uncertainty,1)
	#~ Signal2 = Process(Signals.SUSY2.subprocesses,eventCounts,Signals.SUSY2.label,Signals.SUSY2.fillcolor,Signals.SUSY2.linecolor,Signals.SUSY2.uncertainty,1)	
	#~ Signal3 = Process(Signals.SUSY3.subprocesses,eventCounts,Signals.SUSY3.label,Signals.SUSY3.fillcolor,Signals.SUSY3.linecolor,Signals.SUSY3.uncertainty,1)	
	#~ Signal4 = Process(Signals.SUSY4.subprocesses,eventCounts,Signals.SUSY4.label,Signals.SUSY4.fillcolor,Signals.SUSY4.linecolor,Signals.SUSY4.uncertainty,1)	
	#~ Signal5 = Process(Signals.SUSY5.subprocesses,eventCounts,Signals.SUSY5.label,Signals.SUSY5.fillcolor,Signals.SUSY5.linecolor,Signals.SUSY5.uncertainty,1)	
	#~ signals = [Signal1]
	#~ signals = [Signal1,Signal2,Signal3,Signal4,Signal5]
	signals = [Signal1]

	legend = TLegend(0.7, 0.55, 0.95, 0.95)
	legend.SetFillStyle(0)
	legend.SetBorderSize(1)
	legendEta = TLegend(0.15, 0.75, 0.7, 0.95)
	legendEta.SetFillStyle(0)
	legendEta.SetBorderSize(1)

	#~ legend, legendEta = prepareLegends()

	latex = ROOT.TLatex()
	latex.SetTextSize(0.04)
	latex.SetNDC(True)

	legendHists = []
	

	legendHistData = ROOT.TH1F()
	if mainConfig.plotData:	
		legend.AddEntry(legendHistData,"Data","p")	
		legendEta.AddEntry(legendHistData,"Data","p")	

	

	
	if Run2011 or Run201153X:
		processes = [SingleTop,TTJets,Diboson,DY]
	else:
		processes = [Rare,SingleTop,TTJets_SC,Diboson,DYTauTau,DY]

	for process in reversed(processes):
		temphist = ROOT.TH1F()
		temphist.SetFillColor(process.theColor)
		legendHists.append(temphist.Clone)
		legend.AddEntry(temphist,process.label,"f")
		legendEta.AddEntry(temphist,process.label,"f")
		#~ if mainConfig.plotSignal:
			#~ processes.append(Signal)
	if mainConfig.plotRatio:
		temphist = ROOT.TH1F()
		temphist.SetFillColor(myColors["MyGreen"])
		legendHists.append(temphist.Clone)
		legend.AddEntry(temphist,"Scaling Uncert.","f")	
		temphist2 = ROOT.TH1F()
		temphist2.SetFillColor(myColors["DarkRed"],)
		temphist2.SetFillStyle(3002)
		legendHists.append(temphist2.Clone)
		legend.AddEntry(temphist2,"JEC/Pileup/Top Reweighting Uncert.","f")	


	
	if mainConfig.plotSignal:
		processesWithSignal = []
		for process in processes:
			processesWithSignal.append(process)
		for Signal in signals:
			processesWithSignal.append(Signal)
			temphist = ROOT.TH1F()
			temphist.SetFillColor(Signal.theColor)
			temphist.SetLineColor(Signal.theLineColor)
			legendHists.append(temphist.Clone)		
			legend.AddEntry(temphist,Signal.label,"l")
			legendEta.AddEntry(temphist,Signal.label,"l")
	
	


	nEvents=-1

	
	ROOT.gStyle.SetOptStat(0)
	
	intlumi = ROOT.TLatex()
	intlumi.SetTextAlign(12)
	intlumi.SetTextSize(0.03)
	intlumi.SetNDC(True)
	intlumi2 = ROOT.TLatex()
	intlumi2.SetTextAlign(12)
	intlumi2.SetTextSize(0.07)
	intlumi2.SetNDC(True)
	scalelabel = ROOT.TLatex()
	scalelabel.SetTextAlign(12)
	scalelabel.SetTextSize(0.03)
	scalelabel.SetNDC(True)
	metDiffLabel = ROOT.TLatex()
	metDiffLabel.SetTextAlign(12)
	metDiffLabel.SetTextSize(0.03)
	metDiffLabel.SetNDC(True)
	chi2Label = ROOT.TLatex()
	chi2Label.SetTextAlign(12)
	chi2Label.SetTextSize(0.03)
	chi2Label.SetNDC(True)
	hCanvas.SetLogy()
	from defs import Constants

	if mainConfig.useVectorTrees:
		treeEE = readVectorTrees(path, "EE")
		treeMuMu = readVectorTrees(path, "MuMu")
		treeEMu = readVectorTrees(path, "EMu")		


	elif Run2011 or Run201153X:
		treeEE = readTrees(path, "EE",Run2011=True)
		treeMuMu = readTrees(path, "MuMu",Run2011=True)
		treeEMu = readTrees(path, "EMu",Run2011=True)





	else:
		treeEE = readTrees(path, "EE")
		treeMuMu = readTrees(path, "MuMu")
		treeEMu = readTrees(path, "EMu")


 
	treeEEMC = treeEE
	treeMuMuMC = treeMuMu
	treeEMuMC = treeEMu

	if Run201153X:
		treeEE = readTrees(path, "EE")
		treeMuMu = readTrees(path, "MuMu")
		treeEMu = readTrees(path, "EMu")
	
	from defs import runRanges
	
	runs = runRanges.runs
	if Run2011 or Run201153X:
		runs = [runRanges.Run2011]
	
	plot.addDilepton(dilepton)	
	 

	baseCut = plot.cuts
	for run in runs:
		plot.cuts=baseCut
		plot.cuts = plot.cuts%run.runCut
		lumi = run.lumi
		printLumi = run.printval
		
		if "BlockA" in run.label:
			plot.cuts = plot.cuts.replace("weight","weightBlockA")
		elif "BlockB" in run.label:
			plot.cuts = plot.cuts.replace("weight","weightBlockB")
		
		print plot.cuts

			#~ plot.cuts = plot.cuts.replace("deltaR","1")
		
		
		plotPad.cd()
		plotPad.SetLogy(0)
		
		if plot.variable == "met" or plot.variable == "type1Met" or plot.variable == "tcMet" or plot.variable == "caloMet" or plot.variable == "mht":
			logScale = True
		
		if logScale == True:
			plotPad.SetLogy()
		
		#~ from defs import getOFScale
		#~ ofScale, ofScaleError = getOFScale()		
		scaleTree1 = 1.0
		scaleTree2 = 1.0
		if plot.tree1 == "EE":
			tree1 = treeEE
			tree1MC = treeEEMC
			scaleTree1 = Constants.Trigger.EffEE.val
		elif plot.tree1 == "MuMu":
			tree1 = treeMuMu
			tree1MC = treeMuMuMC
			scaleTree1 = Constants.Trigger.EffMuMu.val		
		elif plot.tree1 == "EMu":
			tree1 = treeEMu	
			tree1MC = treeEMuMC	
			scaleTree1 = Constants.Trigger.EffEMu.val			
		else: 
			print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
			continue
		
		if plot.tree2 != "None":
			if plot.tree2 == "EE":
					tree2 = treeEE
					tree2MC = treeEEMC
					scaleTree2 = Constants.Trigger.EffEE.val				
			elif plot.tree2 == "MuMu":
					tree2 = treeMuMu
					tree2MC = treeMuMuMC
					scaleTree2 = Constants.Trigger.EffMuMu.val

			elif plot.tree2 == "EMu":
					tree2 = treeEMu	
					tree2MC = treeEMuMC	
					scaleTree2 = Constants.Trigger.EffEMu.val					
			else:
				print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
				continue
		else:
			tree2 = "None"
			tree2MC = "None"
			
		if mainConfig.useTriggerEmulation:
			scaleTree2 = 1.0
			scaleTree1 = 1.0				
		
			
		
		if mainConfig.normalizeToData:
			pickleName=plot.filename%("_scaled_"+run.label+"_"+dilepton)
		elif mainConfig.useTriggerEmulation:
			pickleName=plot.filename%("_TriggerEmulation_"+run.label+"_"+dilepton)
		elif Run2011 or Run201153X:
			if Run201153X:
				pickleName=plot.filename%("_53X_"+run.label+"_"+dilepton)
			else:
				pickleName=plot.filename%("_42X_"+run.label+"_"+dilepton)
		else:
			pickleName=plot.filename%("_"+run.label+"_"+dilepton)		
		
		
		
		
		counts = {}
		import pickle
		#~ counts[pickleName] = {}
		
		if Run2011:

			datahist = getDataHist(plot,tree1,tree2,Run2011=True)
			
		elif Run201153X:
			datahist = getDataHist(plot,tree1,tree2,Run201153X=True)
		else:
			if "BlockA" in run.label:
				datahist = getDataHist(plot,tree1,tree2,Block="BlockA")	
			elif "BlockB" in run.label:
				datahist = getDataHist(plot,tree1,tree2,Block="BlockB")	
			else :
				datahist = getDataHist(plot,tree1,tree2)	
		datahist.GetXaxis().SetTitle(plot.xaxis) 
		datahist.GetYaxis().SetTitle(plot.yaxis)		
		
		
		print scaleTree1, scaleTree2
		stack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts)
		#if mainConfig.plotSignal:
			#signalCounts = {}
			#signalStack = TheStack(processesWithSignal,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=False,counts=signalCounts)

	
				
		errIntMC = ROOT.Double()
		intMC = stack.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
				
		val = float(intMC)
		err = float(errIntMC)
				
		counts["Total Background"] = {"val":val,"err":err}		
		counts["Data"] = {"val":datahist.Integral(0,datahist.GetNbinsX()+1),"err":math.sqrt(datahist.Integral(0,datahist.GetNbinsX()+1))}		
		if mainConfig.plotData:
			yMax = datahist.GetBinContent(datahist.GetMaximumBin())
		else:	
			yMax = stack.theHistogram.GetBinContent(datahist.GetMaximumBin())
		if plot.yMax == 0:
			if logScale:
				yMax = yMax*1000
			else:
				yMax = yMax*1.5

		else: yMax = plot.yMax
			
		#~ yMax = 200
		hCanvas.DrawFrame(plot.firstBin,plot.yMin,plot.lastBin,yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))
		

	 
		if mainConfig.normalizeToData:
			scalefac = datahist.Integral(datahist.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(plot.firstBin),stack.theHistogram.FindBin(plot.lastBin))			

			drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)	
			stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,0.955,scalefac*scaleTree1,scalefac*scaleTree2)
			stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.045,scalefac*scaleTree1,scalefac*scaleTree2)								
		
		elif mainConfig.useVectorTrees or Run2011 or Run201153X: 
			drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
			stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,0.955,scaleTree1,scaleTree2)	
			stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.045,scaleTree1,scaleTree2)				
		
		else:
			drawStack = stack
			plot.cuts = plot.cuts.replace("met", "metJESUp")	
			plot.cuts = plot.cuts.replace(" ht", "htJESUp")		
			plot.cuts = plot.cuts.replace("nJets", "nShiftedJetsJESUp")
			stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,JESUp=True,saveIntegrals=True,counts=counts)
			plot.cuts = plot.cuts.replace("metJESUp", "metJESDown")
			plot.cuts = plot.cuts.replace("htJESUp", "htJESDown")
			plot.cuts = plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")					
			stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,JESDown=True,saveIntegrals=True,counts=counts)	
			plot.cuts = plot.cuts.replace("metJESDown", "met")
			plot.cuts = plot.cuts.replace("htJESDown", "ht")
			plot.cuts = plot.cuts.replace("nShiftedJetsJESDown", "nJets")	
			plot.cuts = plot.cuts.replace("*(", "Up*(")	
			stackPileUpUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=True,PileUpUp=True,counts=counts)
			plot.cuts = plot.cuts.replace("Up*(", "Down*(")		
			stackPileUpDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=True,PileUpDown=True,counts=counts)	
			plot.cuts = plot.cuts.replace("Down*(", "*(")
			if mainConfig.doTopReweighting:
				stackReweightDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,TopWeightDown=True,saveIntegrals=True,counts=counts)	
				stackReweightUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,TopWeightUp=True,saveIntegrals=True,counts=counts)	


		
		errIntMC = ROOT.Double()
		intMCJESUp = stackJESUp.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
		errIntMC = ROOT.Double()
		intMCJESDown = stackJESDown.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
				
		valJESUp = float(intMCJESUp)
		valJESDown = float(intMCJESDown)
		jesUp = abs(counts["Total Background"]["val"]-valJESUp)
		jesDown = abs(counts["Total Background"]["val"]-valJESDown)
		counts["Total Background"]["jesDown"]=jesDown				
		counts["Total Background"]["jesUp"]=jesUp				
		
		errIntMC = ROOT.Double()
		intMCPileUpUp = stackPileUpUp.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
		errIntMC = ROOT.Double()
		intMCPileUpDown = stackPileUpDown.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
				
		valPileUpUp = float(intMCPileUpUp)
		valPileUpDown = float(intMCPileUpDown)
		pileUpUp = abs(counts["Total Background"]["val"]-valPileUpUp)
		pileUpDown = abs(counts["Total Background"]["val"]-valPileUpDown)
		counts["Total Background"]["pileUpDown"]=pileUpDown				
		counts["Total Background"]["pileUpUp"]=pileUpUp	
					
		errIntMC = ROOT.Double()
		intMCTopWeightUp = stackReweightUp.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
		errIntMC = ROOT.Double()
		intMCTopWeightDown = stackReweightDown.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
				
		valTopWeightUp = float(intMCTopWeightUp)
		valTopWeightDown = float(intMCTopWeightDown)
		topWeightUp = abs(counts["Total Background"]["val"]-valTopWeightUp)
		topWeightDown = abs(counts["Total Background"]["val"]-valTopWeightDown)
		counts["Total Background"]["topWeightDown"]=topWeightDown				
		counts["Total Background"]["topWeightUp"]=topWeightUp				
		
		xSec = abs(stack.theHistogramXsecUp.Integral(0,stack.theHistogram.GetNbinsX()+1)-counts["Total Background"]["val"])
		counts["Total Background"]["xSec"]=xSec
		outFilePkl = open("shelves/%s.pkl"%(pickleName),"w")
		pickle.dump(counts, outFilePkl)
		outFilePkl.close()	
	
		if mainConfig.plotSignal:
			signalhists = []
			for Signal in signals:
				signalhist = Signal.createCombinedHistogram(lumi,plot,tree1,tree2)
				signalhist.SetLineWidth(2)
				signalhist.Add(stack.theHistogram)
				signalhist.SetMinimum(0.1)
				signalhist.Draw("samehist")
				signalhists.append(signalhist)	
	
	
		drawStack.theStack.Draw("samehist")							
		drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
		drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)

				
		
			
		dileptonLabel = ""
		if dilepton == "SF":
			dileptonLabel = "ee+#mu#mu"
		if dilepton == "OF":
			dileptonLabel = "e#mu"
		if dilepton == "EE":
			dileptonLabel = "ee"
		if dilepton == "MuMu":
			dileptonLabel = "#mu#mu"
		if mainConfig.personalWork:
							
			intlumi2.DrawLatex(0.2,0.9,"%s"%dileptonLabel)

		datahist.SetMinimum(0.1)
		if mainConfig.plotData:
			datahist.Draw("samep")	

	
		
		if mainConfig.normalizeToData:			
			scalelabel.DrawLatex(0.6,0.4,"Background scaled by %.2f"%(scalefac))
		

		if plot.variable == "eta1" or plot.variable == "eta2":
			legendEta.SetNColumns(2)
			legendEta.Draw()
			if Run2011:
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")
				intlumi.DrawLatex(0.2,0.6,"Data and MC in 4_2_X")					
			elif Run201153X:
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")
				intlumi.DrawLatex(0.2,0.6,"Data in 5_3_X, MC in 4_2_X")
					
			else:
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")				
		else:
			legend.Draw()
			if Run2011:
				intlumi.DrawLatex(0.65,0.45,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")
				intlumi.DrawLatex(0.65,0.35,"Data and MC in 4_2_X")					
			elif Run201153X:
				intlumi.DrawLatex(0.65,0.45,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")
				intlumi.DrawLatex(0.65,0.35,"Data in 5_3_X, MC in 4_2_X")
					
			else:
				intlumi.DrawLatex(0.63,0.45,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	


		#~ if (plot.variable == "p4.Pt()" or plot.variable == "met" or plot.variable == "type1Met" or plot.variable == "tcMet" or plot.variable == "caloMet" or plot.variable == "mht"):
			#~ from math import sqrt
			#~ lowerBound = 130
			#~ if plot.variable == "p4.Pt()":
				#~ lowerBound = 0				
			#~ intData = datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(400))
			#~ errIntData = sqrt(datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(400)))
			#~ errIntMC = ROOT.Double()
			#~ intMC = drawStack.theHistogram.IntegralAndError(drawStack.theHistogram.FindBin(lowerBound),drawStack.theHistogram.FindBin(400),errIntMC)
			#~ if sqrt(errIntData**2+errIntMC**2)> 0:
				#~ sigma = (intMC-intData)/sqrt(errIntData**2+errIntMC**2)
				#~ 
			#~ else:
				 #~ sigma = 0
#~ 
			#~ bin130 = datahist.FindBin(lowerBound)
			#~ bin400 = datahist.FindBin(400)
			#~ i = bin130
			#~ chi2 = 0
			#~ while i <= bin400:
				#~ if datahist.GetBinError(i) > 0 and drawStack.theHistogram.GetBinError(i)>0:
					#~ chi2 = chi2 + (abs(datahist.GetBinContent(i)-drawStack.theHistogram.GetBinContent(i))/sqrt(datahist.GetBinError(i)**2+drawStack.theHistogram.GetBinError(i)**2))**2
				#~ i = i+1
			#~ 
#~ 
			#~ metDiffLabel.SetTextSize(0.05)
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d GeV}{#splitline{Data: %d \pm %.2f}{#splitline{MC: %.2f \pm %.2f}{Significance: %.2f #sigma_{stat}}}}"%(lowerBound,intData,errIntData,intMC,errIntMC,sigma))
			#~ chi2Label.SetTextSize(0.05)
			#~ chi2Label.DrawLatex(0.18,0.69,"Chi^{2}/N_{dof} = %.2f / %d"%(chi2,(bin400-bin130-1)))
		
		from math import sqrt
		lowerBound = 0
		upperBound = 5000
		if plot.variable == "met" and region == "bTagControl":
			lowerBound = 50				
		if plot.variable == "met" and region == "ttBarDileptonSF":
			lowerBound = 40				
		if plot.variable == "met" and region == "SignalHighMET":
			lowerBound = 150.0001				
		if plot.variable == "ht" and region == "SignalHighMET":
			lowerBound = 100				
		elif plot.variable == "met" and region == "SignalLowMET":
			lowerBound = 100				
		if plot.variable == "nJets" and region == "SignalHighMET":
			lowerBound = 2				
		if plot.variable == "nJets" and (region == "bTagControl" or region == "ttBarDileptonOF" or region == "ttBarDileptonSF"):
			lowerBound = 2				
		elif plot.variable == "nJets" and region == "SignalLowMET":
			lowerBound = 3				
		elif plot.variable == "p4.M()" and (region == "SignalLowMET" or region == "SignalHighMET"):
			lowerBound = 20.01
			upperBound = 69.99
						
		intData = datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(upperBound))
		errIntData = sqrt(datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(upperBound)))
		errIntMC = ROOT.Double()
		intMC = drawStack.theHistogram.IntegralAndError(drawStack.theHistogram.FindBin(lowerBound),drawStack.theHistogram.FindBin(upperBound),errIntMC)
		if sqrt(errIntData**2+errIntMC**2)> 0:
			sigma = (intMC-intData)/sqrt(errIntData**2+errIntMC**2)
			
		else:
			 sigma = 0

		bin130 = datahist.FindBin(lowerBound)
		bin400 = datahist.FindBin(upperBound)
		i = bin130
		chi2 = 0
		while i <= bin400:
			if datahist.GetBinError(i) > 0 and drawStack.theHistogram.GetBinError(i)>0:
				chi2 = chi2 + (abs(datahist.GetBinContent(i)-drawStack.theHistogram.GetBinContent(i))/sqrt(datahist.GetBinError(i)**2+drawStack.theHistogram.GetBinError(i)**2))**2
			i = i+1
		
		
		metDiffLabel.SetTextSize(0.05)
		#~ if (plot.variable == "met" and (region == "SignalHighMET" or region == "SignalLowMET" or region =="bTagControl")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d GeV}{#splitline{Data: %d \pm %.2f (stat.)}{MC: %.2f \pm %.2f (stat.)}}"%(lowerBound,intData,errIntData,intMC,errIntMC))
		#~ elif (plot.variable == "ht" and region == "SignalHighMET"):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d GeV}{#splitline{Data: %d \pm %.2f (stat.)}{MC: %.2f \pm %.2f (stat.)}}"%(lowerBound,intData,errIntData,intMC,errIntMC))
		#~ elif ((plot.variable == "nJets") and (region == "SignalHighMET" or region == "SignalLowMET" or region == "bTagControl")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d}{#splitline{Data: %d \pm %.2f (stat.)}{MC: %.2f \pm %.2f (stat.)}}"%(lowerBound-1,intData,errIntData,intMC,errIntMC))
		#~ elif ((plot.variable == "p4.M()") and (region == "SignalHighMET" or region == "SignalLowMET")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum between %d GeV and %d GeV}{#splitline{Data: %d \pm %.2f (stat.)}{MC: %.2f \pm %.2f (stat.)}}"%(lowerBound,upperBound,intData,errIntData,intMC,errIntMC))
		#~ else:
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Data: %d \pm %.2f (stat.)}{MC: %.2f \pm %.2f (stat.)}"%(intData,errIntData,intMC,errIntMC))
		#~ 
		#~ if (plot.variable == "met" and (region == "SignalHighMET" or region == "SignalLowMET" or region =="bTagControl" or region =="ttBarDileptonSF")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d GeV}{#splitline{Data: %d}{MC: %d}}"%(lowerBound,intData,intMC))
		#~ elif (plot.variable == "ht" and region == "SignalHighMET"):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d GeV}{#splitline{Data: %d}{MC: %d}}"%(lowerBound,intData,intMC))
		#~ elif ((plot.variable == "nJets") and (region == "SignalHighMET" or region == "SignalLowMET" or region == "bTagControl" or region =="ttBarDileptonSF" or region =="ttBarDileptonOF")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum above %d}{#splitline{Data: %d}{MC: %d}}"%(lowerBound-1,intData,intMC))
		#~ elif ((plot.variable == "p4.M()") and (region == "SignalHighMET" or region == "SignalLowMET")):
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Sum between %d GeV and %d GeV}{#splitline{Data: %d}{MC: %d}}"%(lowerBound,upperBound,intData,intMC))
		#~ else:
			#~ metDiffLabel.DrawLatex(0.18,0.82,"#splitline{Data: %d}{MC: %d}"%(intData,intMC))
		#~ chi2Label.SetTextSize(0.05)
		#~ chi2Label.DrawLatex(0.18,0.69,"Chi^{2}/N_{dof} = %.2f / %d"%(chi2,(bin400-bin130-1)))
		
		if mainConfig.personalWork:
			if Run2011 or Run201153X:	
				latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
			else: 
				latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))
		else:
			if Run2011 or Run201153X:	
				latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
			else: 
				latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))

		if mainConfig.produceReweighting:
			weights = []
			sumOfEntries = 0
			sumOfWeightedEntries = 0
			nBins =  datahist.GetNbinsX()
			y=0
			while y < nBins:
				if datahist.GetBinContent(y) !=0:
					
					weights.append(drawStack.theHistogram.GetBinContent(y)/datahist.GetBinContent(y))


				else:
					weights.append(1)	
				
				sumOfEntries = sumOfEntries+datahist.GetBinContent(y)
				sumOfWeightedEntries = sumOfWeightedEntries+datahist.GetBinContent(y)*weights[y]
				y=y+1
			#~ print weights
			#~ print sumOfEntries/sumOfWeightedEntries
		if mainConfig.plotRatio:
			try:
				ratioPad.cd()
			except AttributeError:
				print "Plot fails. Look up in errs/failedPlots.txt"
				outFile =open("errs/failedPlots.txt","a")
				outFile.write('%s\n'%plot.filename%("_"+run.label+"_"+dilepton))
				outFile.close()
				plot.cuts=baseCut
				return 1
			ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kBlack,adaptiveBinning=0.25)
			ratioGraphs.addErrorByHistograms( "Pileup", stackPileUpUp.theHistogram, stackPileUpDown.theHistogram,color= myColors["DarkRed"],fillStyle=3002)			
			ratioGraphs.addErrorByHistograms( "JES", stackJESUp.theHistogram, stackJESDown.theHistogram,color= myColors["DarkRed"],fillStyle=3002)			
			ratioGraphs.addErrorByHistograms( "TopWeight", stackReweightUp.theHistogram, stackReweightDown.theHistogram,color= myColors["DarkRed"],fillStyle=3002)			
			ratioGraphs.addErrorBySize("Effs",0.06726812023536856,color=myColors["MyGreen"],add=True)
			ratioGraphs.addErrorByHistograms( "Xsecs", drawStack.theHistogramXsecUp, drawStack.theHistogramXsecDown,color=myColors["MyGreen"],add=True)
			ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
			if mainConfig.plotSignal:
				signalRatios = []
				for index, signalhist in enumerate(signalhists):
					signalRatios.append(ratios.RatioGraph(datahist,signalhist, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=signalhist.GetLineColor(),adaptiveBinning=0.25))
					signalRatios[index].draw(ROOT.gPad,False,False,True,chi2Pos=0.7-index*0.1)				

		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		if mainConfig.plotRatio:

			ratioPad.RedrawAxis()

		nameModifier = run.label+"_"+dilepton
		if mainConfig.doTopReweighting:
			nameModifier+="_TopReweighted"
		if mainConfig.plotData == False:
			nameModifier+="_MCOnly"

		if mainConfig.normalizeToData:
			hCanvas.Print("fig/DataMC/"+plot.filename%("_scaled_"+nameModifier),)
		elif mainConfig.useTriggerEmulation:
			hCanvas.Print("fig/DataMC/"+plot.filename%("_TriggerEmulation_"+nameModifier),)
		elif Run2011 or Run201153X:
			if Run201153X:
				hCanvas.Print("fig/DataMC/"+plot.filename%("_53X_"+nameModifier),)
			else:
				hCanvas.Print("fig/DataMC/"+plot.filename%("_42X_"+nameModifier),)
		else:
			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_TopReweighted_"+run.label+"_"+dilepton),)
			hCanvas.Print("fig/DataMC/"+plot.filename%("_"+nameModifier),)
			#~ plotPad.cd()
			#~ plotPad.SetLogy(0)
			#~ hCanvas.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ plotPad.Range(plot.firstBin,0,plot.lastBin,1000)
			#~ plotPad.RedrawAxis()
			#~ datahist.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_"+run.label+"_"+dilepton+"_NoLog"),)
						
	plot.cuts=baseCut
	
