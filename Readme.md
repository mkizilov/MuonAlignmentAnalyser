# Description
This is set of tools for visualising CMS Muon Alignment of CSC, GEM and DT chambers.
It is designed to be used with [https://swan.web.cern.ch/swan/](CEWN SWAN) but you can run it locally if you have needed libraries.
It can parse 
local geometry from xml files obtained by converting global geometry .db file with [https://github.com/cms-sw/cmssw/blob/f6e0fc429ceb8c78f0f0391bcc915e696065122d/Alignment/MuonAlignment/test/muonGeometryDBConverter_cfg.py](CMSSW .db to .xml converter)
TBMA iteration shifts from TBMA report.py files
CSC layer shifts from .csv tables from [https://github.com/mkizilov/CSCLayerAlignment](CSC Layer Alignment)
Root files from CSC layer al. and plot them.
See example.