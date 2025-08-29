
## About
Official implementation of [TTADDA-UAV](https://data.4tu.nl/my/collections/936b5772-09fc-4856-983d-1f9cc2f38d15/edit) dataset. **Currently in review**


The dataset is related to the paper:

**TODO add link to paper after acceptance**
[TTADDA-UAV: RGB and multispectral high-resolution UAV monitoring of Potato fields across Japan and the Netherlands
]()

## Installation
This software is tested on Python 3.11. To install the dependencies, run:
```
pip install omegaconf
pip install pandas
pip install geopandas
pip install openpyxl
```

## Usage
Make sure to extract and download the dataset, this will be done automatically if path can not be found:

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
**TODO after publication**

## Funding
This research was funded by the TTADDA[https://www.ttadda.com/]. A public private partnership between companies in the Netherlands and Japan 