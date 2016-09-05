def plotDataMC(mainConfig,dilepton):
	import gc
	gc.enable()	
	
	from ROOT import TCanvas, TPad, TH1F, TH1I, THStack, TLegend, TMath, gROOT,TFile, TH2F
	import ratios
	from defs import Backgrounds
	from defs import Signals
	from defs import defineMyColors
	from defs import myColors	
	from defs import Region
	from defs import Regions
	from defs import Plot
	from setTDRStyle import setTDRStyle
	gROOT.SetBatch(True)
	from helpers import *	
	import math
	
	signalDenominatorFile = TFile("../SignalScan/T6bbllsleptonDenominatorHisto.root")
	signalDenominatorHisto = TH2F(signalDenominatorFile.Get("massScan"))
	
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
		temphist2 = ROOT.TH1F()
		temphist2.SetFillColor(myColors["DarkRed"],)
		temphist2.SetFillStyle(3002)
		legendHists.append(temphist2.Clone)	


	
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
	intlumi.SetTextSize(0.045)
	intlumi.SetNDC(True)
	scalelabel = ROOT.TLatex()
	scalelabel.SetTextAlign(12)
	scalelabel.SetTextSize(0.03)
	scalelabel.SetNDC(True)
	hCanvas.SetLogy()


	treeEE = readTrees(mainConfig.dataSetPath, "EE")
	treeMuMu = readTrees(mainConfig.dataSetPath, "MuMu")
	treeEMu = readTrees(mainConfig.dataSetPath, "EMu")
 


	

	
	mainConfig.plot.addDilepton(dilepton)	 
	
	plotPad.cd()
	plotPad.SetLogy(0)
	logScale = mainConfig.plot.log
	if mainConfig.plot.variable == "met" or mainConfig.plot.variable == "genMet" or mainConfig.plot.variable == "mht":
		logScale = True
	
	if logScale == True:
		plotPad.SetLogy()

	scaleTree1 = 1.0
	scaleTree2 = 1.0
	if mainConfig.plot.tree1 == "EE":
		tree1 = treeEE
	elif mainConfig.plot.tree1 == "MuMu":
		tree1 = treeMuMu
	elif mainConfig.plot.tree1 == "EMu":
		tree1 = treeEMu				
	else: 
		print "Unknown Dilepton combination! %s not created!"%(mainConfig.plot.filename,)
		return
	
	if mainConfig.plot.tree2 != "None":
		if mainConfig.plot.tree2 == "EE":
				tree2 = treeEE			
		elif mainConfig.plot.tree2 == "MuMu":
				tree2 = treeMuMu

		elif mainConfig.plot.tree2 == "EMu":
				tree2 = treeEMu						
		else:
			print "Unknown Dilepton combination! %s not created!"%(mainConfig.plot.filename,)
			return
	else:
		tree2 = "None"				
	
		
	
	if mainConfig.normalizeToData:
		pickleName=mainConfig.plot.filename%("_scaled_"+mainConfig.runRange.label+"_"+dilepton)
	else:
		pickleName=mainConfig.plot.filename%("_"+mainConfig.runRange.label+"_"+dilepton)		
	
	
	counts = {}
	import pickle
	print mainConfig.plot.cuts
	datahist = getDataHist(mainConfig.plot,tree1,tree2)	
	print datahist.GetEntries()
	stack = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts)

			
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
	if mainConfig.plot.yMax == 0:
		if logScale:
			yMax = yMax*1000
		else:
			yMax = yMax*1.5
						
	else: yMax = plot.yMax
	
	#~ yMax = 220

	plotPad.DrawFrame(mainConfig.plot.firstBin,mainConfig.plot.yMin,mainConfig.plot.lastBin,yMax,"; %s ; %s" %(mainConfig.plot.xaxis,mainConfig.plot.yaxis))
	
	
	

 
	if mainConfig.normalizeToData:
		scalefac = datahist.Integral(datahist.FindBin(mainConfig.plot.firstBin),datahist.FindBin(mainConfig.plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(mainConfig.plot.firstBin),stack.theHistogram.FindBin(mainConfig.plot.lastBin))			

		drawStack = TheStack(processes,mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,1.0,scalefac*scaleTree1,scalefac*scaleTree2)								
					
	
	else:
		drawStack = stack
			

		
	outFilePkl = open("shelves/%s.pkl"%(pickleName),"w")
	pickle.dump(counts, outFilePkl)
	outFilePkl.close()	

	if mainConfig.plotSignal:
		signalhists = []
		signalLabels = []
		for Signal in signals:
			signalhist = Signal.createCombinedHistogram(mainConfig.runRange.lumi,mainConfig.plot,tree1,tree2,signal=True)
			signalhist.SetLineWidth(2)
			signalhist.Add(stack.theHistogram)
			signalhist.SetMinimum(0.1)
			signalhist.Draw("samehist")
			signalhists.append(signalhist)
			signalLabels.append(Signal.label)


	drawStack.theStack.Draw("samehist")							

	dileptonLabel = ""
	if dilepton == "SF":
		dileptonLabel = "ee + #mu#mu"
	if dilepton == "OF":
		dileptonLabel = "e#mu"
	if dilepton == "EE":
		dileptonLabel = "ee"
	if dilepton == "MuMu":
		dileptonLabel = "#mu#mu"

	datahist.SetMinimum(0.1)
	if mainConfig.plotData:
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
	yLabelPos = 0.83
	cmsExtra = ""
	cmsExtra = "Private Work"
	if not mainConfig.plotData:
		cmsExtra = "#splitline{Private Work}{Simulation}"
		yLabelPos = 0.81	
	
	latexCMS.DrawLatex(0.19,0.87,"CMS")
	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))

	if mainConfig.plotRatio:
		ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=mainConfig.plot.firstBin, xMax=mainConfig.plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,color=ROOT.kBlack,adaptiveBinning=0.25)
		ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
		if mainConfig.plotSignal:
			signalRatios = []			
				
			legendRatio = TLegend(0.175, 0.725, 0.65, 0.95)
			legendRatio.SetFillStyle(0)
			legendRatio.SetBorderSize(0)
			legendRatio.SetTextFont(42)
			backgroundHist = ROOT.TH1F()
			legendRatio.AddEntry(backgroundHist,"Data / background","pe")
			temphist = ROOT.TH1F()
			temphist.SetFillColor(myColors["MyGreen"])
		
			for index, signalhist in enumerate(signalhists):
				signalRatios.append(ratios.RatioGraph(datahist,signalhist, xMin=mainConfig.plot.firstBin, xMax=mainConfig.plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,color=signalhist.GetLineColor(),adaptiveBinning=0.25))
				signalRatios[index].draw(ROOT.gPad,False,False,True,chi2Pos=0.7-index*0.1)
				signalhist.SetMarkerColor(signalhist.GetLineColor())
				legendRatio.AddEntry(signalhist,"Data / Background + Signal (%s)"%signalLabels[index],"p")				
			legendRatio.Draw("same")					

	ROOT.gPad.RedrawAxis()
	plotPad.RedrawAxis()
	if mainConfig.plotRatio:

		ratioPad.RedrawAxis()

	nameModifier = mainConfig.runRange.label+"_"+dilepton
	if mainConfig.plotData == False:
		nameModifier+="_MCOnly"
	
	if mainConfig.plotSignal:	
		nameModifier+="_"+signalNameLabel

	if mainConfig.normalizeToData:
		hCanvas.Print("fig/"+mainConfig.plot.filename%("_scaled_"+nameModifier),)
	else:
		hCanvas.Print("fig/"+mainConfig.plot.filename%("_"+nameModifier),)

					


