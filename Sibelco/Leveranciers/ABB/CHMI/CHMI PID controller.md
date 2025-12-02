created: [[2010-11-19]]T16:15:06.0000000+01:00


- ### HMI
  <table>
  <colgroup>
  <col style="width: 25%" />
  <col style="width: 15%" />
  <col style="width: 19%" />
  <col style="width: 39%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>HMI</strong></th>
  <th><strong>InteractionPar</strong></th>
  <th><strong>IN=Van HMI OUT=Naar HMI</strong></th>
  <th></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td><blockquote>
  <p><del>ACT_VALUE</del></p>
  </blockquote></td>
  <td></td>
  <td><p>OUT Actual value (feedback) of controller</p>
  <p></p></td>
  <td>Niet gebruikt</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>CAUTO</p>
  </blockquote></td>
  <td>AutoMode</td>
  <td>OUT Controller in Automatic</td>
  <td><blockquote>
  <p>HMI.CAUTO := InteractionPar.AutoMode</p>
  </blockquote>
  <ul>
  <li><p>Indien in ManMode zet 'OUT_PAR' op de uitgang via Track</p></li>
  </ul></td>
  </tr>
  <tr class="odd">
  <td>CI_CMDON</td>
  <td>-</td>
  <td>IN Command to switch to Automatic (internal set point)</td>
  <td>Zet 'InteractionPar.AutoMode' op True</td>
  </tr>
  <tr class="even">
  <td>CMDDW1</td>
  <td>-</td>
  <td>IN Command to decrease output by small step (1%)</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>CMDDW5</td>
  <td>-</td>
  <td>IN Command to decrease output by large step (5%)</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>CMDUP1</td>
  <td>-</td>
  <td>IN Command to increase output by small step (1%)</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>CMDUP5</td>
  <td>-</td>
  <td>IN Command to increase output by large step (5%)</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>CM_CMDON</td>
  <td>-</td>
  <td>IN Command to switch to manual</td>
  <td>Zet 'InteractionPar.AutoMode' op False</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>CX_CMDON</del></p>
  </blockquote></td>
  <td>-</td>
  <td>IN Command to switch to Automatic (external setpoint)</td>
  <td>Niet gebruikt</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>KP_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for proportional factor</td>
  <td>InteractionPar.Gain := HMI.KP_Par</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>OH_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for max. output limiter to Actuator</td>
  <td></td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>OL_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for min. output limiter to Actuator</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>OUT_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for Manual output from controller</td>
  <td></td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>OUT_VALUE</p>
  </blockquote></td>
  <td>PID.Out</td>
  <td>OUT Analoge output to actuator</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>PV_ERR</del></p>
  </blockquote></td>
  <td></td>
  <td>OUT Process Value</td>
  <td>Niet gebruikt</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>PV_H</del></p>
  </blockquote></td>
  <td></td>
  <td>OUT High alarm Process Value</td>
  <td>Niet gebruikt (eventueel koppelen aan 'PID.MaxOutR')</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>PV_L</del></p>
  </blockquote></td>
  <td></td>
  <td>OUT Low alarm Process Value</td>
  <td>Niet gebruikt (eventueel koppelen aan 'PID.MinOutR')</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>PV_VALUE</p>
  </blockquote></td>
  <td>Parameter.PV</td>
  <td>OUT Process value</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>SPIACT</p>
  </blockquote></td>
  <td>PID.SP</td>
  <td>OUT Controller in internal setpoint</td>
  <td></td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>SPI_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for internal setpoint</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>SPXACT</del></p>
  </blockquote></td>
  <td></td>
  <td>OUT Controller in external setpoint</td>
  <td>Extern setpunt niet gebruikt</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>SPX_VALUE</del></p>
  </blockquote></td>
  <td></td>
  <td>OUT External setpoint</td>
  <td>Extern setpunt niet gebruikt</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>TI_PAR</p>
  </blockquote></td>
  <td>-</td>
  <td>IN Parameter for integration time</td>
  <td></td>
  </tr>
  </tbody>
  </table>
