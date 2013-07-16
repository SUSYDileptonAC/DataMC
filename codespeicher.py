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

	
	
	if mainConfig.plot2011:
		TTJets = Process(Backgrounds2011.TTJets.subprocesses,eventCounts,Backgrounds2011.TTJets.label,Backgrounds2011.TTJets.fillcolor,Backgrounds2011.TTJets.linecolor,Backgrounds2011.TTJets.uncertainty,1)	
		Diboson = Process(Backgrounds2011.Diboson.subprocesses,eventCounts,Backgrounds2011.Diboson.label,Backgrounds2011.Diboson.fillcolor,Backgrounds2011.Diboson.linecolor,Backgrounds2011.Diboson.uncertainty,1)	
		DY = Process(Backgrounds2011.DrellYan.subprocesses,eventCounts,Backgrounds2011.DrellYan.label,Backgrounds2011.DrellYan.fillcolor,Backgrounds2011.DrellYan.linecolor,Backgrounds2011.DrellYan.uncertainty,1)	
		SingleTop = Process(Backgrounds2011.SingleTop.subprocesses,eventCounts,Backgrounds2011.SingleTop.label,Backgrounds2011.SingleTop.fillcolor,Backgrounds2011.SingleTop.linecolor,Backgrounds2011.SingleTop.uncertainty,1)			
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

	legend, legendEta = prepareLegends()

	latex = ROOT.TLatex()
	latex.SetTextSize(0.04)
	latex.SetNDC(True)

	legendHists = []
	
	if mainConfig.plotData == True:
		legendHistData = ROOT.TH1F()	
		legend.AddEntry(legendHistData,"Data","p")	
		legendEta.AddEntry(legendHistData,"Data","p")	

	
	if mainConfig.compare2011:
		legend.Clear()
		legendEta.Clear()
		legend.AddEntry(legendHistData,"2011 Data in 53X","p")	
		legendEta.AddEntry(legendHistData,"2011 Data in 53X","p")			
		legendHistData42 = ROOT.TH1F()	
		legendHistData42.SetLineColor(ROOT.kRed)
		legend.AddEntry(legendHistData42,"2011 Data in 42X","l")	
		legendEta.AddEntry(legendHistData42,"2011 Data in 42X","l")
		if mainConfig.compareSFvsOF:
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
	if mainConfig.compareTTbar == True:
		processes = [Rare,Diboson,SingleTop,DY]
		legendHistTT = ROOT.TH1F()
		legendHistTT.SetLineColor(ROOT.kRed)
		legendHistTT_MCatNLO = ROOT.TH1F()
		legendHistTT_MCatNLO.SetLineColor(ROOT.kGreen+3)
		legendHistTTJets = ROOT.TH1F()
		legendHistTTJets.SetLineColor(ROOT.kBlue)	
		legend.AddEntry(legendHistTT,"Powheg t#bar{t}","l")
		legend.AddEntry(legendHistTT_MCatNLO,"MCatNLO t#bar{t}","l")
		legend.AddEntry(legendHistTTJets,"Madgraph t#bar{t}","l")
		legendEta.AddEntry(legendHistTT,"Powheg t#bar{t}","l")
		legendEta.AddEntry(legendHistTT_MCatNLO,"MCatNLO t#bar{t}","l")
		legendEta.AddEntry(legendHistTTJets,"Madgraph t#bar{t}","l")				
		for process in reversed(processes):
			temphist = ROOT.TH1F()
			temphist.SetFillColor(process.theColor)
			legendHists.append(temphist.Clone)
			legend.AddEntry(temphist,process.label,"f")
			legendEta.AddEntry(temphist,process.label,"f")

				
	elif mainConfig.plotMC == True:
		if mainConfig.plot2011:
			processes = [SingleTop,TTJets,Diboson,DY]
		else:
			processes = [Rare,SingleTop,TT,Diboson,DY]
			#~ processes = [TT]

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
	elif mainConfig.compareTTbar == False and mainConfig.plotMC == False:
		processes = []

	
	if mainConfig.plotSignal:
		for Signal in signals:
			temphist = ROOT.TH1F()
			temphist.SetFillColor(Signal.theColor)
			temphist.SetLineColor(Signal.theLineColor)
			legendHists.append(temphist.Clone)		
			legend.AddEntry(temphist,Signal.label,"l")
			legendEta.AddEntry(temphist,Signal.label,"l")
	
	
	if mainConfig.compareSFvsOF and not mainConfig.compare2011:
		legend.Clear()
		legendEta.Clear()
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
		if mainConfig.plotMC:
			legend.AddEntry(temphist,"Same Flavour MC","p")
			legend.AddEntry(temphist2,"Opposite Flavour MC","l")
			legendEta.AddEntry(temphist,"Same Flavour MC","p")
			legendEta.AddEntry(temphist2,"Opposite Flavour MC","l")
		if mainConfig.plotData:
			legend.AddEntry(temphist3,"Same Flavour Data","p")
			legend.AddEntry(temphist4,"Opposite Flavour Data","l")
			legendEta.AddEntry(temphist3,"Same Flavour Data","p")
			legendEta.AddEntry(temphist4,"Opposite Flavour Data","l")
	if mainConfig.compareSFvsOFFlavourSeperated:
		legend.Clear()
		legendEta.Clear()
		temphist = ROOT.TH1F()
		temphist2 = ROOT.TH1F()
		temphist3 = ROOT.TH1F()

		temphist.SetLineColor(ROOT.kBlack)
		temphist2.SetLineColor(ROOT.kRed)
		temphist3.SetLineColor(ROOT.kBlue)

		temphist.SetMarkerColor(ROOT.kBlack)
		temphist2.SetMarkerColor(ROOT.kRed)
		temphist3.SetMarkerColor(ROOT.kBlue)

		legend.AddEntry(temphist,"Opposite Flavour Data","p")
		legend.AddEntry(temphist2,"Same Flavour Data EE scaled","p")
		legend.AddEntry(temphist3,"Same Flavour Data MuMu scaled","p")
		legendEta.AddEntry(temphist,"Opposite Flavour Data","p")
		legendEta.AddEntry(temphist2,"Same Flavour Data EE scaled","p")
		legendEta.AddEntry(temphist3,"Same Flavour Data MuMu scaled","p")


		
	
	#~ plots = configPlot.get("ThePlots","plots")
	plots = ThePlots()
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
	#~ lumi = Constants.Lumi.val
	if mainConfig.plot2011:
		lumi = 4980

	if mainConfig.useVectorTrees:
		treeEE = readVectorTrees(path, "EE")
		treeMuMu = readVectorTrees(path, "MuMu")
		treeEMu = readVectorTrees(path, "EMu")		


	elif mainConfig.plot2011:
		treeEE = readTrees42(path, "EE")
		treeMuMu = readTrees42(path, "MuMu")
		treeEMu = readTrees42(path, "EMu")
		treeEE53X = readTrees(path, "EE")
		treeMuMu53X = readTrees(path, "MuMu")
		treeEMu53X = readTrees(path, "EMu")



	else:
		treeEE = readTrees(path, "EE")
		treeMuMu = readTrees(path, "MuMu")
		treeEMu = readTrees(path, "EMu")
	if mainConfig.compare2011:
		treeEE42 = readTrees42(path, "EE")
		treeMuMu42 = readTrees42(path, "MuMu")
		treeEMu42 = readTrees42(path, "EMu")

