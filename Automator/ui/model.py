
from PyQt5 import QtCore, QtGui

class FacebookAccountsModel(QtCore.QAbstractTableModel):
    """ Facebook accounts model"""
        
    def __init__(self, data, parent = None):
        super().__init__(parent=parent)
        self._df = data.loc[:,['Full name','Account status','group']]

        # for ind, header in enumerate(self._df.columns.values):
        #     self.setHeaderData(ind, QtCore.Qt.Horizontal,header)

    def rowCount(self, parent = None):
        return self._df.shape[0]

    def columnCount(self, parent = None):
        return self._df.shape[1]

    def data(self, index, role):
    

        # if(role == Qt.FontRole):
        #     return QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        
        # if(role == QtCore.Qt.TextAlignmentRole):
        #     return QtCore.Qt.AlignHCenter

        if(index.isValid()):
            if(role == QtCore.Qt.BackgroundColorRole):
                if(super().data(index, QtCore.Qt.DisplayRole) == 'Active'):
                    return QtGui.QColor(0,255,0,100)

                elif(super().data(index, QtCore.Qt.DisplayRole) == 'Inactive'):
                    return QtGui.QColor(255,50,0,100)

            if(role == QtCore.Qt.DisplayRole):
                return str(self._df.iloc[index.row(), index.column()])
            
        return None
        
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int):
        
        if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):
            return self._df.columns[section]

    
        if(orientation == QtCore.Qt.Vertical and role==QtCore.Qt.DisplayRole):
            return section + 1

        return None


class FacebookAccountsSortoModel(QtCore.QSortFilterProxyModel):
    """ Daily customers sorting model"""
    def __init__(self, source_model, parent = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._accounts_group_matcher = QtCore.QRegularExpression()
      
        # Set source model
        self.setSourceModel(source_model)
    
    def setAccountGroupFilter(self, pattern):
        """Set regex for customer name"""
        self._accounts_group_matcher.setPattern(pattern)

        self.invalidateFilter()

    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex):
        
        account_group_index = self.sourceModel().index(row_num, 2, source_parent)

        account_group = self.sourceModel().data(account_group_index, QtCore.Qt.DisplayRole)

        tests =  [
            self._accounts_group_matcher.match(account_group).hasMatch(),
        ]
        return (not False in tests)

