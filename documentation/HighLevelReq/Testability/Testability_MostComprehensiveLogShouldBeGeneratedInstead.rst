.. _Testability_MostComprehensiveLogShouldBeGeneratedInstead:

Most Comprehensive Log Should Be Generated Instead
=================================================================================================================================

``Testability_MostComprehensiveLogShouldBeGeneratedInstead``
*********************************************************************************************************************************

.. csv-table::
   :widths: 7, 40

   "Status", "Approved"
   "Features Ref.", "N/A"
   "Changes Ref.", "CNI-12345"
   "HW unit", "HW1, HW2"

Description:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Among concurrent :term:`Technical Log` requests, System shall generate only the :term:`technical logs <Technical Log>` that are not a subset of other requests.

.. uml::

    @startuml
    title \nMost Comprehensive Log is Generated Instead\n

    start

    while (System has Log requests in queue) is (Yes)
        :System gets the first item in queue;

            if (Current log request in queue\nis a subset of any of the succeeding requests) then (Yes)
                :Drop the current request;
            else (No)
                :System processes the request;
            endif

    endwhile (No)
    stop
    @enduml

Related Entity Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Create link to another Use case or Requirement <https://www.sphinx-doc.org/en/1.7/markup/inline.html#cross-referencing-arbitrary-locations>`_

Related System Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None
