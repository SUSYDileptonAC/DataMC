def SFvsOF(path,plot,dilepton,logScale,compare2011=False,compareSFvsOFFlavourSeperated=False,compareSFvsOF=True):	
	import ROOT
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


	if compare2011:
		eventCounts = totalNumberOfGeneratedEvents(path,Run2011=True)
		
	else: 
		eventCounts = totalNumberOfGeneratedEvents(path)

	
	
	if compare2011:
		eventCounts = totalNumberOfGeneratedEvents(path,Run2011=True)
		TTJets = Process(Backgrounds2011.TTJets.subprocesses,eventCounts,Backgrounds2011.TTJets.label,Backgrounds2011.TTJets.fillcolor,Backgrounds2011.TTJets.linecolor,Backgrounds2011.TTJets.uncertainty,1,Run2011=True)	
		Diboson = Process(Backgrounds2011.Diboson.subprocesses,eventCounts,Backgrounds2011.Diboson.label,Backgrounds2011.Diboson.fillcolor,Backgrounds2011.Diboson.linecolor,Backgrounds2011.Diboson.uncertainty,1,Run2011=True)	
		DY = Process(Backgrounds2011.DrellYan.subprocesses,eventCounts,Backgrounds2011.DrellYan.label,Backgrounds2011.DrellYan.fillcolor,Backgrounds2011.DrellYan.linecolor,Backgrounds2011.DrellYan.uncertainty,1,Run2011=True)	
		SingleTop = Process(Backgrounds2011.SingleTop.subprocesses,eventCounts,Backgrounds2011.SingleTop.label,Backgrounds2011.SingleTop.fillcolor,Backgrounds2011.SingleTop.linecolor,Backgrounds2011.SingleTop.uncertainty,1,Run2011=True)			
	else:
			
		TTJets = Process(Backgrounds.TTJets.subprocesses,eventCounts,Backgrounds.TTJets.label,Backgrounds.TTJets.fillcolor,Backgrounds.TTJets.linecolor,Backgrounds.TTJets.uncertainty,1)	
		TT = Process(Backgrounds.TT.subprocesses,eventCounts,Backgrounds.TT.label,Backgrounds.TT.fillcolor,Backgrounds.TT.linecolor,Backgrounds.TT.uncertainty,1)	
		TT_MCatNLO = Process(Backgrounds.TT_MCatNLO.subprocesses,eventCounts,Backgrounds.TT_MCatNLO.label,Backgrounds.TT_MCatNLO.fillcolor,Backgrounds.TT_MCatNLO.linecolor,Backgrounds.TT_MCatNLO.uncertainty,1)	
		Diboson = Process(Backgrounds.Diboson.subprocesses,eventCounts,Backgrounds.Diboson.label,Backgrounds.Diboson.fillcolor,Backgrounds.Diboson.linecolor,Backgrounds.Diboson.uncertainty,1)	
		Rare = Process(Backgrounds.Rare.subprocesses,eventCounts,Backgrounds.Rare.label,Backgrounds.Rare.fillcolor,Backgrounds.Rare.linecolor,Backgrounds.Rare.uncertainty,1)	
		DY = Process(Backgrounds.DrellYan.subprocesses,eventCounts,Backgrounds.DrellYan.label,Backgrounds.DrellYan.fillcolor,Backgrounds.DrellYan.linecolor,Backgrounds.DrellYan.uncertainty,1)	
		SingleTop = Process(Backgrounds.SingleTop.subprocesses,eventCounts,Backgrounds.SingleTop.label,Backgrounds.SingleTop.fillcolor,Backgrounds.SingleTop.linecolor,Backgrounds.SingleTop.uncertainty,1)	

	#~ Signal1 = Process(Signals.SUSY1.subprocesses,eventCounts,Signals.SUSY1.label,Signals.SUSY1.fillcolor,Signals.SUSY1.linecolor,Signals.SUSY1.uncertainty,1)
	#~ Signal2 = Process(Signals.SUSY2.subprocesses,eventCounts,Signals.SUSY2.label,Signals.SUSY2.fillcolor,Signals.SUSY2.linecolor,Signals.SUSY2.uncertainty,1)	
	#~ Signal3 = Process(Signals.SUSY3.subprocesses,eventCounts,Signals.SUSY3.label,Signals.SUSY3.fillcolor,Signals.SUSY3.linecolor,Signals.SUSY3.uncertainty,1)	
	#~ Signal4 = Process(Signals.SUSY4.subprocesses,eventCounts,Signals.SUSY4.label,Signals.SUSY4.fillcolor,Signals.SUSY4.linecolor,Signals.SUSY4.uncertainty,1)	
	#~ Signal5 = Process(Signals.SUSY5.subprocesses,eventCounts,Signals.SUSY5.label,Signals.SUSY5.fillcolor,Signals.SUSY5.linecolor,Signals.SUSY5.uncertainty,1)	
	#~ signals = [Signal1]
	#~ signals = [Signal1,Signal2,Signal3,Signal4,Signal5]
	signals = []

	legend = TLegend(0.7, 0.55, 0.95, 0.95)
	legend.SetFillStyle(0)
	legend.SetBorderSize(1)
	legendEta = TLegend(0.15, 0.75, 0.7, 0.95)
	legendEta.SetFillStyle(0)
	legendEta.SetBorderSize(1)


	latex = ROOT.TLatex()
	latex.SetTextSize(0.04)
	latex.SetNDC(True)

	legendHists = []


	


				
	if compare2011:
		processes = [SingleTop,TTJets,Diboson,DY]
	else:
		processes = [Rare,SingleTop,TT,Diboson,DY]


	temphist = ROOT.TH1F()
	temphist2 = ROOT.TH1F()
	temphist3 = ROOT.TH1F()
	temphist4 = ROOT.TH1F()
	temphist.SetLineColor(ROOT.kRed)
	temphist2.SetLineColor(ROOT.kRed)
	temphist3.SetLineColor(ROOT.kBlue)
	temphist4.SetLineColor(ROOT.kBlue)
	temphist.SetMarkerColor(ROOT.kRed)
	temphist2.SetMarkerColor(ROOT.kRed)
	temphist3.SetMarkerColor(ROOT.kBlue)
	temphist4.SetMarkerColor(ROOT.kBlue)
	
	legend.AddEntry(temphist,"Same Flavour MC","p")
	legend.AddEntry(temphist2,"Opposite Flavour MC","l")
	legendEta.AddEntry(temphist,"Same Flavour MC","p")
	legendEta.AddEntry(temphist2,"Opposite Flavour MC","l")
	
	legend.AddEntry(temphist3,"Same Flavour Data","p")
	legend.AddEntry(temphist4,"Opposite Flavour Data","l")
	legendEta.AddEntry(temphist3,"Same Flavour Data","p")
	legendEta.AddEntry(temphist4,"Opposite Flavour Data","l")
	if compareSFvsOFFlavourSeperated:
		legend.Clear()
		legendEta.Clear()
		temphist = ROOT.TH1F()
		temphist2 = ROOT.TH1F()
		temphist3 = ROOT.TH1F()
		temphist4 = ROOT.TH1F()

		temphist.SetLineColor(ROOT.kBlack)
		temphist2.SetLineColor(ROOT.kRed)
		temphist3.SetLineColor(ROOT.kBlue)
		temphist4.SetLineColor(ROOT.kGreen+3)

		temphist.SetMarkerColor(ROOT.kBlack)
		temphist2.SetMarkerColor(ROOT.kRed)
		temphist3.SetMarkerColor(ROOT.kBlue)
		temphist4.SetMarkerColor(ROOT.kGreen+3)

		legend.AddEntry(temphist,"Opposite Flavour Data","p")
		legend.AddEntry(temphist2,"Same Flavour Data EE scaled to OF","p")
		legend.AddEntry(temphist3,"Same Flavour Data MuMu scaled to OF","p")
		legend.AddEntry(temphist4,"MuMu/EE","p")
		legendEta.AddEntry(temphist,"Opposite Flavour Data","p")
		legendEta.AddEntry(temphist2,"Same Flavour Data EE scaled to OF","p")
		legendEta.AddEntry(temphist3,"Same Flavour Data MuMu scaled to OF","p")
		legendEta.AddEntry(temphist4,"MuMu/EE","p")


		
	
	#~ plots = configPlot.get("ThePlots","plots")
	nEvents=-1

	
	ROOT.gStyle.SetOptStat(0)
	
	intlumi = ROOT.TLatex()
	intlumi.SetTextAlign(12)
	intlumi.SetTextSize(0.03)
	intlumi.SetNDC(True)
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


		


	
	treeEE = readTrees(path, "EE")
	treeMuMu = readTrees(path, "MuMu")
	treeEMu = readTrees(path, "EMu")
	if compare2011:
		treeEE = readTrees(path, "EE",Run2011=True)
		treeMuMu = readTrees(path, "MuMu",Run2011=True)
		treeEMu = readTrees(path, "EMu",Run2011=True)

	treeEEMC = treeEE
	treeMuMuMC = treeMuMu
	treeEMuMC = treeEMu
	
	from defs import runRanges
	
	runs = runRanges.runs
	if compare2011:
		runs = [runRanges.Run2011]
	plot.addDilepton(dilepton)	
	
	 
	baseCut = plot.cuts
	for run in runs:
		print plot.cuts 
		plot.cuts=baseCut
		print plot.cuts	
		plot.cuts = plot.cuts%run.runCut
		
		lumi = run.lumi
		printLumi = run.printval

		
		
		plotPad.cd()
		plotPad.SetLogy(0)
		if plot.variable == "met" or plot.variable == "type1Met" or plot.variable == "tcMet" or plot.variable == "caloMet" or plot.variable == "mht":
			logScale = True		
		if logScale == True:
			plotPad.SetLogy()
		
		from defs import getOFScale
		ofScale, ofScaleError = getOFScale()		
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
			scaleTree1 = Constants.Trigger.EffEMu.val*ofScale		
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
					scaleTree2 = Constants.Trigger.EffEMu.val*ofScale					
			else:
				print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
				continue
		else:
			tree2 = "None"
			tree2MC = "None"

		if mainConfig.useTriggerEmulation:
			scaleTree2 = 1.0
			scaleTree1 = 1.0				
	
			


		if compare2011:
			datahist = getDataHist(plot,tree1,tree2,Run2011=True)
		else:
			datahist = getDataHist(plot,tree1,tree2)	
		datahist.GetXaxis().SetTitle(plot.xaxis) 
		datahist.GetYaxis().SetTitle(plot.yaxis)
		

		print plot.cuts
	 
		if plot.yMax == 0:
			if logScale:
				yMax = datahist.GetBinContent(datahist.GetMaximumBin())*1000
			else:
				yMax = datahist.GetBinContent(datahist.GetMaximumBin())*2
		else: yMax = plot.yMax		
		hCanvas.DrawFrame(plot.firstBin,plot.yMin,plot.lastBin,yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))					
		
		stack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)							
		

		if compareSFvsOF or compare2011:
			
			datahist.Scale(ofScale)
			scalefac = datahist.Integral(datahist.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(plot.firstBin),stack.theHistogram.FindBin(plot.lastBin))			
			if mainConfig.normalizeToData:
				drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)
			
			else:
				drawStack = stack
			tree1 = treeEE
			tree2 = treeMuMu 
			tree1MC = treeEEMC
			tree2MC = treeMuMuMC
			if compare2011:
				datahist2 = getDataHist(plot,tree1,tree2,Run2011=True)
			else:	
				datahist2 = getDataHist(plot,tree1,tree2)
			print datahist.Integral()	
			print datahist2.Integral()	
			datahist2.GetXaxis().SetTitle(plot.xaxis) 
			datahist2.GetYaxis().SetTitle(plot.yaxis)
			print scaleTree1, scaleTree2
			tempstack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
			if mainConfig.normalizeToData:
				stackSF = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)	
			else:
				stackSF = tempstack			

			tree1 = treeEMu
			tree2 = "None"
			if mainConfig.plotMC:
				drawStack.theHistogram.SetLineColor(ROOT.kRed)
				drawStack.theHistogram.SetMarkerColor(ROOT.kRed)
				stackSF.theHistogram.SetLineColor(ROOT.kRed)
				stackSF.theHistogram.SetMarkerColor(ROOT.kRed)
				drawStack.theHistogram.SetLineWidth(2)
				stackSF.theHistogram.SetLineWidth(2)
				drawStack.theHistogram.Draw("samehist")	
				stackSF.theHistogram.Draw("samep")

				drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
				drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)
			datahist2.SetMarkerColor(ROOT.kBlue)
			if mainConfig.plotData:
				datahist.SetLineColor(ROOT.kBlue)
				datahist.SetLineWidth(2)
				datahist.Draw("samehist")					
				datahist2.Draw("same")
		elif compareSFvsOFFlavourSeperated:
			datahist.Scale(ofScale)
			tree1 = treeEE
			tree2 = "None" 
			datahistEE = getDataHist(plot,tree1,tree2)	
			datahistEE.GetXaxis().SetTitle(plot.xaxis) 
			datahistEE.GetYaxis().SetTitle(plot.yaxis)				
			tree1 = treeMuMu
			tree2 = "None" 
			datahistMuMu = getDataHist(plot,tree1,tree2)	
			datahistMuMu.GetXaxis().SetTitle(plot.xaxis) 
			datahistMuMu.GetYaxis().SetTitle(plot.yaxis)
			scaleFacEE = datahist.Integral(datahist.FindBin(100),datahist.FindBin(plot.lastBin))/datahistEE.Integral(datahistEE.FindBin(100),datahistEE.FindBin(plot.lastBin))				
			scaleFacMuMu = datahist.Integral(datahist.FindBin(100),datahist.FindBin(plot.lastBin))/datahistMuMu.Integral(datahistMuMu.FindBin(100),datahistMuMu.FindBin(plot.lastBin))				
			datahistEE.Scale(scaleFacEE)	
			datahistMuMu.Scale(scaleFacMuMu)	
			datahistEE.SetMarkerColor(ROOT.kRed)
			datahistMuMu.SetMarkerColor(ROOT.kBlue)
			datahistEE.Draw("samep")
			datahistMuMu.Draw("samep")
			datahist.SetLineColor(ROOT.kBlack)
			#~ datahist.SetLineWidth(2)
			datahist.Draw("samep")					


	 

		if mainConfig.normalizeToData:
			if mainConfig.compareSFvsOF:
				scalelabel.SetTextSize(0.05)
				scalelabel.DrawLatex(0.3,0.8,"MC scaled by %.2f"%(scalefac))

		

		if plot.variable == "eta1" or plot.variable == "eta2":
			legendEta.SetNColumns(2)
			legendEta.Draw()
			intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
		else:

			legend.Draw()

			intlumi.DrawLatex(0.63,0.45,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")		



		if mainConfig.personalWork:
			if compare2011:	
				latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
			else: 
				latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))
		else:
			if compare2011:	
				latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
			else: 
				latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))


		if mainConfig.plotRatio:
			ratioPad.cd()
			#~ ratioPad.SetLogy()


			#~ if compare2011:
