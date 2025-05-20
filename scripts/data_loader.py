import pandas as pd
from pathlib import Path
import geopandas as gpd
import natsort


class loadMIAPPE():

    def __init__(self, excel_path=Path("MIAPPE_Minimal_Spreadsheet_Template_TTADDAv4.xlsx"), data_folder=Path("/media/agro/PhDBart2/")):
        self.excel_path = excel_path
        self.data_folder = data_folder

        self.excel_file = pd.read_excel(excel_path, sheet_name=None)

    def get_data_id(self, temp_dataId, temp_variableId, obsUnitId=None, vis=False):
        # Get the file name for the given dataId
        file_name = self.data_folder / self.excel_file["Data file_2"][self.excel_file["Data file_2"]["dataId"] == temp_dataId]["dataFileLink"].values[0]
        # Ensure temp_variableId is a list
        if isinstance(temp_variableId, list):
            columns = ["collectionDate", "obsUnitId"] + temp_variableId
        else:
            columns = ["collectionDate", "obsUnitId", temp_variableId]

        
        if file_name.name.endswith('.csv'):
            # Read the CSV and select the columns
            df_temp = pd.read_csv(file_name)[columns]
            if obsUnitId is not None:
                df_temp = df_temp[df_temp["obsUnitId"]==obsUnitId]
            if vis:
                plot_variable(df_temp, temp_variableId)
        elif file_name.name.endswith('.shp'):
            if file_name.name.endswith('.shp'):
                gdf = gpd.read_file(file_name)
                if vis:
                    gdf.plot()
                return gdf
        elif file_name.name.endswith('.tif'):
            collectionDate = file_name.parent.stem
            return [collectionDate, file_name]
        else:
            raise ValueError(f"Unsupported file type: {file_name}")

        return df_temp

    def get_observed_variables(self, temp_obsUnitId, temp_variableId, vis=False):
        if isinstance(temp_variableId, list):
            rows = self.excel_file["Observed Variable_2"][
                (self.excel_file["Observed Variable_2"]["obsUnitId"] == temp_obsUnitId) &
                (self.excel_file["Observed Variable_2"]["variableId"].isin(temp_variableId))
            ]
        else:
            rows = self.excel_file["Observed Variable_2"][
                (self.excel_file["Observed Variable_2"]["obsUnitId"] == temp_obsUnitId) &
                (self.excel_file["Observed Variable_2"]["variableId"] == temp_variableId)
            ]
        
        result = []
        for row in rows.itertuples(index=False):
            df_temp = self.get_data_id(temp_dataId=row.dataId, temp_variableId=row.variableId, obsUnitId=temp_obsUnitId, vis=vis)
            result.append(df_temp)
        return result
    


    def get_observation_unit_info(self, temp_studyId=None, temp_obsUnitId=None, verbose=True):
        if temp_studyId is not None:
            df_temp = self.excel_file["Observation Unit_2"][
                (self.excel_file["Observation Unit_2"]["studyId"] == temp_studyId)]
        elif temp_obsUnitId is not None:
            df_temp = self.excel_file["Observation Unit_2"][
                (self.excel_file["Observation Unit_2"]["obsUnitId"] == temp_obsUnitId)]
        else:
            raise ValueError("Either temp_studyId or temp_obsUnitId must be provided.")
        
        ## if df_temp is empty
        if df_temp.empty:
            print("No data is available for the given study or observation unit.")
        if verbose:
            print("Rows:")
            print(df_temp.to_string(index=False))

        return df_temp
    
    def get_sensor_info(self, sensorId=None):
        if sensorId is None:
            return self.excel_file["Sensor"]
        else:
            return self.excel_file["Sensor"][self.excel_file["Sensor"]["sensorId"]==sensorId]
            
        
def plot_variable(df_temp, x_axis="collectionDate", y_axis=None):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(df_temp[x_axis], df_temp[y_axis], marker='o')
    plt.grid()
    plt.xlabel("Collection Date")
    plt.ylabel(y_axis)
    plt.title(f"{y_axis} over {x_axis}")
    plt.xticks(rotation=45)
    plt.show()

if __name__=="__main__":
    obj = loadMIAPPE()
    print(obj.get_sensor_info())
    print(obj.get_sensor_info("AmeDAS_T1"))


## get info of all observation units given studyId
# temp_studyId = "TTADDA_NARO_2023"
# obj.get_observed_variables(temp_studyId=temp_studyId)

## get info of all observation unit given ObsUnitId
# temp_obsUnitId = "TTADDA_NARO_2023_F1"
# obj.get_observed_variables(temp_obsUnitId=temp_obsUnitId)
# temp_obsUnitId = "TTADDA_NARO_2023_F1P1"
# obj.get_observed_variables(temp_obsUnitId=temp_obsUnitId)


## example if you want to get the air temperature of field_1
# temp_obsUnitId = "TTADDA_NARO_2023_F1"
# temp_variableId = ["air_temp_avg"]
# get_observed_variables(temp_obsUnitId, temp_variableId)

## get ground coverage of P164
# temp_obsUnitId = "TTADDA_WUR_2022_F1P164"
# temp_variableId = ["ground_coverage"]
# get_observed_variables(temp_obsUnitId, temp_variableId)


## get location of orthomosaic coverage of P164
# temp_obsUnitId = "TTADDA_WUR_2023_F1"
# temp_variableId = ["rgb_orthomosaic_camera1"]
# file_names = obj.get_observed_variables(temp_obsUnitId, temp_variableId)
# for item in file_names:
#     if isinstance(item, list) and len(item) == 2:
#         date, path = item
#         print(f"Date: {date} | File: {path}")
#     else:
#         print(item)

# ## get location of plots
# temp_obsUnitId = "TTADDA_WUR_2023_F1"
# temp_variableId = ["plot_location"]
# plots = obj.get_observed_variables(temp_obsUnitId, temp_variableId)[0]
# print(plots)

# ## get yield
# temp_obsUnitId = "TTADDA_WUR_2023_F1P1"
# temp_variableId = ["tubwght_total_kgm-2"]
# weight = obj.get_observed_variables(temp_obsUnitId, temp_variableId)[0]
# print(weight)

# print("finished")


