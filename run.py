import requests;
import json;
def iplookup(ip_address):
    data_return = requests.get("http://ipapi.co/" + ip_address + "/json/",{});
    return json.loads(data_return.content);

print("""\033[1;32m\n _____          _  __    _____         __                 _             
/ _  / ___ _ __(_)/ _|   \_   \_ __   / /  ___   ___ __ _| |_ ___  _ __ 
\// / / _ \ '__| | |_     / /\/ '_ \ / /  / _ \ / __/ _` | __/ _ \| '__|
 / //\  __/ |  | |  _| /\/ /_ | |_) / /__| (_) | (_| (_| | || (_) | |   
/____/\___|_|  |_|_|   \____/ | .__/\____/\___/ \___\__,_|\__\___/|_|   
                              |_|                                       
                              
Version : 1.0
Github : @ivanwebdevs
""");
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"


def mulai(ip_addressnya):
    result_track = iplookup(str(ip_addressnya));
   
    if "error" in result_track:
        if result_track['reason'] == "RateLimited":
            print(f"{RED}Failed to check! Too many request! retrying...");
            mulai(ip_addressnya);
        else:
            print(f"{RED}{result_track['reason']}");
        

    else:
        print(f"""{PURPLE}IP ADDRESS : {YELLOW}{result_track['ip']}
{PURPLE}ASN : {YELLOW}{result_track['asn']}
{PURPLE}ORG : {YELLOW}{result_track['org']}
{PURPLE}NETWORK : {YELLOW}{result_track['network']}
{PURPLE}VERSION : {YELLOW}{result_track['version']}
{PURPLE}CITY : {YELLOW}{result_track['city']}
{PURPLE}REGION : {YELLOW}{result_track['region']}
{PURPLE}REGION CODE : {YELLOW}{result_track['region_code']}
{PURPLE}COUNTRY : {YELLOW}{result_track['country']}
{PURPLE}COUNTRY NAME : {YELLOW}{result_track['country_name']}
{PURPLE}Country Code ISO : {YELLOW}{result_track['country_code_iso3']}
{PURPLE}Country Capital : {YELLOW}{result_track['country_capital']}
{PURPLE}Country Tld : {YELLOW}{result_track['country_tld']}
{PURPLE}Continent code : {YELLOW}{result_track['continent_code']}
{PURPLE}Postal Code : {YELLOW}{result_track['postal']}
{PURPLE}Latitude : {YELLOW}{result_track['latitude']}
{PURPLE}Longitude : {YELLOW}{result_track['longitude']}
{PURPLE}Timezone : {YELLOW}{result_track['timezone']}
{PURPLE}UTC : {YELLOW}{result_track['utc_offset']}
{PURPLE}Calling code : {YELLOW}{result_track['country_calling_code']}
{PURPLE}Currency : {YELLOW}{result_track['currency']}
{PURPLE}Currency Name : {YELLOW}{result_track['currency_name']}
{PURPLE}Languages : {YELLOW}{result_track['languages']}
{PURPLE}Country Area : {YELLOW}{result_track['country_area']}
{PURPLE}Country Population : {YELLOW}{result_track['country_population']}
""");
    start();
def start():
    print(LIGHT_GREEN);
    ip_addressnya = input("IP ADDRESS : ")
    mulai(ip_addressnya);
    

start();
