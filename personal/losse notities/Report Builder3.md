---
modified:  2025-07-21
date created: 2014-10-28T00:00:00+02:00
date modified: 2025-09-18T21:24:19+02:00
---
# Report Builder3

- # Repeat header rows on each page
  1.  Zet Grouping op Advances Mode
  2.  Zoek de 'Static' van de eerste kolom. Meestal de eerste.
  3.  Zet **RepeatOnNewPage** op true en **KeepWithGroup** op After
  ![image1](image1-1.png)
  
  <http://stackoverflow.com/questions/11285923/tablix-repeat-header-rows-on-each-page-not-working-report-builder-3-0>
  
  <table>
  <colgroup>
  <col style="width: 8%" />
  <col style="width: 91%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th></th>
  <th><p>It depends on the tablix structure you are using. In a table, for example, you do not have column groups, so Reporting Services does not recognize which textboxes are the column headers and setting RepeatColumnHeaders property to True doesn't work.</p>
  <p>Instead, you need to:</p>
  <ol type="1">
  <li><p>Open Advanced Mode in the Groupings pane. (Click the arrow to the right of the Column Groups and select Advanced Mode.)</p></li>
  <li><p>In the Row Groups area (not Column Groups), click on a Static group, which highlights the corresponding textbox in the tablix. Click through each Static group until it highlights the leftmost column header. This is generally the first Static group listed.</p></li>
  <li><p>In the Properties window, set the RepeatOnNewPage property to True.</p></li>
  <li><p>Make sure that the KeepWithGroup property is set to After.</p></li>
  </ol>
  <p>The KeepWithGroup property specifies which group to which the static member needs to stick. If set to After then the static member sticks with the group after it, or below it, acting as a group header. If set to Before, then the static member sticks with the group before, or above it, acting as a group footer. If set to None, Reporting Services decides where to put the static member.</p>
  <p>Now when you view the report, the column headers repeat on each page of the tablix.</p>
  <p><a href="http://youtube.com/watch?v=WAO819-gkKw">This</a> video shows how to set it exactly as the answer described.</p></th>
  </tr>
  </thead>
  <tbody>
  </tbody>
  </table>
  
  *From \<<http://stackoverflow.com/questions/11285923/tablix-repeat-header-rows-on-each-page-not-working-report-builder-3-0>\>*