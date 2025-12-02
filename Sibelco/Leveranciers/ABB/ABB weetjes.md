---
title: ABB weetjes
updated: [[2010-11-19]]T10:05:40.0000000+01:00
created: [[2010-11-18]]T10:56:18.0000000+01:00
---

ABB weetjes
donderdag 18 november 2010

- # ABB weetjes
- ## Autolock aanzetten
  Autolock is configured per user. You can view and configure the settings for
  each user by selecting the user from the list and then click the View Autolock
  button. See IndustrialIT 800xA, Engineering, Graphics (3BSE030335Rxxxx)
  instruction for more information about autolock.
  User Structure -
  ![image1](image1-535.png)
- #
- ## Sequentie vars (SFC)
  Automatically Generated Variables
  For one sequence, the following variables are automatically generated when the program is compiled
  | **Name**                    | **Type** | **Description**                                                                                                               |    |
  |-----------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------|-----|
  | *SequenceName.Reset*        | bool     | While True, the sequence is reset to the initial step. The system resets this variable automatically to False after one scan. |    |
  | SequenceName.Hold           | bool     | While True, all transitions in the sequence are blocked. The above Reset function is NOT affected                             |    |
  | SequenceName.DisableActions | Bool     | While True, all actions associated with the steps of the sequence are disabled, that is, the will not execute                 |    |
  | StepName.X                  | Bool     | This variable is True while the step is active.                                                                               |    |