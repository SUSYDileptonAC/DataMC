#DATA_TREES=../../../sw532v0458/processedTrees/sw532v0460.processed.MergedData.root
TREES=/home/jan/Trees/sw538v0475
TREES_2011=/home/jan/Trees/2011MC
AN_PATH = ../DileptonAN
AN_TABLES=$(AN_PATH)/tables
AN_PLOTS=$(AN_PATH)/plots

PAS_PATH = rwth:~/PAS2/notes/SUS-12-019/trunk/plots


PlotTool = ./Plot.py
TableTool = ./makeDataMCTables.py
Region = Region
Region2 = Region2
newSelection = newSelection

#~ Plot_REGIONS = Region SignalHighMET SignalLowMET bTagControl Zpeak DrellYan Control




all: AN PAS



copyAN:
	#~ scp fig/DataMC/SignalHighMET* $(AN_PLOTS)
	scp fig/DataMC/Signal* $(AN_PLOTS)	
	scp fig/DataMC/ttBarDilepton* $(AN_PLOTS)
	scp fig/DataMC/Inclusive* $(AN_PLOTS)
	#~ scp fig/CompareTTbar/SignalHighMET_MET* $(AN_PLOTS)
	#~ scp fig/CompareTTbar/SignalLowMET_MET* $(AN_PLOTS)
	scp tab/* $(AN_TABLES)

copyTalk:
	scp fig/mll_Datadriven_SignalHighMET_*.pdf  fig/mll_Datadriven_SignalLowMET_*.pdf $(TALK_PATH)/fig
	scp tab/table_region_SignalHighMET*.tex $(TALK_PATH)/tab
 

copyPASPlots:
	scp fig/DataMC/SignalHighMET* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/
	scp fig/DataMC/SignalLowMET* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/
	scp fig/DataMC/ttBarDilepton* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/
	scp fig/DataMC/Inclusive* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/
	scp fig/CompareTTbar/SignalHighMET_MET* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/
	scp fig/CompareTTbar/SignalLowMET_MET* rwth:~/PAS2/notes/SUS-12-019/trunk/plots/moreDataMC/

copyPASTables:
	scp tab/table_DataMC_Signal.tex tab/table_DataMC_Inclusive.tex tab/table_DataMC_ttBarDilepton.tex rwth:~/PAS2/notes/SUS-12-019/trunk/

PASTables:
	$(TableTool) Inclusive
	$(TableTool) Signal
	$(TableTool) ttBarDilepton

DataMC: 
	$(PlotTool) $(TREES) DataMC  $(Region)  
DataMC2011: 
	$(PlotTool) $(TREES_2011) DataMC2011 $(Region) 
DataMC201153X: 
	$(PlotTool) $(TREES_2011)  DataMC201153X $(Region)
CompareReco2011: 
	$(PlotTool) $(TREES_2011) CompareReco2011 $(Region)  	 
CompareReco2011SFvsOF: 
	$(PlotTool) $(TREES_2011) CompareReco2011SFvsOF $(Region)  	 
CompareTTbar: 
	$(PlotTool) $(TREES) CompareTTbar $(Region)  
SFvsOF: 
	$(PlotTool) $(TREES) SFvsOF $(Region)  
SFvsOF2011: 
	$(PlotTool) $(TREES_2011) SFvsOF2011 $(Region)  
SFvsOFFlavourSeperated: 
	$(PlotTool) $(TREES) SFvsOFFlavourSeperated $(Region) 
plotRares: 
	$(PlotTool) $(TREES) plotRares $(Region) 
overlay: 
	$(PlotTool) $(TREES) overlay $(Region) $(Region2) $(newSelection)
	
AN: 
	$(PlotTool) $(TREES) notNeeded AN
PAS: 
	$(PlotTool) $(TREES) notNeeded PAS

help: 
	cat help.txt
	 
