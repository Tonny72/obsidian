created:: [[2010-11-22]]
tags:: 800xA

Indien men een BoolIO heeft die wordt gebruikt als output, maar enkel gebruikt als bool

IF NOT *BoolIO*.Forced THEN
*BoolIO*.IOValue := *BoolIO*.Value
END_IF;

*bool* := *BoolIO*.IOValue;

Zie ook SibelcoCommonLib.ConvertBoolIO_DO_naar_bool

Experiment
Een BoolIO aangemaakt en nog niet gekoppeld aan hardware
=\> Status = `16#C0` (=Initial Value)
