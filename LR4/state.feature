Feature: State switching
    realization of switching different states of the computer

    Scenario: On the computer
        Given Computer is Off

        When Switching on

        Then State should be On

    Scenario: Suspend the computer
        Given Computer is On

        When Switching Suspend

        Then State should be Suspend

    Scenario: Hibirnate the computer
        Given Computer is Suspended

        When Switching Hibirnate

        Then State should be Suspend