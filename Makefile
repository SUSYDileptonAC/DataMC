#DATA_TREES=../../../sw532v0458/processedTrees/sw532v0460.processed.MergedData.root


AN_PATH = ..//DileptonAN
AN_TABLES=$(AN_PATH)/tables
AN_PLOTS=$(AN_PATH)/plots

PAS_PATH = rwth:~/PAS2/notes/SUS-12-019/trunk/plots


PlotTool = ./Plot.py
TableTool = ./makeDataMCTables.py
region = region
plot = plot
runRange = runRange
signals = signals


DataMC: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d -a 
DataMCSignal: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d -a -c $(signals) 
DataMCNoRatio: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d  
DataMCSignalNoRatio: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d  -c $(signals) 
MC: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange)
MCSignal: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -c $(signals) 

	 
signalCentral:
	$(PlotTool) -p mllPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p metPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p htPlot  -s SignalCentral -r Full2012 -d -a
	$(PlotTool) -p eta1Plot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p eta2Plot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p ptElePlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p ptMuPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p trailingPtPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p leadingPtPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p nJetsPlot  -s SignalCentral -r Full2012 -d -a 
	$(PlotTool) -p nBJetsPlot  -s SignalCentral -r Full2012 -d -a 
	
signalForward:
	$(PlotTool) -p mllPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p metPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p htPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p eta1Plot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p eta2Plot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p ptElePlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p ptMuPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p trailingPtPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p leadingPtPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p nJetsPlot  -s SignalForward -r Full2012 -d -a 
	$(PlotTool) -p nBJetsPlot  -s SignalForward -r Full2012 -d -a 