: 
	treeEEMC = treeEE
	treeMuMuMC = treeMuMu
	treeEMuMC = treeEMu
	
	from defs import runRanges
	
	runs = runRanges.runs
	
	
	 
	for index, plot in enumerate(plots.thePlots):
		baseCut = plot.cuts
		for run in runs:
			print plot.cuts 
			plot.cuts=baseCut
			print plot.cuts	
			plot.cuts = plot.cuts+run.runCut
			
			lumi = run.lumi
			printLumi = run.printval
			
			
			if mainConfig.useVectorTrees:
				print plot.cuts
				plot.cuts = plot.cuts.replace("met","vMet.Pt()")
				plot.cuts = plot.cuts.replace("pt1","lepton1.Pt()")
				plot.cuts = plot.cuts.replace("pt2","lepton2.Pt()")
				plot.cuts = plot.cuts.replace("eta1","lepton1.Eta()")
				plot.cuts = plot.cuts.replace("eta2","lepton2.Eta()")
				plot.cuts = plot.cuts.replace("deltaR","sqrt((lepton1.Eta()-lepton2.Eta())^2+(lepton1.Phi()-lepton2.Phi())^2)")
				#~ plot.cuts = plot.cuts.replace("deltaR","1")
				print plot.cuts
			
			
			plotPad.cd()
			plotPad.SetLogy(0)
			if plot.log == True:
				plotPad.SetLogy()
			
			from defs import getOFScale
			ofScale, ofScaleError = getOFScale()		
			scaleTree1 = 1.0
			scaleTree2 = 1.0
			if plot.tree1 == "EE":
				tree1 = treeEE
				tree1MC = treeEEMC
				scaleTree1 = Constants.Trigger.EffEE.val
				if (mainConfig.plot2011 and mainConfig.plot53X):
					tree153X = treeEE53X
			elif plot.tree1 == "MuMu":
				tree1 = treeMuMu
				tree1MC = treeMuMuMC
				scaleTree1 = Constants.Trigger.EffMuMu.val
				if (mainConfig.plot2011 and mainConfig.plot53X):
					tree153X = treeMuMu53X			
			elif plot.tree1 == "EMu":
				tree1 = treeEMu	
				tree1MC = treeEMuMC	
				scaleTree1 = Constants.Trigger.EffEMu.val*ofScale
				if (mainConfig.plot2011 and mainConfig.plot53X):
					tree153X = treeEMu53X			
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
						if (mainConfig.plot2011 and mainConfig.plot53X):
							tree253X = treeMuMu53X
				elif plot.tree2 == "EMu":
						tree2 = treeEMu	
						tree2MC = treeEMuMC	
						scaleTree2 = Constants.Trigger.EffEMu.val*ofScale
						if (mainConfig.plot2011 and mainConfig.plot53X):
							tree253X = treeEMu53X					
				else:
					print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
					continue
			else:
				tree2 = "None"
				tree2MC = "None"
				if (mainConfig.plot2011 and mainConfig.plot53X):
					tree253X = "None"
				
			
				
			if mainConfig.compare2011:	
				if plot.tree1 == "EE":
					tree142 = treeEE42
				elif plot.tree1 == "MuMu":
					tree142 = treeMuMu42
				elif plot.tree1 == "EMu":
					tree142 = treeEMu42	
				else: 
					print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
					continue
				
				if plot.tree2 != "None":
					if plot.tree2 == "EE":
							tree242 = treeEE42
					elif plot.tree2 == "MuMu":
							tree242 = treeMuMu42
					elif plot.tree2 == "EMu":
							tree242 = treeEMu42	
					else:
						print "Unknown Dilepton combination! %s not created!"%(plot.filename,)
						continue
				else:
					tree242 = "None"
			if mainConfig.useTriggerEmulation:
				scaleTree2 = 1.0
				scaleTree1 = 1.0				
			#~ scaleTree2 = 1.0
			#~ scaleTree1 = 1.0				
				
				
			hCanvas.DrawFrame(plot.firstBin,plot.yMin,plot.lastBin,plot.yMax,"; %s ; %s" %(plot.xaxis,plot.yaxis))
			
			stack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)

			if mainConfig.plot2011:
				if mainConfig.plot53X:
					datahist = getDataHist(plot,tree153X,tree253X)
				else:
					datahist = getDataHist42(plot,tree1,tree2)
			else:
				datahist = getDataHist(plot,tree1,tree2)	
			datahist.GetXaxis().SetTitle(plot.xaxis) 
			datahist.GetYaxis().SetTitle(plot.yaxis)
			
			#~ print "Hier! %d"%(datahist.Integral(0,40),)	

			print plot.cuts
		 
			if mainConfig.normalizeToData:
				scalefac = datahist.Integral(datahist.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/stack.theHistogram.Integral(stack.theHistogram.FindBin(plot.firstBin),stack.theHistogram.FindBin(plot.lastBin))			

				drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)
				#~ plot.cuts = plot.cuts.replace("met", "metJESUp")	
				#~ print plot.cuts	
				#~ plot.cuts = plot.cuts.replace("ht", "htJESUp")		
				#~ print plot.cuts
				#~ plot.cuts = plot.cuts.replace("nJets", "nShiftedJetsJESUp")		
				#~ print plot.cuts		
				stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,0.955,scalefac*scaleTree1,scalefac*scaleTree2)
				#~ plot.cuts = plot.cuts.replace("metJESUp", "metJESDown")
				#~ plot.cuts = plot.cuts.replace("htJESUp", "htJESDown")
				#~ plot.cuts = plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")	
				stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.045,scalefac*scaleTree1,scalefac*scaleTree2)	
				#~ plot.cuts = plot.cuts.replace("metJESDown", "met")
				#~ plot.cuts = plot.cuts.replace("htJESDown", "ht")
				#~ plot.cuts = plot.cuts.replace("nShiftedJetsJESDown", "nJets")							
			
			elif mainConfig.useVectorTrees or mainConfig.plot2011: 
				drawStack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
				#~ plot.cuts = plot.cuts.replace("met", "metJESUp")	
				#~ print plot.cuts	
				#~ plot.cuts = plot.cuts.replace("ht", "htJESUp")		
				#~ print plot.cuts
				#~ plot.cuts = plot.cuts.replace("nJets", "nShiftedJetsJESUp")		
				#~ print plot.cuts		
				stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,0.955,scaleTree1,scaleTree2)
				#~ plot.cuts = plot.cuts.replace("metJESUp", "metJESDown")
				#~ plot.cuts = plot.cuts.replace("htJESUp", "htJESDown")
				#~ plot.cuts = plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")	
				stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.045,scaleTree1,scaleTree2)				
			
			else:
				drawStack = stack
				plot.cuts = plot.cuts.replace("met", "metJESUp")	
				#~ print plot.cuts	
				plot.cuts = plot.cuts.replace(" ht", "htJESUp")		
				#~ print plot.cuts
				plot.cuts = plot.cuts.replace("nJets", "nShiftedJetsJESUp")
				#~ print plot.cuts						
				stackJESUp = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
				plot.cuts = plot.cuts.replace("metJESUp", "metJESDown")
				plot.cuts = plot.cuts.replace("htJESUp", "htJESDown")
				plot.cuts = plot.cuts.replace("nShiftedJetsJESUp", "nShiftedJetsJESDown")					
				stackJESDown = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
				plot.cuts = plot.cuts.replace("metJESDown", "met")
				plot.cuts = plot.cuts.replace("htJESDown", "ht")
				plot.cuts = plot.cuts.replace("nShiftedJetsJESDown", "nJets")	

			if mainConfig.compareSFvsOF and not mainConfig.compareSFvsOFFlavourSeperated:
				
				datahist.Scale(ofScale)
				tree1 = treeEE
				tree2 = treeMuMu 
				tree1MC = treeEEMC
				tree2MC = treeMuMuMC
				datahist2 = getDataHist(plot,tree1,tree2)	
				datahist2.GetXaxis().SetTitle(plot.xaxis) 
				datahist2.GetYaxis().SetTitle(plot.yaxis)
				print scaleTree1, scaleTree2
				tempstack = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
				if mainConfig.normalizeToData:
					#~ scalefacSF = datahist.Integral(datahist2.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/tempstack.theHistogram.Integral(tempstack.theHistogram.FindBin(plot.firstBin),tempstack.theHistogram.FindBin(plot.lastBin))			
					stackSF = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scalefac*scaleTree1,scalefac*scaleTree2)	
					#~ scalefacDataSF = datahist.Integral(datahist2.FindBin(plot.firstBin),datahist.FindBin(plot.lastBin))/datahist2.Integral(datahist2.FindBin(plot.firstBin),datahist2.FindBin(plot.lastBin))
					#~ datahist2.Scale(scalefacDataSF)			
				else:
					stackSF = tempstack			

				tree1 = treeEMu
				tree2 = "None"
				if mainConfig.plotMC:
					drawStack.theHistogram.SetLineColor(ROOT.kRed)
					drawStack.theHistogram.SetMarkerColor(ROOT.kRed)
					if not mainConfig.normalizeToData:
						#~ drawStack.theHistogram.Scale(ofScale)
						print stackSF.theHistogram.Integral()/drawStack.theHistogram.Integral()
					stackSF.theHistogram.SetLineColor(ROOT.kRed)
					stackSF.theHistogram.SetMarkerColor(ROOT.kRed)
					drawStack.theHistogram.SetLineWidth(2)
					stackSF.theHistogram.SetLineWidth(2)
					#~ stackSF.theHistogram.Scale(stack.theHistogram.Integral(stack.theHistogram.FindBin(0),stack.theHistogram.FindBin(150))/stackSF.theHistogram.Integral(stackOF.theHistogram.FindBin(0),stackOF.theHistogram.FindBin(150)))
					drawStack.theHistogram.Draw("samehist")	
					stackSF.theHistogram.Draw("samep")

					drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
					drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)
				datahist2.SetMarkerColor(ROOT.kBlue)
				if mainConfig.plotData:
					datahist2.Draw("same")
			elif mainConfig.compareSFvsOFFlavourSeperated:
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
				
				
			elif mainConfig.plotMC:		
				drawStack.theStack.Draw("samehist")							
				drawStack.theStack.GetXaxis().SetTitle(plot.xaxis) 
				drawStack.theStack.GetYaxis().SetTitle(plot.yaxis)
			if mainConfig.plotSignal:
				signalhists = []
				for Signal in signals:
					signalhist = Signal.createCombinedHistogram(lumi,plot,tree1,tree2)
					signalhist.SetLineWidth(2)
					signalhist.Add(stack.theHistogram)
					signalhist.SetMinimum(0.1)
					signalhist.Draw("samehist")
					signalhists.append(signalhist)
					
			
				
			if mainConfig.compareTTbar:
				stack2 = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)		
				stack3 = TheStack(processes,lumi,plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)		
				hist = TT.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
				hist3 = TT_MCatNLO.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)	
				#~ hist.Scale(0.6)				
				hist2 = TTJets.createCombinedHistogram(lumi, plot,tree1MC,tree2MC,1.0,scaleTree1,scaleTree2)
				hist2.GetXaxis().SetTitle(plot.xaxis)
				#~ hist2.Scale(0.6) 
				
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
				hist.SetLineColor(ROOT.kRed)								
				hist2.SetLineColor(ROOT.kBlue)								
				hist3.SetLineColor(ROOT.kGreen+3)								
				hist.SetLineWidth(2)
				hist2.SetLineWidth(2)					
				hist3.SetLineWidth(2)					
				drawStack.theStack.Add(hist)
				stack2.theStack.Add(hist2)
				stack3.theStack.Add(hist3)
				drawStack.theHistogram.Add(hist)
				stack2.theHistogram.Add(hist2)
				stack3.theHistogram.Add(hist3)
				stack2.theStack.Draw("samehist")	
				stack3.theStack.Draw("samehist")	
							
			if mainConfig.plotData:			
				datahist.SetMinimum(0.1)
				if mainConfig.compareSFvsOF:
					datahist.SetLineColor(ROOT.kBlue)
					datahist.SetLineWidth(2)
					#datahist.Scale(datahist2.Integral(datahist2.FindBin(0),datahist2.FindBin(150))/datahist.Integral(datahist.FindBin(0),datahist.FindBin(50)))
					datahist.Draw("samehist")
				else:	
					datahist.Draw("samep")	
					
	#~ 
			if mainConfig.compare2011:	
				datahist42 = getDataHist42(plot,tree142,tree242)	
				datahist42.GetXaxis().SetTitle(plot.xaxis) 
				datahist42.GetYaxis().SetTitle(plot.yaxis)	
				datahist42.SetLineColor(ROOT.kRed)	
				
				datahist42.SetLineWidth(2)	
				datahist42.Draw("samehist")
				if mainConfig.compareSFvsOF:
					datahistSF = getDataHist(plot,treeEE,treeMuMu)
					datahistSF42 = getDataHist42(plot,treeEE42,treeMuMu42)
					datahistSF.SetMarkerColor(ROOT.kBlue)		
					datahistSF42.SetMarkerColor(ROOT.kRed)
					datahistSF.Draw("samep")		
					datahistSF42.Draw("samep")		
			
			if mainConfig.normalizeToData and not mainConfig.compareTTbar:
				#~ scalelabel.DrawLatex(0.6,0.4,"t#bar{t}t#bar{t} scaled by %.2f"%(Backgrounds.TT.scaleFac))
				if mainConfig.compareSFvsOF:
					#~ scalelabel.DrawLatex(0.3,0.8,"All scaled to OF Data!")
					scalelabel.SetTextSize(0.05)
					scalelabel.DrawLatex(0.3,0.8,"MC scaled by %.2f"%(scalefac))
					#~ scalelabel.DrawLatex(0.6,0.35,"SF MC scaled by %.2f"%(scalefacSF))
					#~ scalelabel.DrawLatex(0.6,0.3,"SF Data scaled by %.2f"%(scalefacDataSF))
				else:
					scalelabel.DrawLatex(0.6,0.4,"Background scaled by %.2f"%(scalefac))
			

			if plot.variable == "eta1" or plot.variable == "eta2":
				#~ stack.theStack.SetMaximum(2*stack.theStack.GetMaximum())
				legendEta.SetNColumns(2)
				legendEta.Draw()
				intlumi.DrawLatex(0.2,0.7,"#splitline{"+plot.label+"}{"+plot.label2+"}")	
			else:
				#~ if plot.log == True:	
					#~ stack.theStack.SetMaximum(5*stack.theStack.GetMaximum())
				#~ else:	
					#~ stack.theStack.SetMaximum(1.2*stack.theStack.GetMaximum())
				legend.Draw()
				if (mainConfig.plot2011 and not mainConfig.plot53X):
					intlumi.DrawLatex(0.7,0.5,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{Data and MC in 4_2_X}}")	
				elif (mainConfig.plot2011 and mainConfig.plot53X):
					intlumi.DrawLatex(0.7,0.5,"#splitline{"+plot.label+"}{#splitline{"+plot.label2+"}{Data in 5_3_X, MC in 4_2_X}}")	
				else:
					intlumi.DrawLatex(0.7,0.5,"#splitline{"+plot.label+"}{"+plot.label2+"}")	


			if (plot.variable == "p4.Pt()" or plot.variable == "met" or plot.variable == "type1Met" or plot.variable == "tcMet" or plot.variable == "caloMet" or plot.variable == "mht") and not mainConfig.compareSFvsOF and not mainConfig.compareTTbar and not mainConfig.compare2011 and not mainConfig.compareSFvsOFFlavourSeperated:
				from math import sqrt
				lowerBound = 130
				if plot.variable == "p4.Pt()":
					lowerBound = 0				
				intData = datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(400))
				errIntData = sqrt(datahist.Integral(datahist.FindBin(lowerBound),datahist.FindBin(400)))
				errIntMC = ROOT.Double()
				intMC = drawStack.theHistogram.IntegralAndError(drawStack.theHistogram.FindBin(lowerBound),drawStack.theHistogram.FindBin(400),errIntMC)
				if sqrt(errIntData**2+errIntMC**2)> 0:
					sigma = (intMC-intData)/sqrt(errIntData**2+errIntMC**2)
					
				else:
					 sigma = 0
				
	#~ 

				bin130 = datahist.FindBin(lowerBound)
				bin400 = datahist.FindBin(400)
				i = bin130
				chi2 = 0
				while i <= bin400:
					if datahist.GetBinError(i) > 0 and drawStack.theHistogram.GetBinError(i)>0:
						chi2 = chi2 + (abs(datahist.GetBinContent(i)-drawStack.theHistogram.GetBinContent(i))/sqrt(datahist.GetBinError(i)**2+drawStack.theHistogram.GetBinError(i)**2))**2
					i = i+1
				

				metDiffLabel.SetTextSize(0.05)
				metDiffLabel.DrawLatex(0.25,0.83,"#splitline{Integral in Region %d GeV to 400 GeV}{#splitline{Data: %d \pm %.2f}{#splitline{MC: %.2f \pm %.2f}{Significance: %.2f #sigma_{stat}}}}"%(lowerBound,intData,errIntData,intMC,errIntMC,sigma))
				chi2Label.SetTextSize(0.05)
				chi2Label.DrawLatex(0.4,0.7,"Chi^{2}/N_{dof} = %.2f / %d"%(chi2,(bin400-bin130-1)))
			
			if mainConfig.personalWork:
				if mainConfig.compare2011 or mainConfig.plot2011:	
					latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
				else: 
					latex.DrawLatex(0.15, 0.96, "CMS Private Work  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))
					#~ latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.05 fb^{-1}")
			else:
				if mainConfig.compare2011 or mainConfig.plot2011:	
					latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.0 fb^{-1}")
				else: 
					latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 8 TeV,     #scale[0.6]{#int}Ldt = %s fb^{-1}"%(printLumi,))
					#~ latex.DrawLatex(0.15, 0.96, "CMS Preliminary  #sqrt{s} = 7 TeV,     #scale[0.6]{#int}Ldt = 5.05 fb^{-1}")

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
				print weights
				print sumOfEntries/sumOfWeightedEntries
			if mainConfig.plotRatio:
				ratioPad.cd()
				#~ ratioPad.SetLogy()

				if mainConfig.compareTTbar:
					ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.5)
					ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)				
					ratioGraphs2 =  ratios.RatioGraph(datahist,stack2.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=0.5)
					ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
					ratioGraphs3 =  ratios.RatioGraph(datahist,stack3.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kGreen+3,adaptiveBinning=0.5)
					ratioGraphs3.draw(ROOT.gPad,False,False,True,chi2Pos=0.7)	
					#~ ratioPad2.cd()
					#~ ratioPad2.SetLogy()
					#~ ratioGraphs4 =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=100000)
					#~ ratioGraphs4.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)				
					#~ ratioGraphs5 =  ratios.RatioGraph(datahist,stack2.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=1000000)
					#~ ratioGraphs5.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
					#~ ratioGraphs6 =  ratios.RatioGraph(datahist,stack3.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kGreen+3,adaptiveBinning=1000000)
					#~ ratioGraphs6.draw(ROOT.gPad,False,False,True,chi2Pos=0.7)	
				elif mainConfig.compare2011:
					if mainConfig.compareSFvsOF:
						ratioGraphs =  ratios.RatioGraph(datahistSF,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=0.25)
						ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)						
						ratioGraphs2 =  ratios.RatioGraph(datahistSF42,datahist42, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=0.25)
						ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
						#~ ratioPad2.cd()
						#~ ratioPad2.SetLogy()
						#~ ratioGraphs3 =  ratios.RatioGraph(datahistSF,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=100000)
						#~ ratioGraphs3.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)						
						#~ ratioGraphs4 =  ratios.RatioGraph(datahistSF42,datahist42, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=100000)
						#~ ratioGraphs4.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)										
					else:
						ratioGraphs =  ratios.RatioGraph(datahist,datahist42, xMin=plot.firstBin, xMax=plot.lastBin,title="53X / 42X",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.25)
						ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
						#~ ratioPad2.cd()
						#~ ratioPad2.SetLogy()
						#~ ratioGraphs2 =  ratios.RatioGraph(datahist,datahist42, xMin=plot.firstBin, xMax=plot.lastBin,title="53X / 42X",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=100000)
						#~ ratioGraphs2.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)										
				elif mainConfig.compareSFvsOF:
					if mainConfig.plotMC:
						ratioGraphs =  ratios.RatioGraph(stackSF.theHistogram,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.5,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=0.25)
						ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
						if mainConfig.plotData:					
							ratioGraphs2 =  ratios.RatioGraph(datahist2,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.5,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=0.25)
							ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)
						#~ ratioPad2.cd()
						#~ ratioPad2.SetLogy()
						#~ ratioGraphs3 =  ratios.RatioGraph(stackSF.theHistogram,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.3333,yMax=3,ndivisions=30,color=ROOT.kRed,adaptiveBinning=10000)
						#~ ratioGraphs3.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
						#~ if mainConfig.plotData:					
							#~ ratioGraphs4 =  ratios.RatioGraph(datahist2,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.33333,yMax=3,ndivisions=30,color=ROOT.kBlue,adaptiveBinning=10000)
							#~ ratioGraphs4.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)						
					else:
						ratioGraphs =  ratios.RatioGraph(datahist2,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=0.25)
						ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
						#~ ratioPad2.cd()
						#~ ratioPad2.SetLogy()										
						#~ ratioGraphs2 =  ratios.RatioGraph(datahist2,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=10000)
						#~ ratioGraphs2.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)										
				elif mainConfig.compareSFvsOFFlavourSeperated:
						ratioGraphs =  ratios.RatioGraph(datahistEE,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=0.25)
						ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)					
						ratioGraphs2 =  ratios.RatioGraph(datahistMuMu,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=0.25)
						ratioGraphs2.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)	
						ratioGraphs5 =  ratios.RatioGraph(datahistMuMu,datahistEE, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kGreen,adaptiveBinning=0.25)
						ratioGraphs5.draw(ROOT.gPad,False,False,True,chi2Pos=0.6)	
						#~ ratioPad2.cd()
						#~ ratioPad2.SetLogy()				
						#~ ratioGraphs3 =  ratios.RatioGraph(datahistEE,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kRed,adaptiveBinning=10000)
						#~ ratioGraphs3.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)					
						#~ ratioGraphs4 =  ratios.RatioGraph(datahistMuMu,datahist, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlue,adaptiveBinning=100000)
						#~ ratioGraphs4.draw(ROOT.gPad,False,False,True,chi2Pos=0.2)					
						#~ ratioGraphs6 =  ratios.RatioGraph(datahistMuMu,datahistEE, xMin=plot.firstBin, xMax=plot.lastBin,title="SF / OF",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kGreen,adaptiveBinning=100000)
						#~ ratioGraphs6.draw(ROOT.gPad,False,False,True,chi2Pos=0.6)					
				else: 
					ratioGraphs =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlack,adaptiveBinning=0.25)
					ratioGraphs.addErrorByHistograms( "Xsecs", drawStack.theHistogramXsecUp, drawStack.theHistogramXsecDown,color=myColors["MyGreen"])
					ratioGraphs.addErrorBySize("Effs",0.06726812023536856,color=myColors["MyGreen"],add=True)
					#~ ratioGraphs.addErrorBySize("Lumi",0.045,color=myColors["MyGreen"],add=True)				
					ratioGraphs.addErrorByHistograms( "JES", stackJESUp.theHistogram, stackJESDown.theHistogram,color= myColors["DarkRed"],fillStyle=3002,add=True)
					ratioGraphs.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)
					if mainConfig.plotSignal:
						signalRatios = []
						for index, signalhist in enumerate(signalhists):
							signalRatios.append(ratios.RatioGraph(datahist,signalhist, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=signalhist.GetLineColor(),adaptiveBinning=0.25))
							signalRatios[index].draw(ROOT.gPad,False,False,True,chi2Pos=0.7-index*0.1)				
					#~ ratioPad2.cd()
					#~ ratioPad2.SetLogy()				
					#~ ratioGraphs2 =  ratios.RatioGraph(datahist,drawStack.theHistogram, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=ROOT.kBlack,adaptiveBinning=1000000000)
					#~ ratioGraphs2.addErrorByHistograms( "Xsecs", drawStack.theHistogramXsecUp, drawStack.theHistogramXsecDown,color=myColors["MyGreen"])
					#~ ratioGraphs2.addErrorBySize("Effs",0.06726812023536856,color=myColors["MyGreen"],add=True)
					#~ ratioGraphs.addErrorBySize("Lumi",0.045,color=myColors["MyGreen"],add=True)				
					#~ ratioGraphs2.addErrorByHistograms( "JES", stackJESUp.theHistogram, stackJESDown.theHistogram,color= myColors["DarkRed"],fillStyle=3002)

					#~ ratioGraphs2.draw(ROOT.gPad,True,False,True,chi2Pos=0.8)

					#~ if mainConfig.plotSignal:
						#~ signalRatios2 = []
						#~ for index, signalhist in enumerate(signalhists):
							#~ signalRatios2.append(ratios.RatioGraph(datahist,signalhist, xMin=plot.firstBin, xMax=plot.lastBin,title="Data / MC",yMin=0.333333,yMax=3,ndivisions=10,color=signalhist.GetLineColor(),adaptiveBinning=10000))
							#~ signalRatios2[index].draw(ROOT.gPad,False,False,True,chi2Pos=0.7-index*0.1)
			ROOT.gPad.RedrawAxis()
			plotPad.RedrawAxis()
			if mainConfig.plotRatio:

				ratioPad.RedrawAxis()
				#~ ratioPad2.RedrawAxis()

			if mainConfig.compareSFvsOF and not mainConfig.compare2011:
				if mainConfig.normalizeToData:	
					hCanvas.Print(plot.filename%("_OFvsSF_scaled_"+run.label),)				
				else: 
					hCanvas.Print(plot.filename%("_OFvsSF_"+run.label),)
			
			elif mainConfig.compareSFvsOF and mainConfig.compare2011:
				if mainConfig.normalizeToData:
					hCanvas.Print(plot.filename%("_OFvsSF_2011_scaled_"+run.label,))	
				else:
					hCanvas.Print(plot.filename%("_OFvsSF_2011_"+run.label),)
			elif mainConfig.compareSFvsOFFlavourSeperated:
				if mainConfig.normalizeToData:
					hCanvas.Print(plot.filename%("_OFvsSF_FlavourSeperated_scaled_"+run.label),)
				else:
					hCanvas.Print(plot.filename%("_OFvsSF_FlavourSeperated_"+run.label),)		
			elif mainConfig.compareTTbar:
				if mainConfig.useTriggerEmulation:
					hCanvas.Print(plot.filename%("_TTbarCompare_TriggerEmulation_"+run.label),)
				else:
					hCanvas.Print(plot.filename%("_TTbarCompare_"+run.label),)		
			else:
				if mainConfig.normalizeToData:
					hCanvas.Print(plot.filename%("_scaled_"+run.label),)
				elif mainConfig.useTriggerEmulation:
					hCanvas.Print(plot.filename%("_TriggerEmulation_"+run.label),)
				elif mainConfig.plot2011:
					if mainConfig.plot53X:
						hCanvas.Print(plot.filename%("_2011_53X_"+run.label),)
					else:
						hCanvas.Print(plot.filename%("_2011_"+run.label),)
				else:
					hCanvas.Print(plot.filename%("_"+run.label),)			
			print plot.cuts
