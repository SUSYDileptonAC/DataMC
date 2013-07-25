def plotMCOverlay(path,plots,dilepton,logScale,region="Inclusive",Run2011=False,Run201153X=False):
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



	print plots[0].cuts
	print plots[1].cuts

	
	
	if Run2011 or Run201153X:
		eventCounts = totalNumberOfGeneratedEvents(path,Run2011=True)
		TTJets = Process(Backgrounds2011.TTJets.subprocesses,eventCounts,Backgrounds2011.TTJets.label,Backgrounds2011.TTJets.fillcolor,Backgrounds2011.TTJets.linecolor,Backgrounds2011.TTJets.uncertainty,1,Run2011=True)	
		Diboson = Process(Backgrounds2011.Diboson.subprocesses,eventCounts,Backgrounds2011.Diboson.label,Backgrounds2011.Diboson.fillcolor,Backgrounds2011.Diboson.linecolor,Backgrounds2011.Diboson.uncertainty,1,Run2011=True)	
		DY = Process(Backgrounds2011.DrellYan.subprocesses,eventCounts,Backgrounds2011.DrellYan.label,Backgrounds2011.DrellYan.fillcolor,Backgrounds2011.DrellYan.linecolor,Backgrounds2011.DrellYan.uncertainty,1,Run2011=True)	
		SingleTop = Process(Backgrounds2011.SingleTop.subprocesses,eventCounts,Backgrounds2011.SingleTop.label,Backgrounds2011.SingleTop.fillcolor,Backgrounds2011.SingleTop.linecolor,Backgrounds2011.SingleTop.uncertainty,1,Run2011=True)			
	else:
		eventCounts = totalNumberOfGeneratedEvents(path)	
		TTJets = Process(Backgrounds.TTJets.subprocesses,eventCounts,Backgrounds.TTJets.label,Backgrounds.TTJets.fillcolor,Backgrounds.TTJets.linecolor,Backgrounds.TTJets.uncertainty,1)	
		TT = Process(Backgrounds.TT.subprocesses,eventCounts,Backgrounds.TT.label,Backgrounds.TT.fillcolor,Backgrounds.TT.linecolor,Backgrounds.TT.uncertainty,1)	
		TTJets_SC = Process(Backgrounds.TTJets_SpinCorrelations.subprocesses,eventCounts,Backgrounds.TTJets_SpinCorrelations.label,Backgrounds.TTJets_SpinCorrelations.fillcolor,Backgrounds.TTJets_SpinCorrelations.linecolor,Backgrounds.TTJets_SpinCorrelations.uncertainty,1)	
		TT_MCatNLO = Process(Backgrounds.TT_MCatNLO.subprocesses,eventCounts,Backgrounds.TT_MCatNLO.label,Backgrounds.TT_MCatNLO.fillcolor,Backgrounds.TT_MCatNLO.linecolor,Backgrounds.TT_MCatNLO.uncertainty,1)	
		Diboson = Process(Backgrounds.Diboson.subprocesses,eventCounts,Backgrounds.Diboson.label,Backgrounds.Diboson.fillcolor,Backgrounds.Diboson.linecolor,Backgrounds.Diboson.uncertainty,1)	
		Rare = Process(Backgrounds.Rare.subprocesses,eventCounts,Backgrounds.Rare.label,Backgrounds.Rare.fillcolor,Backgrounds.Rare.linecolor,Backgrounds.Rare.uncertainty,1)	
		DY = Process(Backgrounds.DrellYan.subprocesses,eventCounts,Backgrounds.DrellYan.label,Backgrounds.DrellYan.fillcolor,Backgrounds.DrellYan.linecolor,Backgrounds.DrellYan.uncertainty,1,additionalSelection=Backgrounds.DrellYan.additionalSelection)	
		DYTauTau = Process(Backgrounds.DrellYanTauTau.subprocesses,eventCounts,Backgrounds.DrellYanTauTau.label,Backgrounds.DrellYanTauTau.fillcolor,Backgrounds.DrellYanTauTau.linecolor,Backgrounds.DrellYanTauTau.uncertainty,1,additionalSelection=Backgrounds.DrellYanTauTau.additionalSelection)	
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

	#~ legend, legendEta = prepareLegends()

	latex = ROOT.TLatex()
	latex.SetTextSize(0.04)
	latex.SetNDC(True)

	legendHists = []
	

	legendHistData = ROOT.TH1F()	
	#~ legend.AddEntry(legendHistData,"Data","p")	
	#~ legendEta.AddEntry(legendHistData,"Data","p")	

	

	
	if Run2011 or Run201153X:
		processes = [SingleTop,TTJets,Diboson,DY]
	else:
		#~ processes = [Rare,SingleTop,TTJets_SC,Diboson,DYTauTau,DY]
		processes = [TTJets_SC]

	#~ for process in reversed(processes):
		#~ temphist = ROOT.TH1F()
		#~ temphist.SetFillColor(process.theColor)
		#~ legendHists.append(temphist.Clone)
		#~ legend.AddEntry(temphist,process.label,"f")
		#~ legendEta.AddEntry(temphist,process.label,"f")
		if mainConfig.plotSignal:
			processes.append(Signal)
	temphist = ROOT.TH1F()
	temphist.SetFillColor(ROOT.kRed)
	temphist.SetLineColor(ROOT.kRed)
	temphist.SetMarkerColor(ROOT.kRed)
	temphist2 = ROOT.TH1F()
	temphist2.SetFillColor(ROOT.kBlack)
	temphist2.SetLineColor(ROOT.kBlack)
	temphist2.SetMarkerColor(ROOT.kBlack)
	legend.AddEntry(temphist,plots[0].regionName+" data","p")
	legendEta.AddEntry(temphist,plots[0].regionName+" data","p")
	if plots[1].overlayLabel != "None":
		legend.AddEntry(temphist2,plots[1].regionName+" data "+plots[1].overlayLabel,"p")
		legendEta.AddEntry(temphist2,plots[1].regionName+" data "+plots[1].overlayLabel,"p")
	else:
		legend.AddEntry(temphist2,plots[1].regionName+" data","p")
		legendEta.AddEntry(temphist2,plots[1].regionName+" data","p")
	legend.AddEntry(temphist,plots[0].regionName+" MC","l")
	legendEta.AddEntry(temphist,plots[0].regionName+" MC","l")
	if plots[1].overlayLabel != "None":
		legend.AddEntry(temphist2,plots[1].regionName+" MC "+plots[1].overlayLabel,"l")
		legendEta.AddEntry(temphist2,plots[1].regionName+" MC "+plots[1].overlayLabel,"l")
	else:
		legend.AddEntry(temphist2,plots[1].regionName+" MC","l")
		legendEta.AddEntry(temphist2,plots[1].regionName+" MC","l")
		#~ if mainConfig.plotSignal:
			#~ processes.append(Signal)



	
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
	intlumi.SetTextSize(0.03)
	intlumi.SetNDC(True)
	intlumi2 = ROOT.TLatex()
	intlumi2.SetTextAlign(12)
	intlumi2.SetTextSize(0.03)
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
	
	plots[0].addDilepton(dilepton)	
	plots[1].addDilepton(dilepton)	
	 

	baseCut = plots[0].cuts
	baseCut2 = plots[1].cuts
	for run in runs:
		plots[0].cuts=baseCut
		plots[0].cuts = plots[0].cuts%run.runCut
		plots[1].cuts=baseCut2
		plots[1].cuts = plots[1].cuts%run.runCut
		lumi = run.lumi
		printLumi = run.printval
		
		
		if mainConfig.useVectorTrees:
			plot.cuts = plot.cuts.replace("met","vMet.Pt()")
			plot.cuts = plot.cuts.replace("pt1","lepton1.Pt()")
			plot.cuts = plot.cuts.replace("pt2","lepton2.Pt()")
			plot.cuts = plot.cuts.replace("eta1","lepton1.Eta()")
			plot.cuts = plot.cuts.replace("eta2","lepton2.Eta()")
			plot.cuts = plot.cuts.replace("deltaR","sqrt((lepton1.Eta()-lepton2.Eta())^2+(lepton1.Phi()-lepton2.Phi())^2)")
			#~ plot.cuts = plot.cuts.replace("deltaR","1")
		
		
		plotPad.cd()
		plotPad.SetLogy(0)
		
		if plots[0].variable == "met" or plots[0].variable == "type1Met" or plots[0].variable == "tcMet" or plots[0].variable == "caloMet" or plots[0].variable == "mht":
			logScale = True
		
		if logScale == True:
			plotPad.SetLogy()
		
		#~ from defs import getOFScale
		#~ ofScale, ofScaleError = getOFScale()		
		scaleTree1 = 1.0
		scaleTree2 = 1.0
		if plots[0].tree1 == "EE":
			tree1 = treeEE
			tree1MC = treeEEMC
			scaleTree1 = Constants.Trigger.EffEE.val
		elif plots[0].tree1 == "MuMu":
			tree1 = treeMuMu
			tree1MC = treeMuMuMC
			scaleTree1 = Constants.Trigger.EffMuMu.val		
		elif plots[0].tree1 == "EMu":
			tree1 = treeEMu	
			tree1MC = treeEMuMC	
			scaleTree1 = Constants.Trigger.EffEMu.val			
		else: 
			print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
			continue
		
		if plots[0].tree2 != "None":
			if plots[0].tree2 == "EE":
					tree2 = treeEE
					tree2MC = treeEEMC
					scaleTree2 = Constants.Trigger.EffEE.val				
			elif plots[0].tree2 == "MuMu":
					tree2 = treeMuMu
					tree2MC = treeMuMuMC
					scaleTree2 = Constants.Trigger.EffMuMu.val

			elif plots[0].tree2 == "EMu":
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
		
			
		

		
		stack = TheStack(processes,lumi,plots[0],tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=False)
		stack2 = TheStack(processes,lumi,plots[1],tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=False)
		
		#~ stack.theHistogram.Scale(1./stack.theHistogram.Integral())
		#~ stack2.theHistogram.Scale(1./stack2.theHistogram.Integral())
		#~ datahist = getDataHist(plots[0],tree1,tree2)
		#~ datahist2 = getDataHist(plots[1],tree1,tree2)
		#~ datahist2.Scale(1./datahist2.Integral())
		#~ datahist.Scale(1./datahist.Integral())
		#~ stack.theHistogram.Scale(1./stack.theHistogram.Integral())
		stack2.theHistogram.Scale(stack.theHistogram.Integral()/stack2.theHistogram.Integral())
		datahist = getDataHist(plots[0],tree1,tree2)
		datahist2 = getDataHist(plots[1],tree1,tree2)
		datahist2.Scale(datahist.Integral()/datahist2.Integral())
		#~ datahist.Scale(1./datahist.Integral())
		if plots[0].yMax == 0:
			if logScale:
				yMax = stack.theHistogram.GetBinContent(stack.theHistogram.GetMaximumBin())*1000
			else:
				yMax = stack.theHistogram.GetBinContent(stack.theHistogram.GetMaximumBin())*2
		else: yMax = plots[0].yMax	
		#~ yMax = 1.	
		#~ yMin = 0.001
		hCanvas.DrawFrame(plots[0].firstBin,plots[0].yMin,plots[0].lastBin,yMax,"; %s ; %s" %(plots[0].xaxis,plots[0].yaxis))
		

	 
	
		stack.theHistogram.Draw("samehist")
		stack.theHistogram.SetLineColor(ROOT.kRed)							
		stack.theHistogram.SetMarkerColor(ROOT.kRed)							
		stack2.theHistogram.Draw("samehist")							
				
		datahist.SetMarkerColor(ROOT.kRed)
		datahist.SetLineColor(ROOT.kRed)
		datahist.Draw("samep")
		datahist2.Draw("samep")
			
		dileptonLabel = ""
		if dilepton == "SF":
			dileptonLabel = "ee+#mu#mu"
		if dilepton == "OF":
			dileptonLabel = "e#mu"
		if dilepton == "EE":
			dileptonLabel = "ee"
		if dilepton == "MuMu":
			dileptonLabel = "#mu#mu"


		if plots[0].variable == "eta1" or plots[0].variable == "eta2":
			legendEta.SetNColumns(2)
			legendEta.Draw()
			if plots[1].overlayLabel != "None":
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plots[0].label+" "+dileptonLabel+"}{#splitline{"+plots[0].regionName+" & "+plots[1].regionName+" "+plots[1].overlayLabel+"}{"+plots[0].label3+"}}")				
				
			else:	
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plots[0].label+" "+dileptonLabel+"}{#splitline{"+plots[0].regionName+" & "+plots[1].regionName+"}{"+plots[0].label3+"}}")				
		else:
			legend.Draw()
			if plots[1].overlayLabel != "None":
				intlumi.DrawLatex(0.63,0.45,"#splitline{"+plots[0].label+" "+dileptonLabel+"}{#splitline{"+plots[0].regionName+" & "+plots[1].regionName+" "+plots[1].overlayLabel+"}{"+plots[0].label3+"}}")	
			else:
				intlumi.DrawLatex(0.63,0.45,"#splitline{"+plots[0].label+" "+dileptonLabel+"}{#splitline{"+plots[0].regionName+" & "+plots[1].regionName+"}{"+plots[0].label3+"}}")	

		

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
			if plots[1].overlayLabel != "None":
				ratioGraphs =  ratios.RatioGraph(stack.theHistogram,stack2.theHistogram, xMin=plots[0].firstBin, xMax=plots[0].lastBin,title="#frac{%s}{%s}"%(plots[0].regionName,plots[1].regionName+" "+plots[1].overlayLabel),yMin=0.0,yMax=3,ndivisions=15,color=ROOT.kBlack,adaptiveBinning=0.25)
			else:
				ratioGraphs =  ratios.RatioGraph(stack.theHistogram,stack2.theHistogram, xMin=plots[0].firstBin, xMax=plots[0].lastBin,title="#frac{%s}{%s}"%(plots[0].regionName,plots[1].regionName),yMin=0.0,yMax=3,ndivisions=15,color=ROOT.kBlack,adaptiveBinning=0.25)				
			ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
			ratioGraphs2 =  ratios.RatioGraph(datahist,datahist2, xMin=plots[0].firstBin, xMax=plots[0].lastBin,title="#frac{%s}{%s}"%(plots[0].regionName,plots[1].regionName),yMin=0.0,yMax=3,ndivisions=15,color=ROOT.kRed,adaptiveBinning=0.25)
			ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.8)
		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		if mainConfig.plotRatio:

			ratioPad.RedrawAxis()




			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_TopReweighted_"+run.label+"_"+dilepton),)
		#~ if plots[1].overlayLabel != "None":
			#~ hCanvas.Print("fig/DataMCOverlay/"+plots[0].filename%("_"+plots[1].regionName+"Overlay"+"_"+plots[1].overlayLabel+"_"+run.label+"_"+dilepton),)			
		#~ else:	
			#~ hCanvas.Print("fig/DataMCOverlay/"+plots[0].filename%("_"+plots[1].regionName+"Overlay"+"_"+run.label+"_"+dilepton),)
		if plots[1].overlayLabel != "None":
			hCanvas.Print("fig/DataMCOverlay/"+"TTOnly_"+plots[0].filename%("_"+plots[1].regionName+"Overlay"+"_"+plots[1].overlayLabel+"_"+run.label+"_"+dilepton),)			
		else:	
			hCanvas.Print("fig/DataMCOverlay/"+"TTOnly_"+plots[0].filename%("_"+plots[1].regionName+"Overlay"+"_"+run.label+"_"+dilepton),)
			#~ plotPad.cd()
			#~ plotPad.SetLogy(0)
			#~ hCanvas.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ plotPad.Range(plot.firstBin,0,plot.lastBin,1000)
			#~ plotPad.RedrawAxis()
			#~ datahist.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_"+run.label+"_"+dilepton+"_NoLog"),)
						
	plots[0].cuts=baseCut
	plots[1].cuts=baseCut2
	