#~ 
				#~ ratioGraphs =  ratios.RatioGraph(datahistSF,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=0.25)
				#~ ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)						
				#~ ratioGraphs2 =  ratios.RatioGraph(datahistSF42,datahist42, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=0.25)
				#~ ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
								
			if compareSFvsOF or compare2011:

				ratioGraphs =  ratios.RatioGraph(stackSF.theHistogram,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.5,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=0.25)
				ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
			
				ratioGraphs2 =  ratios.RatioGraph(datahist2,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.5,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=0.25)
				ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)
				
							
			elif compareSFvsOFFlavourSeperated:
					ratioGraphs =  ratios.RatioGraph(datahistEE,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.25)
					ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)					
					ratioGraphs2 =  ratios.RatioGraph(datahistMuMu,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=0.25)
					ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
					ratioGraphs5 =  ratios.RatioGraph(datahistMuMu,datahistEE, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kGreen+3,adaptiveBinning=0.25)
					ratioGraphs5.draw(ROOT.gPad,False,False,True,chi2Pos=0.6)	
				

		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		if mainConfig.plotRatio:

			ratioPad.RedrawAxis()

		if compareSFvsOF:
			if mainConfig.normalizeToData:	
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_scaled_"+run.label),)				
			else: 
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_"+run.label),)
		
		elif compare2011:
			if mainConfig.normalizeToData:
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_2011_scaled_"+run.label,))	
			else:
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_2011_"+run.label),)
		elif compareSFvsOFFlavourSeperated:
			if mainConfig.normalizeToData:
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_FlavourSeperated_scaled_"+run.label),)
			else:
				hCanvas.Print("fig/SFvsOF/"+plot.filename%("_OFvsSF_FlavourSeperated_"+run.label),)		
	
		print plot.cuts
		plot.cuts=baseCut
		print plot.cuts		
