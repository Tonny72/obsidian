---
tags: [application]
modified: 2025-09-18 12:01
date created: 2023-09-11T00:00:00+02:00
date modified: 2025-10-19T22:46:37+02:00
---
# Obsidian
## Shortcut keys

| key      | action                   |     |
| -------- | ------------------------ | --- |
| ctrl ;   | add properties to a page |     |
| ctrl p   | open command menu        |     |
| ctrl e   | toggle reading view      |     |
| Alt up   | move line up             |     |
| Alt down | move line down           |     |

## Log
[2024-07-23[../../journals/older/2024/07/2024-07-23]] #Obsidian

## Back-links using Influx plugin
[[2023-09-11]] Back-links in Influx do not work in pages.

## Change header
Look in deader.css file. No need to restart. Just save .css file 😀

## Full width notes
Settings - Editor - Display - Readable Line Length
### Show line numbers
Settings - Editor - Display - Show line numbers

## Simple task query
  ```
  tasks
  not done
  ```

## dataview examples
  ```
  dataview
  LIST
  FROM "journals"
  SORT file.name DESC
  ```

## Resize an image
  add a |*size* after the image name

## Image in a table
  add \\ before \|
  ```
  ![[assets/image6-2.png\|50]]
  ```

## Daily journal
Obsidian is niet echt geschikt voor daily journals.


## Show backlinks with query
  ```
  '''query
  tag:topic1
  '''
  ```

## Plugins
### Edit History
Do not use. Creates extra .edtz files in the same directory as the .md file.

### Importer
Used it to import [OneNote](applications/pkm/OneNote.md) notes. Worked like a charm.

### Obsidian MD for VSCode
zie 

![[dev/dev tools/VSCode/VSCode#Obsidian MD for VSCode|VSCode]]



## Summary

```
```add-summary
tags: #M3
```

## Query met #Obsidian
  ```query
  #Obsidian 
  ```

## Plugins
- [[applications/git/git]]
- Linter
