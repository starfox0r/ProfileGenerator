import random
import string
import csv
from names import get_first_name, get_last_name

# Define a list of cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# Define a list of top 10 companies in the US
companies = ['3M', 'Abbott Laboratories', 'AbbVie', 'Abiomed', 'Accenture', 'Activision Blizzard', 'Adobe', 'Advanced Micro Devices', 'AES', 'Aflac', 'Agilent Technologies', 'Air Products & Chemicals', 'Akamai Technologies', 'Alaska Air Group', 'Albemarle', 'Alexandria Real Estate Equities', 'Align Technology', 'Allegion', 'Alliant Energy', 'Allstate', 'Alphabet (Class A)', 'Alphabet (Class C)', 'Altria Group', 'Amazon', 'Amcor', 'Ameren', 'American Airlines Group', 'American Electric Power', 'American Express', 'American International Group', 'American Tower', 'American Water Works', 'Ameriprise Financial', 'AmerisourceBergen', 'Amgen', 'Analog Devices', 'ANSYS', 'Anthem', 'Aon', 'APA Corporation', 'Apache', 'Apartment Investment & Management', 'Apple', 'Applied Materials', 'Aptiv', 'Archer-Daniels-Midland', 'Arconic', 'Arthur J. Gallagher', 'Assurant', 'AT&T', 'Atmos Energy', 'Autodesk', 'Automatic Data Processing', 'AutoZone', 'AvalonBay Communities', 'Avery Dennison', 'Baker Hughes', 'Ball', 'Bank of America', 'Baxter International', 'Becton Dickinson', 'Berkshire Hathaway', 'Best Buy', 'Biogen', 'BlackRock', 'Block (H&R)', 'Boeing', 'Booking Holdings', 'BorgWarner', 'Boston Properties', 'Boston Scientific', 'Bristol-Myers Squibb', 'Broadcom', 'Broadridge Financial Solutions', 'Brown-Forman', 'C. H. Robinson Worldwide', 'Celanese', 'CenterPoint Energy', 'Cerner', 'CF Industries Holdings', 'Charles Schwab', 'Charter Communications', 'Chesapeake Energy', 'Chevron', 'Chubb', 'Church & Dwight', 'Cigna', 'Cimarex Energy', 'Cincinnati Financial', 'Cintas', 'Cisco Systems', 'Citigroup', 'Citizens Financial Group', 'Citrix Systems', 'CME Group', 'CMS Energy', 'Coca-Cola', 'Cognizant Technology Solutions', 'Colgate-Palmolive', 'Comcast', 'Comerica', 'Conagra Brands', 'Concho Resources', 'ConocoPhillips', 'Consolidated Edison', 'Constellation Brands', 'Copart', 'Corning', 'Costco Wholesale', 'Coty', 'Crown Castle International', 'CSX', 'Cummins', 'CVS Health', 'D. R. Horton', 'Danaher', 'Darden Restaurants', 'DaVita', 'Deere', 'Delta Air Lines', 'Dentsply Sirona', 'Devon Energy', 'Diamondback Energy', 'Digital Realty Trust', 'Discover Financial Services', 'Discovery (Series A)', 'Discovery (Series C)', 'Dollar General', 'Dollar Tree', 'Dominion Energy', 'Domino\'s Pizza', 'Dover', 'Dow', 'DTE Energy', 'Duke Energy', 'DuPont de Nemours', 'DXC Technology', 'E*TRADE Financial', 'Eastman Chemical', 'Eaton', 'eBay', 'Edison International', 'Edwards Lifesciences', 'Electronic Arts']

# Open a CSV file for writing
with open('random_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name', 'Age', 'City', 'Postal Code', 'Salary', 'Company'])
    writer.writeheader()

    # Generate random data for 10 individuals and write to CSV file
    for i in range(100):
        # Generate random first and last names
        first_name = get_first_name()
        last_name = get_last_name()

        # Generate random age between 18 and 65
        age = random.randint(18, 65)

        # Generate random city and postal code
        city = random.choice(cities)
        postal_code = ''.join(random.choices(string.digits, k=5))

        # Generate random salary between $30,000 and $100,000
        salary = random.randint(30000, 100000)

        # Assign a random company from the top 10 companies list
        company = random.choice(companies)

        # Write the generated data to the CSV file
        writer.writerow({'First Name': first_name, 'Last Name': last_name, 'Age': age, 'City': city, 'Postal Code': postal_code, 'Salary': salary, 'Company': company})
