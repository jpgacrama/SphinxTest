.. _Testability_StoredFilesShouldHavePriorityTags:

System Shall Delete Technical Log Files according to their Priority Tag and Time Stamp
=================================================================================================================================

``WSystem20_Testability_StoredFilesShouldHavePriorityTags``
*********************************************************************************************************************************

.. csv-table::
   :widths: 7, 40

   "Status", "Approved"
   "Features Ref.", "N/A"
   "Changes Ref.", "CNI-1234"
   "HW unit", "HW1, HW2"

Description:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System should know the Priority Tag of each file since it has limited space according to :ref:`DiagnosticDataBudget <DiagnosticDataBudget>`
Each file should have a Priority Tag, and Time Stamp assigned to it.

If two or more files have the same Priority Tag, then the file with the earlier Time Stamp has *lower* priority than the one which was created later.
If there is insufficient space to store new Technical Logs, then the files with lower priority are deleted.

Related Entity Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Create link to another Use case or Requirement <https://www.sphinx-doc.org/en/1.7/markup/inline.html#cross-referencing-arbitrary-locations>`_

Related System Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None
