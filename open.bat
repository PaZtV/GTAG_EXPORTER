@echo off

:sleep

echo SCRIPT MADE BY PAZTV_ AT discord.gg/ZtGqq2wfFc
echo DO NOT USE THIS IF THE PLACE YOU WILL SHARE THIS HAS A 'PAID TIER'
echo IF YOU PUBLISH THIS IN ANY 'PAID' CHANNELS THEN I WILL TOUCH YOU
echo.
set /p choice=Do you understand? (y/n): 

if /i "%choice%"=="y" goto run
if /i "%choice%"=="n" goto wahwah

:wahwah
echo wah wah
start "" "https://c.tenor.com/-CfhczC_cREAAAAC/tenor.gif"
goto end

:run
start cmd /k py important\gtag_script.py
goto end

:end