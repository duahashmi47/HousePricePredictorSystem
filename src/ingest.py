import os
import zipfile
import pandas as pd
from abc import ABC, abstractmethod 

#Define Abstract Class It's a factory interface
class DataIngester(ABC):
    @abstractmethod
    def ingest(self, file_path: str):
        """Abstract method to ingest data from the given file path."""
        pass

#Concrete Class for zip files
class ZipDataIngester(DataIngester):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extract a .zip file and return its contents into a DataFrame."""
        #ensure its a zip file
        if not file_path.endswith(".zip"):
            raise ValueError("Provided file is not a .zip archive.")
        #extract zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")
        #find the extracted file (assuming ther is only one file)
        extracted_files = os.listdir("extracted_data")
        #check if there is one or multiple files or none at all
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.") 
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the extracted data.")
        #read the csv file into a dataframe
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        return df
    
#factory implementation to create DataIngestors
class DataIngestionFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngester:
        """Returns the appropriate DataIngester based on the file type."""
        if file_extension == ".zip":
            return ZipDataIngester()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
if __name__ == "__main__":
    file_path = "D:/Dua's Projects/end-to-end-price-predictor-system/data/archive.zip"
    file_extension = os.path.splitext(file_path)[1]
    data_ingester = DataIngestionFactory.get_data_ingestor(file_extension)
    df = data_ingester.ingest(file_path)
    print(df.head())
    pass



