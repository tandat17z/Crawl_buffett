import pandas as pd
import numpy as np
import time, os
from src.get_volume import get_volume
from src.get_table import get_table
from src.dividend import GetDividend
class ReadPdf():
    def __init__(
        self,
        path_all_com="docs/List_company_23052023 - Listing.csv",
        path_save="",
        ):
        self.path_all_com = path_all_com
        self.path_save = path_save

    def get_all_com(self, reverse: bool = False):
        """
        Get all company in japan stock
        Parameters
        ----------
        reverse : bool
            reverse list company
        Returns
        -------
        None
        """
        lst_com = pd.read_csv(self.path_all_com)
        if "check" not in lst_com.columns:
            lst_com["check"] = np.nan
        if reverse:
            lst_com = lst_com[::-1]
        for i in lst_com.index:
            id_company = lst_com["Symbol"][i]
            check = lst_com["check"][i]
            if check == "Done":
                get_volume(id_company, self.path_save, save_file=True)
                get_table(id_company, self.path_save, save_file=True)
                dividendClass = GetDividend(path_save=self.path_save)
                dividendClass.get_dividend(id_company, save_file=True)
                
            