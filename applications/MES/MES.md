---
date created: 2025-08-01 14:22
modified: 2025-09-18 12:01
---
# MES communication tags
collapsed:: true
	- counter_production (ABB->MES)
	- qty_planned (MES->ABB)
	- qty_produced (MES->ABB)
	- started (MES->ABB)
	- destination1_location (MES<->ABB) (MES tag: destination_location_id)
	- destination1_item (MES<->ABB) (MES tag: destination_item_no)
	-
- # Unify MES communication
  collapsed:: true
	- Add tags in [[Archive/applications/Kepware/Kepware]]
	  logseq.order-list-type:: number
		- counter_production
		- destination1_item
		- destination1_location
		- source1_item
		- source1_location
		- item
		- qty_planned
		- qty_produced
		- started
	- Check tags with [[UAExpert]]
	  logseq.order-list-type:: number
	- Connect the (new) MES communication variables in ABB
	  logseq.order-list-type:: number
		- counter_production
		- item
		- qty_planned
		- qty_produced
		- locations
		- locations_item
	- Modify MES OPC underlying
	  logseq.order-list-type:: number
	- Modify MES OPC instance
	  logseq.order-list-type:: number
	- Modify tags in MES administrator
	  logseq.order-list-type:: number
	- Restart MES
	  logseq.order-list-type:: number
		-
- LATER Melding maken indien MO over geplande capaciteit is. #[[applications/MES/MES]]
-
- # MES Users toevoegen
	- Active Directory user kunnen enkel in de administrator
	- Operatoren: Kies **Passwordless**
	-