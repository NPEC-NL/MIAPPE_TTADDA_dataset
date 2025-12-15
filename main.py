################################################################
# Author     : Bart van Marrewijk                              #
# Contact    : bart.vanmarrewijk@wur.nl                        #
# Date       : 10-07-2024                                      #
# Description: Code related to the TTADDA-UAV dataset           #
################################################################

# Usage: see if__name__



from tqdm import tqdm
import requests
from zipfile import ZipFile
import config



class TTADDA_UAV():
    """

    Description:
    loading and visualidation TTADDA-UAV dataset: DOI 

    https://github.com/NPEC-NL/MIAPPE_TTADDA_dataset/tree/main

    Author     : Bart M. van Marrewijk
    Contact    : bart.vanmarrewijk@wur.nl
    Date       : 20-03-2025

    Example usage:
    """

    def __init__(self, **kwargs):
        config_data = config.Config("config.yaml")

        # self._set_attributes(config_data)
        self.__dict__.update(config_data.__dict__)

        # If the data folder can not be found then ask to download the data
        if not self.project_dir.exists():
            self.project_dir.mkdir()

        print("Warning currently automatically downloading the dataset does not work, because data is not yet published...")
        print(f"download files manually and unzip them in {self.project_dir}")

        # for key, value in self.url_list.items():
        #     print(f"{key}: {value}")
        # return
        self.check_data()

    def check_data(self):
        for key, item in self.url_list.items():
            self.check_url(key, item)


    def check_url(self, sub_folder, url):
        user_input = f"Data not found {self.project_dir / sub_folder}"
        print(user_input)
        if self.__download(sub_folder, url):
            self.__unzip(sub_folder)

        print("Successfully loaded the WURTomato dataset")

    # # Download LastSTRAW data file in zip format
    def __download(self, sub_folder, url):
        """
        If the unzipped files exist do not download. If they do not
        exist then download the zip file
        """
        print(self.project_dir / sub_folder)
        if not (self.project_dir / sub_folder).is_dir():
            # if not self.project_dir.exists():
            #     self.project_dir.mkdir()

            self.downloadFile = f"{sub_folder}_download.zip"
            if (self.project_dir / self.downloadFile).is_file():
                print("Already downloaded but not unzipped")
                return True

            response = requests.get(str(url), stream=True)
            if response.status_code == 200:
                print(f"Downloading, this may take a while ({sub_folder} is {self.gb_dict[sub_folder]}GB)...")
                total_size = int(response.headers.get('content-length', 0))  # Get total size in bytes
                block_size = 8192  # Or whatever chunk size you want
                progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

                with open(self.project_dir / self.downloadFile, "wb") as file:
                    for chunk in response.iter_content(chunk_size=block_size):
                        if chunk:
                            file.write(chunk)
                            progress_bar.update(len(chunk))
                progress_bar.close()
                print("File downloaded successfully.")
                return True
            else:
                print(f"Failed to download file. Status code: {response.status_code}")
        else:
            print("File already download and extracted.")
            return False

    # Taken from https://www.geeksforgeeks.org/unzipping-files-in-python/
    def __unzip(self, sub_folder):
        """
        If data zip file has been download, extract all files
        and delete downloaded zip file
        """
        if (self.project_dir / self.downloadFile).is_file():
            if not (self.project_dir / sub_folder).is_dir():
                print(f"Extracting: {self.project_dir / self.downloadFile}")
                with ZipFile(str(self.project_dir / self.downloadFile), "r") as zObject:
                    file_list = zObject.namelist()
                    total_files = len(file_list)
                    progress_bar = tqdm(total=total_files, unit='file', desc="Extracting files")
                    for file in file_list:
                        zObject.extract(file, path=str(self.project_dir))
                        progress_bar.update(1)
                    progress_bar.close()

                new_zip_file = self.project_dir / (sub_folder + ".zip")
                print(f"Extracting: {new_zip_file}")
                with ZipFile(new_zip_file, "r") as zObject:
                    file_list = zObject.namelist()
                    total_files = len(file_list)
                    progress_bar = tqdm(total=total_files, unit='file', desc="Extracting files")
                    for file in file_list:
                        zObject.extract(file, path=str(self.project_dir / sub_folder))
                        progress_bar.update(1)
                    progress_bar.close()
                print(f"Deleting {new_zip_file}")
                # os.remove(str(new_zip_file))

if __name__ == "__main__":

    # Create an instance of WurTomatoData
    obj = TTADDA_UAV()
