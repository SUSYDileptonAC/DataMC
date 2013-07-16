def compareReco2011(path,plot,dilepton,logScale,doSFvsOF=False):
	
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



	eventCounts = totalNumberOfGeneratedEvents(path)

	
	


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
	

	legendHistData = TH1F()
	legendHistData42 = TH1F()

	legend.Clear()
	legendEta.Clear()
	legendHistData.SetLineColor(ROOT.kBlue)
	legend.AddEntry(legendHistData,"2011 Data in 53X","l")	
	legendEta.AddEntry(legendHistData,"2011 Data in 53X","l")			
	legendHistData42 = ROOT.TH1F()	
	legendHistData42.SetLineColor(ROOT.kRed)
	legend.AddEntry(legendHistData42,"2011 Data in 42X","l")	
	legendEta.AddEntry(legendHistData42,"2011 Data in 42X","l")
	if doSFvsOF:
		legend.Clear()
		legendEta.Clear()
		legendHistData.SetMarkerColor(ROOT.kBlue)
		legend.AddEntry(legendHistData,"2011 Data in 53X SF","p")	
		legendEta.AddEntry(legendHistData,"2011 Data in 53X SF","p")
		
		legendHistDataOF = ROOT.TH1F()	
		legendHistDataOF.SetLineColor(ROOT.kBlue)
		legend.AddEntry(legendHistDataOF,"2011 Data in 53X OF","l")	
		legendEta.AddEntry(legendHistDataOF,"2011 Data in 53X OF","l")				
						
		legendHistData42 = ROOT.TH1F()	
		legendHistData42.SetMarkerColor(ROOT.kRed)
		legend.AddEntry(legendHistData42,"2011 Data in 42X SF","p")	
		legendEta.AddEntry(legendHistData42,"2011 Data in 42X SF","p")					
				
		legendHistDataOF42 = ROOT.TH1F()	
		legendHistDataOF42.SetLineColor(ROOT.kRed)
		legend.AddEntry(legendHistDataOF42,"2011 Data in 42X OF","l")	
		legendEta.AddEntry(legendHistDataOF42,"2011 Data in 42X OF","l")					



		
	
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
	



	treeEE42X = readTrees(path, "EE",Run2011=True)
	treeMuMu42X = readTrees(path, "MuMu",Run2011=True)
	treeEMu42X = readTrees(path, "EMu",Run2011=True)
	treeEE53X = readTrees(path, "EE")
	treeMuMu53X = readTrees(path, "MuMu")
	treeEMu53X = readTrees(path, "EMu")




	from defs import runRanges
	
	runs = [runRanges.Run2011]
	
	plot.addDilepton(dilepton)	
	
	 

	baseCut = plot.cuts
	for run in runs:
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
		

		if plot.tree1 == "EE":
			tree1 = treeEE42X
			tree153X = treeEE53X
		elif plot.tree1 == "MuMu":
			tree1 = treeMuMu42X
			tree153X = treeMuMu53X			
		elif plot.tree1 == "EMu":
			tree1 = treeEMu42X	
			tree153X = treeEMu53X			
		else: 
			print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
			continue
		
		if plot.tree2 != "None":
			if plot.tree2 == "EE":
					tree2 = treeEE42X
					tree253X = treeEE53X					
			elif plot.tree2 == "MuMu":
					tree2 = treeMuMu42X
					tree253X = treeMuMu53X
			elif plot.tree2 == "EMu":
					tree2 = treeEMu42X
					tree253X = treeEMu53X					
			else:
				print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
				continue
		else:
			tree2 = "None"
			tree253X = "None"
			
		
			
		
		print doSFvsOF	
			

		
		datahist42X = getDataHist(plot,tree1,tree2,Run2011=True)	
		datahist42X.GetXaxis().SetTitle(plot.xaxis) 
		datahist42X.GetYaxis().SetTitle(plot.yaxis)
		
		print datahist42X.Integral()
		print plot.cuts
		if plot.yMax == 0:
			if logScale:
				yMax = datahist42X.GetBinContent(datahist42X.GetMaximumBin())*1000
			else:
				yMax = datahist42X.GetBinContent(datahist42X.GetMaximumBin())*2
		else: yMax = plot.yMax		
		hCanvas.DrawFrame(plot.firstBin,plot.yMin,plot.lastBin,yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))


		datahist53X = getDataHist(plot,tree153X,tree253X,Run201153X=True)	
		datahist53X.GetXaxis().SetTitle(plot.xaxis) 
		datahist53X.GetYaxis().SetTitle(plot.yaxis)	
		datahist53X.SetLineColor(ROOT.kBlue)	
			
		datahist53X.SetLineWidth(2)	
		datahist53X.Draw("samehist")
		datahist42X.SetLineColor(ROOT.kRed)
		datahist42X.SetLineWidth(2)
		datahist42X.Draw("samehist")	
		if doSFvsOF:
			datahistSF53X = getDataHist(plot,treeEE53X,treeMuMu53X,Run201153X=True)
			datahistSF42X = getDataHist(plot,treeEE42X,treeMuMu42X,Run2011=True)
			datahistSF53X.SetMarkerColor(ROOT.kBlue)		
			datahistSF42X.SetMarkerColor(ROOT.kRed)
			datahistSF53X.Draw("samep")		
			datahistSF42X.Draw("samep")		
		
		dileptonLabel = ""
		if dilepton == "SF":
			dileptonLabel = "ee+#mu#mu"
		if dilepton == "OF":
			dileptonLabel = "e#mu"
		if dilepton == "EE":
			dileptonLabel = "ee"
		if dilepton == "MuMu":
			dileptonLabel = "#mu#mu"		
		if doSFvsOF:
			if plot.variable == "eta1" or plot.variable == "eta2":
				#~ stack.theStack.SetMaximum(2*stack.theStack.GetMaximum())
				legendEta.SetNColumns(2)
				legendEta.Draw()
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
			else:

				legend.Draw()

				intlumi.DrawLatex(0.63,0.45,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
		else:
			if plot.variable == "eta1" or plot.variable == "eta2":
				#~ stack.theStack.SetMaximum(2*stack.theStack.GetMaximum())
				legendEta.SetNColumns(2)
				legendEta.Draw()
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
			else:

				legend.Draw()

				intlumi.DrawLatex(0.63,0.45,"#splitline{"+plot.label+" "+dileptonLabel+"}{#splitline{"+plot.label2+"}{"+plot.label3+"}}")	
		
		if mainConfig.personalWork:
			latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")

		else:
			latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")



		if mainConfig.plotRatio:
			ratioPad.cd()



			
			if doSFvsOF:
				ratioGraphs =  ratios.RatioGraph(datahistSF53X,datahist53X, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=0.25)
				ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)						
				ratioGraphs2 =  ratios.RatioGraph(datahistSF42X,datahist42X, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=0.25)
				ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
									
			else:
				ratioGraphs =  ratios.RatioGraph(datahist53X,datahist42X, xMin=plot.firstBin, xMax=plot.lastBin,title="53X / 42X",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlack,adaptiveBinning=0.25)
				ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
								

		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()
		if mainConfig.plotRatio:

			ratioPad.RedrawAxis()


		

		if doSFvsOF:
			hCanvas.Print("fig/2011Reco/"+plot.filename%("_CompareReco_OFvsSF_"+run.label),)
		else:	
			hCanvas.Print("fig/2011Reco/"+plot.filename%("_CompareReco_"+run.label+"_"+dilepton),)

		print plot.cuts
		plot.cuts=baseCut
		print plot.cuts			
