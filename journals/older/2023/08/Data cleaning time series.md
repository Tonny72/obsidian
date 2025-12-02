---
date created: 2024-08-06 08:22
tags:
  - "#data-cleaning"
  - time-series
---

# python script en volledige output

[[script onderzoek data cleaning time series]]



# Find outliers op basis van max. rate

Deze tabel toont de rate (~het aantal kW) bij verschillende groupering periodes.
*Bij welke quantielen is de rate goed?*
=> Dit is eigenlijk niet te af te leiden.

**Voorbeeld**

<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (13, 5)</small><table border="1" class="dataframe"><thead><tr><th>statistic</th><th>AF11PM_energy_rate_1mo</th><th>AF11PM_energy_rate_5m</th><th>AF11PM_energy_rate_15m</th><th>AF11PM_energy_rate_1h</th></tr><tr><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>"count"</td><td>57.0</td><td>480833.0</td><td>161709.0</td><td>40440.0</td></tr><tr><td>"null_count"</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>"mean"</td><td>0.083344</td><td>0.084167</td><td>0.084101</td><td>0.084094</td></tr><tr><td>"std"</td><td>0.01817</td><td>0.023052</td><td>0.020802</td><td>0.019371</td></tr><tr><td>"min"</td><td>0.014366</td><td>-0.952148</td><td>-0.232422</td><td>0.0</td></tr><tr><td>"0.01%"</td><td>0.014366</td><td>0.0</td><td>0.0</td><td>0.00293</td></tr><tr><td>"0.1%"</td><td>0.014366</td><td>0.029297</td><td>0.033203</td><td>0.035156</td></tr><tr><td>"1%"</td><td>0.036743</td><td>0.046875</td><td>0.046875</td><td>0.049316</td></tr><tr><td>"99%"</td><td>0.116865</td><td>0.153809</td><td>0.144531</td><td>0.137939</td></tr><tr><td>"99.9%"</td><td>0.146394</td><td>0.246094</td><td>0.220703</td><td>0.203613</td></tr><tr><td>"99.99%"</td><td>0.146394</td><td>0.342773</td><td>0.332031</td><td>0.296875</td></tr><tr><td>"99.999%"</td><td>0.146394</td><td>0.908203</td><td>0.416016</td><td>0.333252</td></tr><tr><td>"max"</td><td>0.146394</td><td>2.185547</td><td>0.787109</td><td>0.333252</td></tr></tbody></table></div>

| statistic | AF11PM_energy_rate_1mo |
| --------- | ---------------------- |
|           |                        |

# Bij groepering van welke periode komen het minste afwijkingen voor

=> Als er wordt gegroepeerd op **1h** dan komen er er zo goed als geen afwijkingen voor.

## Deze tabel toont het verschil aan kWh per maand voor verschillende groeperings periodes.

<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (10, 8)</small><table border="1" class="dataframe"><thead><tr><th>datetime</th><th>HSK15_3_K2_6_PM_energy_1mo</th><th>HSK15_3_K2_6_PM_energy_5m</th><th>5m</th><th>HSK15_3_K2_6_PM_energy_15m</th><th>15m</th><th>HSK15_3_K2_6_PM_energy_1h</th><th>1h</th></tr><tr><td>datetime[ms]</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>2020-05-01 00:00:00</td><td>83630.0</td><td>83635.0</td><td>-5.0</td><td>83631.5</td><td>-1.5</td><td>83631.5</td><td>-1.5</td></tr><tr><td>2020-07-01 00:00:00</td><td>109883.5</td><td>110202.0</td><td>-318.5</td><td>109883.5</td><td>0.0</td><td>109883.5</td><td>0.0</td></tr><tr><td>2021-04-01 00:00:00</td><td>115734.0</td><td>115785.0</td><td>-51.0</td><td>115734.0</td><td>0.0</td><td>115734.0</td><td>0.0</td></tr><tr><td>2022-03-01 00:00:00</td><td>109230.0</td><td>109371.0</td><td>-141.0</td><td>109336.0</td><td>-106.0</td><td>109230.0</td><td>0.0</td></tr><tr><td>2022-04-01 00:00:00</td><td>90758.0</td><td>90813.0</td><td>-55.0</td><td>90813.0</td><td>-55.0</td><td>90758.0</td><td>0.0</td></tr><tr><td>2023-03-01 00:00:00</td><td>101506.0</td><td>101630.0</td><td>-124.0</td><td>101581.0</td><td>-75.0</td><td>101506.0</td><td>0.0</td></tr><tr><td>2023-04-01 00:00:00</td><td>96264.0</td><td>96266.0</td><td>-2.0</td><td>96266.0</td><td>-2.0</td><td>96266.0</td><td>-2.0</td></tr><tr><td>2024-03-01 00:00:00</td><td>96690.0</td><td>96844.0</td><td>-154.0</td><td>96816.0</td><td>-126.0</td><td>96690.0</td><td>0.0</td></tr><tr><td>2024-04-01 00:00:00</td><td>100922.0</td><td>100928.0</td><td>-6.0</td><td>100928.0</td><td>-6.0</td><td>100928.0</td><td>-6.0</td></tr><tr><td>2024-05-01 00:00:00</td><td>83178.0</td><td>83181.0</td><td>-3.0</td><td>83181.0</td><td>-3.0</td><td>83181.0</td><td>-3.0</td></tr></tbody></table></div>

# Conclusie

- Groepeer eerst per **1h** en werk vandaar verder om outliers te zoeken.
- Nadeel: er zijn 720 uren in een maand. Als er 1 uur niet klopt, verliest men veel info voor een correcte kWh berekening.