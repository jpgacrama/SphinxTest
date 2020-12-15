.. _SampleUseCaseAnchor:

UC: Sample Use Case Name
=================================================================================================================================

``SampleUseCaseAnchor``
*********************************************************************************************************************************

.. csv-table::
   :widths: 7, 40

   "Status", "Approved"
   "Features Ref.", "FeatureNum"
   "Changes Ref.", "BugNumber"
   "HW unit", "HW1, HW2"

Introduction:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place your introduction here.

1. Sample intro 1

2. Sample intro 2.

Purpose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Place the purpose of this Use Case here

Actors:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Actor 1
    - Actor 2

Triggers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Place the trigger to this Use case here

Pre-conditions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1.  Place the list of Preconditions here

Description:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. This contains the text-based explanation of the UML diagram below. *Keep this to a minimum though*. Diagrams are still easier to understand.


.. uml::

    @startuml

        title \nMain Sequence Diagram\n

        actor "Actor 1" as Actor1
        actor "Actor 2" as Actor2
        participant "Domain1" as Domain1
        participant "Domain2" as Domain2

        Actor1  -> Domain1: //<<Commissioning Information for//\n//New Feature is sent to Domain1>>//

        opt Actor 2
            Actor2  -> Domain1: //<<Commissioning Information for//\n//New Feature is sent to Domain1>>//
        end

        note over Domain1
            Domain1 assumes that validation
            is already done by the
            Actor 1.
        end note

        Domain1 -> Domain1: License-related validation is done

        alt License-related errors are found
            Domain1 -> Actor1: Operator is notified on\nthe appropriate License-related errors
            note over Actor1
                Use Case ends
            end note
        end

        note over Domain1 #DodgerBlue
            Information from Commissioning
            shows that it is time to gather files.
        end note

        ref over Domain1
            //See File Uploads// Sequence Diagram
        end ref

    @enduml

.. uml::

    @startuml
    title \nFile Uploads\n

    actor "Actor 1" as Actor1
    participant "Domain2" as Domain2

    box "Domain1" #LightBlue
        participant "Domain1" as Domain1
        participant "Domain2" as Domain2
    end box

    participant "System Component 2" as SysComp2

    note over Domain1 #DodgerBlue
        Information from Commissioning
        shows that it is time to gather files.
    end note

    loop For each active cell in Domain1
        Domain1 -> Domain2: //SOAP_ModifyParamReq: Domain2 Start Test Request//
        Domain2 -> Domain1: //SOAP_ParValueChangeInd: Domain2 Start Test Response (OK)//

        Domain2 -> Domain2: //Create File//
        Domain2 -> Domain1: TFTP_Data: //Send File//

        note over Domain2, Domain2
            File transfer among Domain2, Domain1, and Domain2 still follow the legacy TFTP way.
            Nothing has changed because of //FeatureID//.
        end note

        Domain1 -> Domain2: TFTP_Data: //Send file to Domain2//
        Domain2 -> SysComp2: HTTP PUT: //File transfer via HTTP//

        note over Domain2, SysComp2
            Some useful information which is applicable
            to //Domain 2// and //System Component 2//
        end note

        note over Domain2
            See //Another Requirement ID//
            for more information
        end note

        alt All files are transferred to System Component 2 successfully

            Domain1 -> Domain2: TFTP_Data: //Sends a summary file containing all the files it sent//
            Domain2 -> SysComp2: HTTP PUT: //Sends a summary file containing all the files it sent//
            SysComp2 -> Domain2: HTTP Status: 200 //File transfer successful//
            Domain2 -> Domain1: TFTP_ACK: //File transfer successful//

        else System Component 2 responds with Nack

            SysComp2 -> Domain2: HTTP Status: 503 Service unavailable //(i.e. File transfer via HTTP rejected)//
            Domain2 -> Domain1: TFTP_ACK: //File transfer via HTTP rejected//

            note over Domain1 #Aqua
                See Activity Diagram for
                handling Faulty Situation
            end note

            note over Domain1 #Aqua
                Domain1 assumes that all files will not be sent towards SysComp2 since SysComp2 has problems
            end note

            Domain1 -> Domain1: <font color=red> Request Rejected Alarm is raised.
            Domain1 -> Actor1: <font color=red> Notification message

            note over Actor1
                Use Case ends
            end note

        else File upload to SysComp2 Fails

            SysComp2 -> Domain2: //File transfer via HTTP failed.//
            Domain2 -> Domain1: TFTP_ACK: //File transfer via HTTP failed//

            note over Domain1 #Aqua
                Domain1 stores the filename(s) which failed to upload.
            end note

            opt All files were sent / were attempted to be sent

            Domain1 -> Domain2: //Sends a summary file//
            Domain2 -> SysComp2: HTTP PUT: //Sends a summary file//

            note over Domain1, SysComp2
                Summary file contains all the filenames that were successfully sent, and those which were not
            end note

            SysComp2 -> Domain2: HTTP Status: 200 //File transfer successful//
            Domain2 -> Domain1: TFTP_ACK: //File transfer successful//

            Domain1 -> Domain1: <font color=red> File Upload Failed alarm is raised.
                Domain1 -> Actor1: <font color=red> Notification message
            end

            note over Actor1
                Use Case ends
            end note

        else There is no connection to System Component 2

            Domain1 -> Domain1: **Internal Timeout reached**

            note over Domain1 #Aqua
                See Activity Diagram for
                handling Faulty Situation
            end note

            Domain1 -> Domain1: <font color=red> No connection to System Component 2 is raised.
            Domain1 -> Actor1: <font color=red> Notification

            note over Actor1
                Use Case ends
            end note

        end

        end

    @enduml

.. uml::

    @startuml

        title \nHandling Faulty Situation in Domain1.\n

        start

        while (Faulty situation **DID NOT** happen for the **THIRD** time.\nSee note for Exceptions.) is (True)

            note left
                When the scan interval is in the unit of **weeks or months**,
                Fault should be raised **IMMEDIATELY**
            end note

            :Domain1 discards the results of the previous Scan, if any.;
            :Domain1 waits for the next Scan Interval.;

        endwhile (False)

        #DodgerBlue:Appropriate Fault is raised.
        See either //Main Sequence Diagram//.;

        stop

    @enduml

Post-conditions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    System Component 2 receives the Data from the Domain1. Information about the Domain1, and the Date Executed should be present inside the file.

Exceptions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **ALT CASE: License Related Errors**

        For Step 1, see the possible numbered scenarios below, and their corresponding Post-conditions:

        1. The needed license to run this feature is not loaded into the Domain1.
        2. The needed license already expired.
        3. Generic ID-related validation fails.

        **Post Condition:**

        1. The Operator should be notified of the needed license to run this functionality.
        Domain1 raises License Missing alarm. Use Case ends.

Notes and Issues:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Add notes and issues here

References:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Add references here