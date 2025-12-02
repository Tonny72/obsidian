---
date created: 2014-03-14
modified: 2025-07-21
---
# Outlook

Default sending account in outlook 2013

<http://www.slipstick.com/outlook/outlook-2010/multiple-accounts-and-the-default-account/>

HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Outlook\Options\Mail
DWORD value: NewItemsUseDefaultSendingAccount
Value: 1

- # Maak een link naar een outlook message
- ## VBA script
  \#If VBA7 Then
  Private Declare PtrSafe Function GlobalUnlock Lib "kernel32" (ByVal hMem As LongPtr) As Long
  Private Declare PtrSafe Function GlobalLock Lib "kernel32" (ByVal hMem As LongPtr) As Long
  Private Declare PtrSafe Function GlobalAlloc Lib "kernel32" (ByVal wFlags As LongPtr, ByVal dwBytes As LongPtr) As Long
  Private Declare PtrSafe Function CloseClipboard Lib "User32" () As Long
  Private Declare PtrSafe Function OpenClipboard Lib "User32" (ByVal hwnd As LongPtr) As Long
  Private Declare PtrSafe Function EmptyClipboard Lib "User32" () As Long
  Private Declare PtrSafe Function lstrcpy Lib "kernel32" (ByVal lpString1 As Any, ByVal lpString2 As Any) As Long
  Private Declare PtrSafe Function SetClipboardData Lib "User32" (ByVal wFormat As LongPtr, ByVal hMem As LongPtr) As Long
  \#Else
  Private Declare Function GlobalUnlock Lib "kernel32" (ByVal hMem As Long) As Long
  Private Declare Function GlobalLock Lib "kernel32" (ByVal hMem As Long) As Long
  Private Declare Function GlobalAlloc Lib "kernel32" (ByVal wFlags As Long, ByVal dwBytes As Long) As Long
  Private Declare Function CloseClipboard Lib "User32" () As Long
  Private Declare Function OpenClipboard Lib "User32" (ByVal hwnd As Long) As Long
  Private Declare Function EmptyClipboard Lib "User32" () As Long
  Private Declare Function lstrcpy Lib "kernel32" (ByVal lpString1 As Any, ByVal lpString2 As Any) As Long
  Private Declare Function SetClipboardData Lib "User32" (ByVal wFormat As Long, ByVal hMem As Long) As Long
  \#End If
  
  Const GHND = &H42
  Const CF_TEXT = 1
  Const MAXSIZE = 4096
  
  Function ClipBoard_SetData(MyString As String)
  'PURPOSE: API function to copy text to clipboard
  'SOURCE: [www.msdn.microsoft.com/en-us/library/office/ff192913.aspx](http://www.msdn.microsoft.com/en-us/library/office/ff192913.aspx)
  
  Dim hGlobalMemory As Long, lpGlobalMemory As Long
  Dim hClipMemory As Long, X As Long
  
  'Allocate moveable global memory
  hGlobalMemory = GlobalAlloc(GHND, Len(MyString) + 1)
  
  'Lock the block to get a far pointer to this memory.
  lpGlobalMemory = GlobalLock(hGlobalMemory)
  
  'Copy the string to this global memory.
  lpGlobalMemory = lstrcpy(lpGlobalMemory, MyString)
  
  'Unlock the memory.
  If GlobalUnlock(hGlobalMemory) \<\> 0 Then
  MsgBox "Could not unlock memory location. Copy aborted."
  GoTo OutOfHere2
  End If
  
  'Open the Clipboard to copy data to.
  If OpenClipboard(0&) = 0 Then
  MsgBox "Could not open the Clipboard. Copy aborted."
  Exit Function
  End If
  
  'Clear the Clipboard.
  X = EmptyClipboard()
  
  'Copy the data to the Clipboard.
  hClipMemory = SetClipboardData(CF_TEXT, hGlobalMemory)
  
  OutOfHere2:
  If CloseClipboard() = 0 Then
  MsgBox "Could not close Clipboard."
  End If
  
  End Function
  
  Sub AddLinkToMessageInClipboard()
  
  Dim objMail As Outlook.MailItem
  
  'One and ONLY one message muse be selected
  If Application.ActiveExplorer.Selection.Count \<\> 1 Then
  MsgBox ("Select one and ONLY one message.")
  Exit Sub
  End If
  
  Set objMail = Application.ActiveExplorer.Selection.Item(1)
  'MsgBox ("\[\[outlook:" + objMail.EntryID + "\]\[MESSAGE: " + objMail.Subject + " (" + objMail.SenderName + ")\]\]")
  Dim txt As String
  txt = "\[\[outlook:" + objMail.EntryID + ""
  
  ClipBoard_SetData txt
  
  End Sub
- ## Registry
  [outlook.reg](outlook.reg)
  Windows Registry Editor Version 5.00
  
  \[HKEY_CLASSES_ROOT\outlook\]
  "URL Protocol"=""
  @="URL:Outlook Folders"
  
  \[HKEY_CLASSES_ROOT\outlook\DefaultIcon\]
  @="C:\\\Program Files (x86)\\\Microsoft Office\\\Office15\\\OUTLLIB.DLL,-9403"
  
  \[HKEY_CLASSES_ROOT\outlook\shell\]
  @="open"
  
  \[HKEY_CLASSES_ROOT\outlook\shell\open\]
  @=""
  
  \[HKEY_CLASSES_ROOT\outlook\shell\open\command\]
  @="\\"C:\\\Program Files (x86)\\\Microsoft Office\\\Office15\\\OUTLOOK.EXE\\" /select \\"%1\\""