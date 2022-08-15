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
