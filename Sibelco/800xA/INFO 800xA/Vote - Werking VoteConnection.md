Dit diagramma toont de aansturing van een motor. Een activatie van MotorUniM.PriorityCmd0Config geeft altijd een alarm, ook als de motor niet draait.

![gnaIInReaIM IN_TEST Nane Real 10 ParEr Vote BrancM...](../../../../../../../assets/images/Exported%20image%2020250721204259-0.png)  

# SignalInRealM

|   |   |   |   |
|---|---|---|---|
|VoteOut|VoteConnection|out|NODE Output to vote objects|
|EnableLatchQuality|bool|in|Enables latch of bad quality that may be reset by InteractionPar.ResetLatchQuality|

# Vote1oo1Q

Voor een enkel signaal Vote1oo1Q gebruiken.

|   |   |   |   |
|---|---|---|---|
|In|VoteConnection|in|IN NODE Input  <br>Afkomstig van SignalInRealM.VoteOut|
|VoteOut|VoteConnection|out|OUT(IN) for cascade connection of vote objects|
|InLevelConfig|dint|in|IN Specification of Level included in voting (-3=LLL, -2=LL, -1=L, 0=DiffN, 1=H, 2=HH, 3=HHH (Obj dep.), else (0 if Bool else 1) + ParError)  <br>Welk alarm-niveau moet worden genomen|
|LatchEnable|bool|in|IN Enables latch on output|
|OutCommandNumber|dint|in|IN Command number to be set on Out. Range 1-32, else 1 +ParError.￼Welk commando-nummer is dit signaal van 1 tot 32|
    
# MotorUniM

|   |   |   |   |
|---|---|---|---|
|VotedCmd|VotedConnection|in|IN NODE Input from voting logic|
|PriorityCmdMan1Config|dword|in|IN Specify which Voted Command number(s) to set PriorityCmdMan1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|
|PriorityCmdMan0Config|dword|in|IN Specify which Voted Command number(s) to set PriorityCmdMan0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|
|PriorityCmd1Config|dword|in|IN Specify which Voted Command number(s) to set PriorityCmd1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|
|PriorityCmd0Config|dword|in|IN Specify which Voted Command number(s) to set PriorityCmd0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|
|ILock1Config|dword|in|IN Specify which Voted Command number(s) to set ILock1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|
|ILock0Config|dword|in|IN Specify which Voted Command number(s) to set ILock0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)|