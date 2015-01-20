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
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d -r 
DataMCSignal: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d -r -c $(signals) 
DataMCNoRatio: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d  
DataMCSignalNoRatio: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -d  -c $(signals) 
MC: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange)
MCSignal: 
	$(PlotTool) -p $(plot)  -s $(region) -r $(runRange) -c $(signals) 

	 
signalCentral:
	$(PlotTool) -p mllPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p metPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p htPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p eta1Plot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p eta2Plot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p ptElePlot  -s SignalBarrel -r Full2012 -d -r -
	$(PlotTool) -p ptMuPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p trailingPtPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p leadingPtPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p nJetsPlot  -s SignalBarrel -r Full2012 -d -r 
	$(PlotTool) -p nBJetsPlot  -s SignalBarrel -r Full2012 -d -r 
	
signalForward:
	$(PlotTool) -p mllPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p metPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p htPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p eta1Plot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p eta2Plot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p ptElePlot  -s SignalForward -r Full2012 -d -r -
	$(PlotTool) -p ptMuPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p trailingPtPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p leadingPtPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p nJetsPlot  -s SignalForward -r Full2012 -d -r 
	$(PlotTool) -p nBJetsPlot  -s SignalForward -r Full2012 -d -r 
