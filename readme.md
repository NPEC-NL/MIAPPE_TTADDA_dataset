
## About
Official implementation of [TTADDA-UAV: RGB and multispectral high-resolution UAV monitoring of Potato fields across Japan and the Netherlands](https://doi.org/10.1016/j.dib.2025.112004) dataset. 

To have a look at our collection:
https://data.4tu.nl/collections/936b5772-09fc-4856-983d-1f9cc2f38d15


## Installation
This software is tested on Python 3.11. To install the dependencies, run:
```
pip install omegaconf
pip install pandas
pip install geopandas
pip install openpyxl
```

## Downloading dataset Usage
The data can be downloaded using the main.py, we only download the MIAPPE and the TTADDA_NARO_2021 automatically. Downloading all datsets would be time consuming. Feel free to uncomment the other datasets in the config file. 
**IMPORTANT automatically downloading is currently disabled. This will be enabled after acceptance data in brief paper. The data can only be downloaded with private links. To run main.py download the "MIAPPE_Minimal_Spreadsheet_Template_TTADDAv4.xlsx" and copy to current folder**

```
python3 main.py
```
For more examples have a look at:
```
example_notebook.ipynb
```

Settings are described in the [config.yaml](config.yaml) file.


## Citation
```
@article{VANMARREWIJK2025112004,
title = {TTADDA-UAV: A multi-season RGB and multispectral UAV dataset of potato fields collected in Japan and the Netherlands},
journal = {Data in Brief},
volume = {62},
pages = {112004},
year = {2025},
issn = {2352-3409},
doi = {https://doi.org/10.1016/j.dib.2025.112004},
url = {https://www.sciencedirect.com/science/article/pii/S2352340925007280},
author = {Bart. M. {van Marrewijk} and Stephen Njehia Njane and Shogo Tsuda and Marcel {van Culemborg} and Gerrit Polder and Kenji Katayama and Tim {van Daalen} and Rick van de Zedde},
keywords = {Phenotyping, Yield estimation, Agriculture, Orthomosaic},
}
```

## Funding
This research was funded by the TTADDA[https://www.ttadda.com/]. A public private partnership between companies in the Netherlands and Japan 