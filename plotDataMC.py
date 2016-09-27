def plotDataMC(mainConfig,dilepton):
	import gc
	gc.enable()	
	
	from ROOT import TCanvas, TPad, TH1F, TH1I, THStack, TLegend, TMath, gROOT,TFile, TH2F
	import ratios
	from defs import Backgrounds
	from defs import Backgrounds2011
	from defs import Signals
	from defs import defineMyColors
	from defs import myColors	
	from defs import Region
	from defs import Regions
	from defs import Plot
	from corrections import triggerEffs, rSFOFTrig
	from setTDRStyle import setTDRStyle
	gROOT.SetBatch(True)
	from helpers import *	
	import math
	
	### file to normalize signal MC
	signalDenominatorFile = TFile("../SignalScan/T6bbllsleptonDenominatorHisto.root")
	signalDenominatorHisto = TH2F(signalDenominatorFile.Get("massScan"))
	
	if mainConfig.forPAS:
		hCanvas = TCanvas("hCanvas", "Distribution", 600,800)
	else:
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


	eventCounts = totalNumberOfGeneratedEvents(mainConfig.dataSetPath)	
	processes = []
	for background in mainConfig.backgrounds:
		processes.append(Process(getattr(Backgrounds,background),eventCounts))
		
	
	### get the signal if any is to be plotted	
	signalEventCounts = {}
	signals = []
	signalNameLabel = ""
	for signal in mainConfig.signals:
		m_b = int(signal.split("_")[2])
		m_n_2 = int(signal.split("_")[4])
		signalEventCounts[signal] = signalDenominatorHisto.GetBinContent(signalDenominatorHisto.GetXaxis().FindBin(m_b),signalDenominatorHisto.GetYaxis().FindBin(m_n_2))
		signals.append(Process(getattr(Signals,signal),signalEventCounts))
		if signalNameLabel == "":
			signalNameLabel = "Signal"
		signalNameLabel += "_m_b_%s_m_n_%s"%(signal.split("_")[2],signal.split("_")[4])
		
	legend = TLegend(0.45, 0.6, 0.925, 0.925)
	legend.SetFillStyle(0)
	legend.SetBorderSize(0)
	legend.SetTextFont(42)
	legend.SetNColumns(2)
	legendEta = TLegend(0.15, 0.75, 0.7, 0.9)
	legendEta.SetFillStyle(0)
	legendEta.SetBorderSize(0)
	legendEta.SetTextFont(42)



	latex = ROOT.TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = ROOT.TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.06)
	latexCMS.SetNDC(True)
	latexCMSExtra = ROOT.TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.045)
	latexCMSExtra.SetNDC(True)	
	legendHists = []
	

	legendHistData = ROOT.TH1F()
	if mainConfig.plotData:	
		legend.AddEntry(legendHistData,"Data","pe")	
		legendEta.AddEntry(legendHistData,"Data","pe")	

	

	### loop over the background processes, add them in iverse order to the legend
	if mainConfig.plotMC:
		for process in reversed(processes):
			temphist = ROOT.TH1F()
			temphist.SetFillColor(process.theColor)
			legendHists.append(temphist.Clone)
			legend.AddEntry(temphist,process.label,"f")
			legendEta.AddEntry(temphist,process.label,"f")
	if mainConfig.plotRatio:
		temphist = ROOT.TH1F()
		temphist.SetFillColor(myColors["MyGreen"])
		legendHists.append(temphist.Clone)	
		#~ legend.AddEntry(temphist,"Syst. uncert.","f")
		temphist2 = ROOT.TH1F()
		temphist2.SetFillColor(myColors["DarkRed"],)
		temphist2.SetFillStyle(3002)
		legendHists.append(temphist2.Clone)	


	
	if mainConfig.plotSignal:
		for Signal in signals:
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
	intlumi.SetTextSize(0.045)
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


	treeEE = readTrees(mainConfig.dataSetPath, "EE")
	treeMuMu = readTrees(mainConfig.dataSetPath, "MuMu")
	treeEMu = readTrees(mainConfig.dataSetPath, "EMu")
 


	

	
	mainConfig.plot.addDilepton(dilepton)	 
	
	plotPad.cd()
	plotPad.SetLogy(0)
	logScale = mainConfig.plot.log
	if mainConfig.plot.variable == "met" or mainConfig.plot.variable == "type1Met" or mainConfig.plot.variable == "tcMet" or mainConfig.plot.variable == "caloMet" or mainConfig.plot.variable == "mht":
		logScale = True
	
	if logScale == True:
		plotPad.SetLogy()

	scaleTree1 = 1.0
	scaleTree2 = 1.0
	if mainConfig.plot.tree1 == "EE":
		tree1 = treeEE
		scaleTree1 = getattr(triggerEffs,mainConfig.etaRegion).effEE.val
		#~ scaleTree1 = mainConfig.selection.trigEffs.effEE.val
		print "ee trigger Eff:"
		print scaleTree1
	elif mainConfig.plot.tree1 == "MuMu":
		tree1 = treeMuMu
		scaleTree1 = getattr(triggerEffs,mainConfig.etaRegion).effMM.val
		#~ scaleTree1 = mainConfig.selection.trigEffs.effMM.val
		print "mumu trigger Eff:"
		print scaleTree1
	elif mainConfig.plot.tree1 == "EMu":
		tree1 = treeEMu	
		scaleTree1 = getattr(triggerEffs,mainConfig.etaRegion).effEM.val
		#~ scaleTree1 = mainConfig.selection.trigEffs.effEM.val
		print "emu trigger Eff:"
		print scaleTree1			
	else: 
		print "Unknown Dilepton combination! %s not created!"%(mainConfig.plot.filename,)
		return
	
	if mainConfig.plot.tree2 != "None":
		if mainConfig.plot.tree2 == "EE":
				tree2 = treeEE
				scaleTree2 = mainConfig.selection.trigEffs.effEE.val
				print "ee trigger Eff:"
				print scaleTree2				
		elif mainConfig.plot.tree2 == "MuMu":
				tree2 = treeMuMu
				scaleTree2 = mainConfig.selection.trigEffs.effMM.val
				print "mumu trigger Eff:"
				print scaleTree2

		elif mainConfig.plot.tree2 == "EMu":
				tree2 = treeEMu	
				scaleTree2 = mainConfig.selection.trigEffs.effEM.val
				print "emu trigger Eff:"
				print scaleTree2				
		else:
			print "Unknown Dilepton combination! %s not created!"%(mainConfig.plot.filename,)
			return
	else:
		tree2 = "None"
		
	if mainConfig.useTriggerEmulation or mainConfig.DontScaleTrig:
		scaleTree2 = 1.0
		scaleTree1 = 1.0				
	
		
	
	if mainConfig.normalizeToData:
		pickleName=mainConfig.plot.filename%("_scaled_"+mainConfig.runRange.label+"_"+dilepton)
	elif mainConfig.useTriggerEmulation:
		pickleName=mainConfig.plot.filename%("_TriggerEmulation_"+mainConfig.runRange.label+"_"+dilepton)
	elif mainConfig.DontScaleTrig:
		pickleName=mainConfig.plot.filename%("_NoTriggerScaling_"+mainConfig.runRange.label+"_"+dilepton)
	else:
		pickleName=mainConfig.plot.filename%("_"+mainConfig.runRange.label+"_"+dilepton)		
	
	
	counts = {}
	import pickle
	print mainConfig.plot.cuts
	if mainConfig.plotData:
		datahist = getDataHist(mainConfig.plot,tree1,tree2)			
		counts["Data"] = {"val":datahist.Integral(0,datahist.GetNbinsX()+1),"err":math.sqrt(datahist.Integral(0,datahist.GetNbinsX()+1))}
		print datahist.GetEntries()
		
	if mainConfig.plotMC:
		#~ stack = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts,doTopReweighting=mainConfig.doTopReweighting,theoUncert=mainConfig.theoUncert,doPUWeights=mainConfig.doPUWeights)
		stack = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts,doTopReweighting=mainConfig.doTopReweighting,doPUWeights=mainConfig.doPUWeights)

		### get the number of MC events and the uncertainty		
		errIntMC = ROOT.Double()
		intMC = stack.theHistogram.IntegralAndError(0,stack.theHistogram.GetNbinsX()+1,errIntMC)				
			
		val = float(intMC)
		err = float(errIntMC)
			
		counts["Total Background"] = {"val":val,"err":err}
		
		### scale the stack if MC is to be normalzed to data
		if mainConfig.normalizeToData:
			scalefac = datahist.Integral(datahist.FindBin(mainConfig.plot.firstBin),datahist.FindBin(mainConfig.plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(mainConfig.plot.firstBin),stack.theHistogram.FindBin(mainConfig.plot.lastBin))			
	
			drawStack = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scalefac*scaleTree1,scalefac*scaleTree2,doPUWeights=mainConfig.doPUWeights)	
			stackJESUp = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,0.955,scalefac*scaleTree1,scalefac*scaleTree2,doPUWeights=mainConfig.doPUWeights)
			stackJESDown = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.045,scalefac*scaleTree1,scalefac*scaleTree2,doPUWeights=mainConfig.doPUWeights)							
						
		else:
			drawStack = stack
			
			if mainConfig.plotSyst:

				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("met", "metJESUp")	
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace(" ht", "htJESUp")		
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("nJets", "nShiftedJetsJESUp")
				stackJESUp = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,JESUp=True,saveIntegrals=True,counts=counts,doPUWeights=mainConfig.doPUWeights)
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("metJESUp", "metJESDown")
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("htJESUp", "htJESDown")
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")					
				stackJESDown = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,JESDown=True,saveIntegrals=True,counts=counts,doPUWeights=mainConfig.doPUWeights)	
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("metJESDown", "met")
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("htJESDown", "ht")
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("nShiftedJetsJESDown", "nJets")	
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("*(", "Up*(")	
				stackPileUpUp = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,saveIntegrals=True,PileUpUp=True,counts=counts,doPUWeights=mainConfig.doPUWeights)
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("Up*(", "Down*(")		
				stackPileUpDown = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,saveIntegrals=True,PileUpDown=True,counts=counts,doPUWeights=mainConfig.doPUWeights)	
				mainConfig.plot.cuts = mainConfig.plot.cuts.replace("Down*(", "*(")
						
		
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
				
				if mainConfig.doTopReweighting:
					stackReweightDown = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,TopWeightDown=True,saveIntegrals=True,counts=counts,doPUWeights=mainConfig.doPUWeights)	
					stackReweightUp = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,TopWeightUp=True,saveIntegrals=True,counts=counts,doPUWeights=mainConfig.doPUWeights)	
							
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
	
		xSec = abs(stack.theHistogramXsecUp.Integral(0,stack.theHistogram.GetNbinsX()+1)-counts["Total Background"]["val"])
		counts["Total Background"]["xSec"]=xSec
		#~ theoUncert = abs(stack.theHistogramTheoUp.Integral(0,stack.theHistogram.GetNbinsX()+1)-counts["Total Background"]["val"])
		#~ counts["Total Background"]["theo"]=theoUncert
		
	outFilePkl = open("shelves/%s.pkl"%(pickleName),"w")
	pickle.dump(counts, outFilePkl)
	outFilePkl.close()	
	
	if mainConfig.plotSignal:
		signalhists = []
		signalLabels = []
		ymaxSignal = 0
		for Signal in signals:
			signalhist = Signal.createCombinedHistogram(mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2)
			signalhist.SetLineWidth(2)
			if mainConfig.stackSignal:
				signalhist.Add(drawStack.theHistogram)
			signalhist.SetMinimum(0.1)
			signalhists.append(signalhist)
			signalLabels.append(Signal.label)
			tmpYmaxSignal = signalhist.GetBinContent(signalhist.GetMaximumBin())
			if tmpYmaxSignal > ymaxSignal:
				ymaxSignal = tmpYmaxSignal
							
	### set the maximum of the y-axis	
	if mainConfig.plotData:
		yMax = datahist.GetBinContent(datahist.GetMaximumBin())
	elif mainConfig.plotMC:	
		yMax = drawStack.theHistogram.GetBinContent(drawStack.theHistogram.GetMaximumBin())
	else:	
		yMax = ymaxSignal
	if mainConfig.plot.yMax == 0:
		if logScale:
			yMax = yMax*1000
		else:
			yMax = yMax*1.5
						
	else: yMax = plot.yMax
	
	#~ yMax = 650

	plotPad.DrawFrame(mainConfig.plot.firstBin,mainConfig.plot.yMin,mainConfig.plot.lastBin,yMax,"; %s ; %s" %(mainConfig.plot.xaxis,mainConfig.plot.yaxis))	


	### draw the stack
	if mainConfig.plotMC:
		drawStack.theStack.Draw("samehist")	

	### Draw signal 
	if mainConfig.plotSignal:
		for Signal in signals:
			signalhist.Draw("samehist")						

	dileptonLabel = ""
	if dilepton == "SF":
		dileptonLabel = "ee + #mu#mu"
	if dilepton == "OF":
		dileptonLabel = "e#mu"
	if dilepton == "EE":
		dileptonLabel = "ee"
	if dilepton == "MuMu":
		dileptonLabel = "#mu#mu"

	if mainConfig.plotData:
		datahist.SetMinimum(0.1)
		datahist.Draw("samep")	


	
	if mainConfig.normalizeToData:			
		scalelabel.DrawLatex(0.6,0.4,"Background scaled by %.2f"%(scalefac))
	

	if mainConfig.plot.variable == "eta1" or mainConfig.plot.variable == "eta2":
		legendEta.SetNColumns(2)
		legendEta.Draw()
		intlumi.DrawLatex(0.2,0.7,"#splitline{"+mainConfig.plot.label+" "+dileptonLabel+"}{#splitline{"+mainConfig.plot.label2+"}{"+mainConfig.plot.label3+"}}")				
	else:
		legend.Draw()
		intlumi.DrawLatex(0.45,0.55,"#splitline{%s}{%s}"%(mainConfig.plot.label2,dileptonLabel))	


	
	latex.DrawLatex(0.95, 0.96, "%s fb^{-1} (13 TeV)"%(mainConfig.runRange.printval,))
	yLabelPos = 0.85
	cmsExtra = ""
	if mainConfig.personalWork:
		cmsExtra = "Private Work"
		if not mainConfig.plotData:
			cmsExtra = "#splitline{Private Work}{Simulation}"
			yLabelPos = 0.82	
	elif not mainConfig.plotData:
		cmsExtra = "Simulation"	
	elif mainConfig.preliminary:
		cmsExtra = "Preliminary"
	elif mainConfig.forTWIKI:
		cmsExtra = "Unpublished"		
	if mainConfig.forPAS:
		latexCMS.DrawLatex(0.15,0.955,"CMS")
		latexCMSExtra.DrawLatex(0.26,0.955,"%s"%(cmsExtra))				
			
	else:
		latexCMS.DrawLatex(0.19,0.89,"CMS")
		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))
	
	if mainConfig.plotRatio:
		ratioPad.cd()
		ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=mainConfig.plot.firstBin, xMax=mainConfig.plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kBlack,adaptiveBinning=0.25)
		if mainConfig.plotSyst:
			ratioGraphs.addErrorByHistograms( "Pileup", stackPileUpUp.theHistogram, stackPileUpDown.theHistogram,color= myColors["MyGreen"])			
			ratioGraphs.addErrorByHistograms( "JES", stackJESUp.theHistogram, stackJESDown.theHistogram,color= myColors["MyGreen"])	
			if mainConfig.doTopReweighting:		
				ratioGraphs.addErrorByHistograms( "TopWeight", stackReweightUp.theHistogram, stackReweightDown.theHistogram,color= myColors["MyGreen"])			
			ratioGraphs.addErrorBySize("Effs",getattr(rSFOFTrig,mainConfig.etaRegion).err,color=myColors["MyGreen"],add=True)
			ratioGraphs.addErrorByHistograms( "Xsecs", drawStack.theHistogramXsecUp, drawStack.theHistogramXsecDown,color=myColors["MyGreen"],add=True)
			#~ ratioGraphs.addErrorByHistograms( "Theo", drawStack.theHistogramTheoUp, drawStack.theHistogramTheoDown,color=myColors["MyGreen"],add=True)
		ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
		if mainConfig.plotSignal and mainConfig.stackSignal:
			signalRatios = []
			
				
			legendRatio = TLegend(0.175, 0.725, 0.65, 0.95)
			legendRatio.SetFillStyle(0)
			legendRatio.SetBorderSize(0)
			legendRatio.SetTextFont(42)
			backgroundHist = ROOT.TH1F()
			legendRatio.AddEntry(backgroundHist,"Data / background","pe")
			temphist = ROOT.TH1F()
			temphist.SetFillColor(myColors["MyGreen"])
			if mainConfig.plotSyst:
				legendRatio.AddEntry(temphist,"Syst. uncert.","f")	
				legendRatio.SetNColumns(2)			
			for index, signalhist in enumerate(signalhists):
				signalRatios.append(ratios.RatioGraph(datahist,signalhist, xMin=mainConfig.plot.firstBin, xMax=mainConfig.plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=signalhist.GetLineColor(),adaptiveBinning=0.25))
				signalRatios[index].draw(ROOT.gPad,False,False,True,chi2Pos=0.7-index*0.1)
				signalhist.SetMarkerColor(signalhist.GetLineColor())
				legendRatio.AddEntry(signalhist,"Data / Background + Signal (%s)"%signalLabels[index],"p")			
			legendRatio.Draw("same")					

	ROOT.gPad.RedrawAxis()
	plotPad.RedrawAxis()
	if mainConfig.plotRatio:

		ratioPad.RedrawAxis()

	nameModifier = mainConfig.runRange.label+"_"+dilepton
	if mainConfig.doTopReweighting:
		nameModifier+="_TopReweighted"
	if mainConfig.plotData == False:
		nameModifier+="_MCOnly"
	if mainConfig.plotMC == False:
		nameModifier+="_NoBkgMC"
		
	if mainConfig.plotSignal:	
		nameModifier+="_"+signalNameLabel
		if mainConfig.stackSignal:
			nameModifier+="_stackedSignal"

	if mainConfig.normalizeToData:
		hCanvas.Print("fig/DataMC/"+mainConfig.plot.filename%("_scaled_"+nameModifier),)
	elif mainConfig.useTriggerEmulation:
		hCanvas.Print("fig/DataMC/"+mainConfig.plot.filename%("_TriggerEmulation_"+nameModifier),)
	elif mainConfig.DontScaleTrig:
		hCanvas.Print("fig/DataMC/"+mainConfig.plot.filename%("_NoTriggerScaling_"+nameModifier),)
	else:
		hCanvas.Print("fig/DataMC/"+mainConfig.plot.filename%("_"+nameModifier),)

					


