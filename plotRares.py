def plotRares(path,plot,dilepton,logScale,region="Inclusive",Run2011=False,Run201153X=False):
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
	

	plotPad = ROOT.TPad("plotPad","plotPad",0,0,1,1)
	setTDRStyle()
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()	
		
	colors = createMyColors()		



	

	eventCounts = totalNumberOfGeneratedEvents(path)	
	Rare = Process(Backgrounds.Rare.subprocesses,eventCounts,Backgrounds.Rare.label,Backgrounds.Rare.fillcolor,Backgrounds.Rare.linecolor,Backgrounds.Rare.uncertainty,1)	
	
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
	legend.AddEntry(legendHistData,"Data","p")	
	legendEta.AddEntry(legendHistData,"Data","p")	

	

	

	processes = [Rare]

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
		legend.AddEntry(temphist2,"JEC Uncert.","f")	


	
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
	
	plot.addDilepton(dilepton)	
	 

	baseCut = plot.cuts
	for run in runs:
		plot.cuts=baseCut
		plot.cuts = plot.cuts%run.runCut
		lumi = run.lumi
		printLumi = run.printval
		
		print plot.cuts
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
			
		#~ if mainConfig.useTriggerEmulation:
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
		plot.lastBin = 250.
		stack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts)
		ofStack = TheStack(processes,lumi,plot,treeEMu,"None",1.0,scaleTree1,scaleTree2,saveIntegrals=True,counts=counts)

	
		
		if plot.yMax == 0:
			if logScale:
				yMax = stack.theHistogram.GetBinContent(stack.theHistogram.GetMaximumBin())*1000
			else:
				yMax = stack.theHistogram.GetBinContent(stack.theHistogram.GetMaximumBin())*2
		else: yMax = plot.yMax		
		hCanvas.DrawFrame(plot.firstBin,-yMax,plot.lastBin,yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))
		

		drawStack = stack
	


				
		
			
		dileptonLabel = ""
		if dilepton == "SF":
			dileptonLabel = "ee+#mu#mu"
			drawStack.theHistogram.Add(ofStack.theHistogram,-0.5*(1.10+1./1.10))
		if dilepton == "OF":
			dileptonLabel = "e#mu"
		if dilepton == "EE":
			dileptonLabel = "ee"
			drawStack.theHistogram.Add(ofStack.theHistogram,-1/(1+1.10**2))
		if dilepton == "MuMu":
			dileptonLabel = "#mu#mu"
			drawStack.theHistogram.Add(ofStack.theHistogram,-(1.10**2)/(1+1.10**2))
						

		drawStack.theHistogram.Draw("samehist")			
		print drawStack.theHistogram.Integral()				
		drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
		drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)
		

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

	


		ROOT.gPad.RedrawAxis()
		plotPad.RedrawAxis()



		nameModifier = run.label+"_"+dilepton
		if mainConfig.doTopReweighting:
			nameModifier+="_TopReweighted"



			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_TopReweighted_"+run.label+"_"+dilepton),)
		hCanvas.Print("fig/DataMC/"+plot.filename%("_"+nameModifier+"_Rares"),)
			#~ plotPad.cd()
			#~ plotPad.SetLogy(0)
			#~ hCanvas.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ plotPad.Range(plot.firstBin,0,plot.lastBin,1000)
			#~ plotPad.RedrawAxis()
			#~ datahist.GetYaxis().SetRangeUser(0,datahist.GetBinContent(datahist.GetMaximumBin())*2)
			#~ hCanvas.Print("fig/DataMC/"+plot.filename%("_"+run.label+"_"+dilepton+"_NoLog"),)
						
	plot.cuts=baseCut
	
