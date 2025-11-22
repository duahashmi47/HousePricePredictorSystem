from abc import ABC, abstractmethod
import pandas as pd

# Abstract Base Class for Data Inspection Strategies

# This class defines a common interface for data inspection strategies.
# Subclasses must implement the inspect method.

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass

# Concrete Strategy for Data Types Inspection
# --------------------------------------------
# This strategy inspects the data types of each column and counts non-null values.

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspect and print the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())

# Concrete Strategy for Summary Statistics Inspection
# --------------------------------------------
# This strategy inspects the summary statistics of each column.

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspect and print the summary statistics of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))

#Context Class that uses a DataInspectionStrategy
#------------------------------------------------
# This class allows you to switch between different data inspection strategies.

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initialize the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self.strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Set a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self.strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Execute the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self.strategy.inspect(df)

if __name__ == "__main__":
    # Example usage of the DataInspector with different strategies.

    # Load the data
    #df = pd.read_csv('D:\\Dua\'s Projects\\end-to-end-price-predictor-system\\extracted_data\\AmesHousing.csv')

    # Initialize the Data Inspector with a specific strategy
    #inspector = DataInspector(DataTypesInspectionStrategy())
    #inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    #inspector.execute_inspection(df)
    pass
