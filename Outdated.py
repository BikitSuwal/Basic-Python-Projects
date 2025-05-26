month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

def main():
    while True:
        try:
            date = input("Date: ").capitalize().strip()
            if '/' in date:
                MM,DD,YYYY = date.split('/')
                DD = MM.zfill(2)
                DD = DD.zfill(2)
                print(f"{YYYY}-{MM}-{DD}")
            
            elif ',' in date:
                m_name,rest = date.split(' ', 1)
                DD,YYYY = rest.split(',')
                MM = str(month.index(m_name) + 1).zfill(2)
                DD = DD.zfill(2)
                print(f"{YYYY}-{MM}-{DD}")
            
            else:
                print("Invalid date format. Please use MM/DD/YYYY or Month DD, YYYY.")
        except (ValueError,IndexError):
            print("Invalid date format. Please use MM/DD/YYYY or Month DD, YYYY.")

if __name__ == "__main__":
    main()