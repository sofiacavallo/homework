Sub Ticker()

    'Establish the Variables
    Dim Ticker As String
    
    Dim TotalStockVolume As LongLong
    TotalStockVolume = 0
    
    'Establish the Summary Table
    Dim TickerHeader As String
    TickerHeader = "Ticker"
    Cells(1, 9).Value = TickerHeader
    
    Dim TotalStockVolumeHeader As String
    TotalStockVolumeHeader = "Total Stock Volume"
    Cells(1, 10).Value = TotalStockVolumeHeader
    
    Dim SummaryTableRow As Integer
    SummaryTableRow = 2
    
    'Establish Last Row variable (no need to declare it)
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    'Loop through all Tickers, through the last row in worksheet
    For i = 2 To lastRow
             
        'Check if we are still within the same Ticker name, if not...
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        
        'Set the Ticker name
        Ticker = Cells(i, 1).Value
        
        'Add to Ticker total
        TotalStockVolume = TotalStockVolume + Cells(i, 7).Value
        
        'Print the Ticker name in the Summary Table, in cell I2
        Range("I" & SummaryTableRow).Value = Ticker
        
        'Print the Total Stock Volume in the Summary Table, in cell J2
        Range("J" & SummaryTableRow).Value = TotalStockVolume
        
        'Add one to the summary table row (go to the next row)
        SummaryTableRow = SummaryTableRow + 1
        
        'Reset the Total Stock Volume
        TotalStockVolume = 0
             
    Else
        'Add the Total Stock Volume
        TotalStockVolume = TotalStockVolume + Cells(i, 7).Value
        
        End If
        
    Next i
    
End Sub
   
