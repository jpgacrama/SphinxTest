.. _DiagnosticDataBudget:

DiagnosticDataBudget
=================================================================================================================================

``DiagnosticDataBudget``
*********************************************************************************************************************************

.. CSV-table::
   :widths: 7, 40
   :stub-columns: 1

    "**Status:**", "Approved"
    "**Features Ref.:**", "N/A"
    "**Changes Ref.:**", "CNI-12345, CNI-12346"

Details:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System shall have a default File Size limit inside the *ROM/* folder. Its purpose is to limit the Total size of :term:`technical logs <Technical Log>`

Note that System :term:`Technical Log` files can be stored as separate files in the Solid State Disk (SSD).
These are stored in the Diagnostic Data Directory .

    .. CSV-table::
        :stub-columns: 1

        "Unit", "MB"
        "Default Value", " - 10 for *Old HW*
         - 200 for *New HW*"
        "Minimum Value", "0"
        "Maximum Value", " - 10 for *Old HW*
         - 200 for *New HW*"
        "Step Value", "1"