- ### PID
  <table>
  <colgroup>
  <col style="width: 27%" />
  <col style="width: 20%" />
  <col style="width: 14%" />
  <col style="width: 38%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><blockquote>
  <p>Sp</p>
  </blockquote></th>
  <th>HMI.SPI_PAR</th>
  <th>in</th>
  <th>The Set point or reference value</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td><blockquote>
  <p>Pv</p>
  </blockquote></td>
  <td>Parameter.PV</td>
  <td>in</td>
  <td>The measured Process value</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>MaxPv</p>
  </blockquote></td>
  <td>Parameter.MaxPV</td>
  <td>In</td>
  <td>The high limit of the process value (100.0)</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>MinPv</p>
  </blockquote></td>
  <td>Parameter.MinPV</td>
  <td>in</td>
  <td>The low limit of the process value</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>Track</p>
  </blockquote></td>
  <td>Variable</td>
  <td>in</td>
  <td>Activation of tracking of an external signal</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>TrackVal</p>
  </blockquote></td>
  <td>Variable</td>
  <td>in</td>
  <td>The signal to follow when in tracking mode</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>MaxOut</p>
  </blockquote></td>
  <td>HMI.OH_PAR</td>
  <td>In</td>
  <td>The high limit of the output (100.0)</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>MinOut</p>
  </blockquote></td>
  <td>HMI.OL_PAR</td>
  <td>in</td>
  <td>The low limit of the output</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>InhInc</del></p>
  </blockquote></td>
  <td><em>Niet gebruikt</em></td>
  <td>in</td>
  <td>Inhibit the output to increase further</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>InhDec</del></p>
  </blockquote></td>
  <td></td>
  <td>in</td>
  <td>Inhibit the output to decrease further</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>ModifyInhLim</del></p>
  </blockquote></td>
  <td></td>
  <td>in</td>
  <td>If true, TrackVal will be used as limit when InhInc or InhDec is active (the output may increase/decrese but not above/below TrackVal)</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>Out</p>
  </blockquote></td>
  <td>IO.Out</td>
  <td>out</td>
  <td>The output from the controller</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>MaxOutR</del></p>
  </blockquote></td>
  <td>-</td>
  <td>out</td>
  <td>True when increase of the output is prevented, either by MaxOut or by InhInc</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>MinOutR</del></p>
  </blockquote></td>
  <td>-</td>
  <td>out</td>
  <td>True when decrease of the output is prevented, either by MinOut or by InhDec</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p><del>BackTrack</del></p>
  </blockquote></td>
  <td>-</td>
  <td>out</td>
  <td>True if the controller is put in manual mode</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p><del>BackTrackVal</del></p>
  </blockquote></td>
  <td>-</td>
  <td>out</td>
  <td>The value that can be used as track signal in previous FB's if the controller is in manual</td>
  </tr>
  </tbody>
  </table>
- ### InteractionPar
  <table>
  <colgroup>
  <col style="width: 27%" />
  <col style="width: 16%" />
  <col style="width: 23%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><del>PvUnit</del></th>
  <th></th>
  <th>coldretain</th>
  <th>Unit for Pv and Sp</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td><del>OutUnit</del></td>
  <td></td>
  <td>coldretain</td>
  <td>Unit for Out</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>AutoMode</p>
  </blockquote></td>
  <td></td>
  <td>retain</td>
  <td>Controller in auto (true) or manual (false) mode</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>OutManValue</p>
  </blockquote></td>
  <td>HMI.OUT_PAR</td>
  <td>coldretain nosort</td>
  <td>Manual output</td>
  </tr>
  <tr class="even">
  <td>Direct</td>
  <td>Bool</td>
  <td>coldretain</td>
  <td>True if to use negative gain</td>
  </tr>
  <tr class="odd">
  <td><blockquote>
  <p>Gain</p>
  </blockquote></td>
  <td>Real</td>
  <td>Coldretain</td>
  <td>Controller gain (1.0)</td>
  </tr>
  <tr class="even">
  <td><blockquote>
  <p>Ti</p>
  </blockquote></td>
  <td>HMI.TI_PAR</td>
  <td>Coldretain</td>
  <td>Integral time (seconds) (20.0s)</td>
  </tr>
  <tr class="odd">
  <td><del>Td</del></td>
  <td>Real</td>
  <td>coldretain</td>
  <td>Derivative time (seconds)</td>
  </tr>
  <tr class="even">
  <td>Offset</td>
  <td>Real</td>
  <td>Coldretain</td>
  <td>Offset used when no integral action is used (50)</td>
  </tr>
  <tr class="odd">
  <td>DerFilterTime</td>
  <td>Real</td>
  <td>Coldretain</td>
  <td>Time constant for derivative filter (1.0)</td>
  </tr>
  <tr class="even">
  <td>ControllerType</td>
  <td>Dint</td>
  <td>Coldretain</td>
  <td>The actual controller type. 1=P, 2=PI, 3=PD and 4=PID (2)</td>
  </tr>
  </tbody>
  </table>