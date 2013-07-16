def compareTTbar(path,plot,dilepton,logScale):	

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
	#~ from defs import ThePlots
	from setTDRStyle import setTDRStyle
	
	from helpers import *	

	
	hCanvas = TCanvas("hCanvas", "Distribution", 800,800)
	
	if mainConfig.plotRatio:
		plotPad = ROOT.TPad("plotPad","plotPad",0,0.4,1,1)
		ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0.2,1,0.4)
		ratioPad2 = ROOT.TPad("ratioPad","ratioPad",0,0.,1,0.2)
		setTDRStyle()		
		plotPad.UseCurrentStyle()
		ratioPad.UseCurrentStyle()
		ratioPad2.UseCurrentStyle()
		plotPad.Draw()	
		ratioPad.Draw()	
		ratioPad2.Draw()	
		plotPad.cd()
	else:
		plotPad = ROOT.TPad("plotPad","plotPad",0,0,1,1)
		setTDRStyle()
		plotPad.UseCurrentStyle()
		plotPad.Draw()	
		plotPad.cd()	
		
	colors = createMyColors()		



	eventCounts = totalNumberOfGeneratedEvents(path)

	
	


			
	TTJets = Process(Backgrounds.TTJets.subprocesses,eventCounts,Backgrounds.TTJets.label,Backgrounds.TTJets.fillcolor,Backgrounds.TTJets.linecolor,Backgrounds.TTJets.uncertainty,1)	
	TTJets_SC = Process(Backgrounds.TTJets_SpinCorrelations.subprocesses,eventCounts,Backgrounds.TTJets_SpinCorrelations.label,Backgrounds.TTJets_SpinCorrelations.fillcolor,Backgrounds.TTJets_SpinCorrelations.linecolor,Backgrounds.TTJets_SpinCorrelations.uncertainty,1)	
	TT = Process(Backgrounds.TT.subprocesses,eventCounts,Backgrounds.TT.label,Backgrounds.TT.fillcolor,Backgrounds.TT.linecolor,Backgrounds.TT.uncertainty,1)	
	TT_MCatNLO = Process(Backgrounds.TT_MCatNLO.subprocesses,eventCounts,Backgrounds.TT_MCatNLO.label,Backgrounds.TT_MCatNLO.fillcolor,Backgrounds.TT_MCatNLO.linecolor,Backgrounds.TT_MCatNLO.uncertainty,1)	
	Diboson = Process(Backgrounds.Diboson.subprocesses,eventCounts,Backgrounds.Diboson.label,Backgrounds.Diboson.fillcolor,Backgrounds.Diboson.linecolor,Backgrounds.Diboson.uncertainty,1)	
	Rare = Process(Backgrounds.Rare.subprocesses,eventCounts,Backgrounds.Rare.label,Backgrounds.Rare.fillcolor,Backgrounds.Rare.linecolor,Backgrounds.Rare.uncertainty,1)	
	DY = Process(Backgrounds.DrellYan.subprocesses,eventCounts,Backgrounds.DrellYan.label,Backgrounds.DrellYan.fillcolor,Backgrounds.DrellYan.linecolor,Backgrounds.DrellYan.uncertainty,1)	
	SingleTop = Process(Backgrounds.SingleTop.subprocesses,eventCounts,Backgrounds.SingleTop.label,Backgrounds.SingleTop.fillcolor,Backgrounds.SingleTop.linecolor,Backgrounds.SingleTop.uncertainty,1)	



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
	
	legendHistData = ROOT.TH1F()	
	legend.AddEntry(legendHistData,"Data","p")	
	legendEta.AddEntry(legendHistData,"Data","p")	

	processes = [Rare,Diboson,SingleTop,DY]
	legendHistTT = ROOT.TH1F()
	legendHistTT.SetLineColor(ROOT.kRed)
	legendHistTT_MCatNLO = ROOT.TH1F()
	legendHistTT_MCatNLO.SetLineColor(ROOT.kGreen+3)
	legendHistTTJets = ROOT.TH1F()
	legendHistTTJets.SetLineColor(ROOT.kBlue)	
	legendHistTTJets_SC = ROOT.TH1F()
	legendHistTTJets_SC.SetLineColor(ROOT.kBlue+3)	
	legend.AddEntry(legendHistTT,"Powheg t#bar{t}","l")
	legend.AddEntry(legendHistTT_MCatNLO,"MCatNLO t#bar{t}","l")
	legend.AddEntry(legendHistTTJets,"Madgraph t#bar{t}","l")
	legend.AddEntry(legendHistTTJets_SC,"Madgraph t#bar{t} w/ SC","l")
	legendEta.AddEntry(legendHistTT,"Powheg t#bar{t}","l")
	legendEta.AddEntry(legendHistTT_MCatNLO,"MCatNLO t#bar{t}","l")
	legendEta.AddEntry(legendHistTTJets,"Madgraph t#bar{t}","l")				
	legendEta.AddEntry(legendHistTTJets_SC,"Madgraph t#bar{t} w/ SC","l")				
	for process in reversed(processes):
		temphist = ROOT.TH1F()
		temphist.SetFillColor(process.theColor)
		legendHists.append(temphist.Clone)
		legend.AddEntry(temphist,process.label,"f")
		legendEta.AddEntry(temphist,process.label,"f")

				
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


	if mainConfig.useVectorTrees:
		treeEE = readVectorTrees(path, "EE")
		treeMuMu = readVectorTrees(path, "MuMu")
		treeEMu = readVectorTrees(path, "EMu")		




	else:
		treeEE = readTrees(path, "EE")
		treeMuMu = readTrees(path, "MuMu")
		treeEMu = readTrees(path, "EMu")

	treeEEMC = treeEE
	treeMuMuMC = treeMuMu
	treeEMuMC = treeEMu
	
	from defs import runRanges
	
	runs = runRanges.runs
	
	plot.addDilepton(dilepton)
	
	 
	print plot.cuts
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
			scaleTree1 = Constants.Trigger.EffEMu.val			
		else: 
			print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
			continue
		
		if plot.tree2 != "None":
			if plot.tree2 == "EE":
					tree2 = treeEE
					tree2MC = treeEEMC
					scaleTree2 = Constants.Trigger.EffEE.val
					if (mainConfig.plot2011 and mainConfig.plot53X):
						tree253X = treeEE53X					
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
		


		datahist = getDataHist(plot,tree1,tree2)	
		datahist.GetXaxis().SetTitle(plot.xaxis) 
		datahist.GetYaxis().SetTitle(plot.yaxis)
		
		if plot.yMax == 0:
			if logScale:
				yMax = datahist.GetBinContent(datahist.GetMaximumBin())*1000
			else:
				yMax = datahist.GetBinContent(datahist.GetMaximumBin())*2
		else: yMax = plot.yMax		
		
		print plot.yMin,yMax
		hCanvas.DrawFrame(plot.firstBin,plot.yMin,plot.lastBin,yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))				
			
		
		stack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)

		

		print plot.cuts
	 
		if mainConfig.normalizeToData:
			scalefac = datahist.Integral(datahist.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(plot.firstBin),stack.theHistogram.FindBin(plot.lastBin))			

			drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)	
			stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,0.955,scalefac*scaleTree1,scalefac*scaleTree2)	
			stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.045,scalefac*scaleTree1,scalefac*scaleTree2)	
		
		
		else:
			drawStack = stack
			plot.cuts = plot.cuts.replace("met", "metJESUp")	
			plot.cuts = plot.cuts.replace(" ht", "htJESUp")		
			plot.cuts = plot.cuts.replace("nJets", "nShiftedJetsJESUp")
			stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
			plot.cuts = plot.cuts.replace("metJESUp", "metJESDown")
			plot.cuts = plot.cuts.replace("htJESUp", "htJESDown")
			plot.cuts = plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")					
			stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
			plot.cuts = plot.cuts.replace("metJESDown", "met")
			plot.cuts = plot.cuts.replace("htJESDown", "ht")
			plot.cuts = plot.cuts.replace("nShiftedJetsJESDown", "nJets")	




		drawStack.theStack.Draw("samehist")							
		drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
		drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)

				
		
			
		stack2 = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)		
		stack3 = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)		
		stack4 = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)		
		hist = TT.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
		hist3 = TT_MCatNLO.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
		hist2 = TTJets.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
		hist4 = TTJets_SC.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
		hist2.GetXaxis().SetTitle(plot.xaxis)
			
		if mainConfig.normalizeToData:
			scalefactor1 =(datahist.Integral(hist.FindBin(plot.firstBin),hist.FindBin(plot.lastBin)) - stack.theHistogram.Integral(hist.FindBin(plot.firstBin),hist.FindBin(plot.lastBin))) /  hist.Integral(hist.FindBin(plot.firstBin),hist.FindBin(plot.lastBin)) 
			scalefactor2 =(datahist.Integral(hist2.FindBin(plot.firstBin),hist2.FindBin(plot.lastBin)) - stack.theHistogram.Integral(hist2.FindBin(plot.firstBin),hist2.FindBin(plot.lastBin))) /  hist2.Integral(hist2.FindBin(plot.firstBin),hist2.FindBin(plot.lastBin)) 
			hist.Scale(scalefactor1)
			hist2.Scale(scalefactor2)
			scalelabel.DrawLatex(0.6,0.4,"#splitline{Madgraph scaled by %.2f }{Powheg scaled by %.2f}"%(scalefactor2,scalefactor1))
			print scalefactor1
		hist2.GetYaxis().SetTitle(plot.yaxis)
		hist.SetFillColor(0)								
		hist2.SetFillColor(0)
		hist3.SetFillColor(0)
		hist4.SetFillColor(0)
		hist.SetLineColor(ROOT.kRed)								
		hist2.SetLineColor(ROOT.kBlue)								
		hist3.SetLineColor(ROOT.kGreen+3)								
		hist4.SetLineColor(ROOT.kBlue+3)								
		hist.SetLineWidth(2)
		hist2.SetLineWidth(2)					
		hist3.SetLineWidth(2)					
		hist4.SetLineWidth(2)					
		drawStack.theStack.Add(hist)
		stack2.theStack.Add(hist2)
		stack3.theStack.Add(hist3)
		stack4.theStack.Add(hist4)
		drawStack.theHistogram.Add(hist)
		stack2.theHistogram.Add(hist2)
		stack3.theHistogram.Add(hist3)
		stack4.theHistogram.Add(hist4)
		stack2.theStack.Draw("samehist")	
		stack3.theStack.Draw("samehist")	
		stack4.theStack.Draw("samehist")	
						

		datahist.SetMinimum(0.1)	
		datahist.Draw("samep")	
				

		dileptonLabel = ""
		if dilepton == "SF":
			dileptonLabel = "ee+#mu#mu"
		if dilepton == "OF":
			dileptonLabel = "e#mu"
		if dilepton == "EE":
			dileptonLabel = "ee"
		if dilepton == "MuMu":
			dileptonLabel = "#mu#mu"
		

		if plot.variable == "eta1" or plot.variable == "eta2":
			legendEta.SetNColumns(2)
			legendEta.Draw()
			intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
		else:

			legend.Draw()

			intlumi.DrawLatex(0.63,0.45,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	



		
		if mainConfig.personalWork:

			latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))
		else:

			latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))


		if mainConfig.plotRatio:
			ratioPad.cd()


			ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.5)
			ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)				
			ratioGraphs2 =  ratios.RatioGraph(datahist,stack2.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=0.5)
			ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
			ratioGraphs3 =  ratios.RatioGraph(datahist,stack3.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kGreen+3,adaptiveBinning=0.5)
			ratioGraphs3.draw(ROOT.gPad,False,False,True,chi2Pos=0.7)	
			ratioGraphs4 =  ratios.RatioGraph(datahist,stack4.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.0,yMax=2,ndivisions=10,color=ROOT.kBlue+3,adaptiveBinning=0.5)
			ratioGraphs4.draw(ROOT.gPad,False,False,True,chi2Pos=0.7)	
			ratioPad2.cd()
			ratioGraphs5 =  ratios.RatioGraph(hist,hist2, xMin=plot.firstBin, xMax=plot.lastBin,title="MC / Madgraph",yMin=0.5,yMax=1.5,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.5,labelSize=0.15)
			ratioGraphs5.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)				
			ratioGraphs6 =  ratios.RatioGraph(hist3,hist2, xMin=plot.firstBin, xMax=plot.lastBin,title="Madgraph(MCatNLO) / Powheg",yMin=0.5,yMax=1.5,ndivisions=10,color=ROOT.kGreen+3,adaptiveBinning=0.5,labelSize=0.12)
			ratioGraphs6.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)				
			ratioGraphs7 =  ratios.RatioGraph(hist4,hist2, xMin=plot.firstBin, xMax=plot.lastBin,title="Madgraph(MCatNLO) / Powheg",yMin=0.5,yMax=1.5,ndivisions=10,color=ROOT.kBlue+3,adaptiveBinning=0.5,labelSize=0.12)
			ratioGraphs7.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)				
		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		if mainConfig.plotRatio:

			ratioPad.RedrawAxis()

	

		if mainConfig.useTriggerEmulation:
			hCanvas.Print("fig/CompareTTbar/"+plot.filename%("_TTbarCompare_TriggerEmulation_"+run.label+"_"+dilepton),)
		else:
			hCanvas.Print("fig/CompareTTbar/"+plot.filename%("_TTbarCompare_"+run.label+"_"+dilepton),)		
		
		print plot.cuts
		plot.cuts=baseCut
		print plot.cuts		
		print "Ende"
