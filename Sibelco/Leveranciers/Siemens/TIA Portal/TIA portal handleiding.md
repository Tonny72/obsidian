---
date created: 2017-03-08
tags:
  - application
date modified: 2025-08-30
---

- # MultiUser server
  https://be-des-aps-022:3737
  
  <https://support.industry.siemens.com/cs/media/106656707_TIA_Portal_Tutorial_Center_web/start.htm#/en/default/index>
  [TIA Portal Tutorial \#01: Network- and Device view](https://www.youtube.com/watch?v=Qew1xpfEcms)
  
  ![image1](image1-566.png)
- # DPRD_DAT en DPWR_DAT
  [Siemens PLC Function Block Training: DPRD_DAT and DPWR_DAT (youtube.com)](https://www.youtube.com/watch?v=yrGkVKPWJkU)
  Wordt gebruikt om consistent (dus alle data 1 in keer) data te versturen naar en van profibus.
- ### Parameters
  LADDR: Hardware ID of the profibus device. Kan je terugvinden bij de systeemconstanten.
- # Geheugen gebruik van van een plc.
  ![[assets/images/Pasted image 20240719152742\.jpg]]
- # Download without reinitialization
  Downloading without reinitialisation
  In order to change user programs that already run in a controller, S7-1200 (firmware V4.0) and S7-1500 controllers offer the option to expand the interfaces of optimized function or data blocks during operation. You can load the changed blocks without setting the controller to STOP and without influencing the actual values of already loaded tags.
  Figure 3-14: Load without reinitialization
  ![[assets/images/Pasted image 20240719153649\.jpg]]
- ## Advantages
	- Reloading of newly defined tags without interrupting the running process. The controller stays in “RUN” mode.
- ## Properties
- Downloading without reinitiatialization is only possible for optimized blocks.
- The newly defined tags are initialized. The existing tags keep their current value.
- A block with reserve requires more memory space in the controller.
- The memory reserve depends on the work memory of the controller; however, it is max. 2 MB.
- It is assumed that a memory reserve has been defined for block.
- By default, the memory reserve is set to 100 byte.
- The memory reserve is defined individually for every block.
- The blocks can be variably expanded.
- ## Recommendation
- Define a memory reserve for blocks that are to be expanded during commissioning (e.g. test blocks). The commissioning process is not disturbed by a download since the actual values of the existing tags remain.
- ## Example: Stetting memory reserve on the block
  The following table describes how you can set the memory reserve for the downloading without reinitializing.
  Table 3-3: Setting memory reserve
  ![[assets/images/Pasted image 20240719154208\.jpg]]
  ![[assets/images/Pasted image 20240719154226\.jpg]]
  **Note** 
  
  ```
  You can also set a default value for the size of the memory reserve for new
  blocks in the TIA portal.
  In the menu bar, navigate to "Options – Settings" and then to "PLC programming – General – Download without reinitialization".
  ```
- ## Example: Downloading without reinitialisation
  The following example displays how to download without reinitialization.
  Table 3-4 Load without reinitialization
  ![[assets/images/Pasted image 20240719154808\.jpg]]
  ![[assets/images/Pasted image 20240719154836\.jpg]]