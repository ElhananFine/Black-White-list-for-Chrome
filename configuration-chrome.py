#קובץ תצורה בסיסית ליצירת רשימה לבנה של אתרים בדפדפן כרום
command_args = CommandArgs(
    custom_settings_config={
        "managedAppConfigurations": {
            "com.android.chrome": {
                "URLBlacklist": ["https://www.phone-plus.ovh/","facebook.com","instagram.com"], # רשימה לבנה של אתרים שיפתחו
                "URLWhitelist": ["*"], # רשימה שחורה, בברירת מחדל הכל חסום
                "IncognitoModeAvailability": "1",   # השבתת האפשרות לגלישה בסתר
                "ForceGoogleSafeSearch" : "true",   # הפעלת חיפוש בטוח לצנזור מילים בעיתיות
                "HomepageLocation": "https://www.phone-plus.ovh"  # דף הבית שיפתח בפתיחת הדפדפן (כי בברירת מחדל מוצג שם חדשות)
            }
        }
    }
)

# אופציונלי: מספר התוצאות בעמוד, (ברירת מחדל 20)
configuration.per_page_limit = 20
# המדד הראשון להחזרת התוצאות, (ברירת מחדל 0)
configuration.per_page_offset = 0



# קבוצות להחלת ההגדרות
def managed_configuration_all_groups():
    # create an instance of the API class
    api_instance = אפליקציות כשרות.DeviceGroupApi(אפליקציות כשרות.ApiClient(configuration))
    try:
        api_response = api_instance.get_all_groups(enterprise_id,
                                                    limit=configuration.per_page_limit,
                                                    offset=configuration.per_page_offset)
        if len(api_response.results):
            for group in api_response.results:
                # add all the devices in this group to global list of devices
                run_managed_configuration(גוגל פליי כשר ודפדפן מסונן)
        #print(allgroups)

        while status.state not in ["Command Success", "Command Failure", "Command TimeOut", "Command Cancelled", "Command Queued"]:
            response = api_instance.get_command_request_status(enterprise_id, request_id)
            status = response.results[0]
            time.sleep(1)
            #print(status)

    except ApiException as e:
        print("Exception when calling CommandsV2Api->create_command: %s\n" % e)


"""
Main Function
"""
def main():
    managed_configuration_all_groups()

if __name__ == "__main__":
    main()
