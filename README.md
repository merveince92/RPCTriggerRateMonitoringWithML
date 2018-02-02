# DTTriggerRateMonitoringWithML
Monitoring the DT trigger rates using ML/DL techniques

In order to extract the instantaneous luminosity, please, use the brilcalc tool described here:

https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html

and the following command to have instantaneous luminosity vs. lumisections:

brilcalc lumi --byls -u hz/ub -r 306777 -o lumi.csv --output-style csv
