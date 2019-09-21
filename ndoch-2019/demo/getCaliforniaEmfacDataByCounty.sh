!/bin/bash

# This script will not work with the current curl request because you need cookie information in it.  In order to get it working you need to do the following.
# 1. Navigate to https://www.arb.ca.gov/emfac/2017/
# 2. Open chrome inspector
# 3. Click the download data button
# 4. Navigate to the network tab in the ispector tab
# 5. Right click csv.php on the left and select copy->copy as curl
# 6. Replace the curl and 'https://www.arb.ca.gov/emfac/2017/csv.php' portion of the curl request below, and then remove the --data and string after it in your pasted request

declare -a arr=('MONO' 'MONTEREY' 'NAPA' 'NEVADA' 'ORANGE' 'PLACER' 'PLUMAS' 'RIVERSIDE' 'SACRAMENTO' 'SAN BENITO' 'SAN BERNARDINO' 'SAN DIEGO' 'SAN FRANCISCO' 'SAN JOAQUIN' 'SAN LUIS OBISPO' 'SAN MATEO' 'SANTA BARBARA' 'SANTA CLARA' 'SANTA CRUZ' 'SHASTA' 'SIERRA' 'SISKIYOU' 'SOLANO' 'SONOMA' 'STANISLAUS' 'SUTTER' 'TEHAMA' 'TRINITY' 'TULARE' 'TUOLUMNE' 'VENTURA' 'YOLO' 'YUB')

for COUNTY in "${arr[@]}"
do

echo $COUNTY
curl 'https://www.arb.ca.gov/emfac/2017/csv.php' --data "data_type=emissions&geo_level=county&region=${COUNTY}&cal_year%5B%5D=2017&season=annual&veh_cat_type=emfac2011&veh_cat_option=all&model_year=all&speed=all&fuel=All&passcode=&cookie_token=1569101169691&verified=" --compressed | tail -n +10 >> emissions.csv

done
