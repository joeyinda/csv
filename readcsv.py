import csv

# Function to calculate the total sales for each product
def calculate_total_sales(data):
    total_sales = {}
    for row in data:
        product = row['Product']
        quantity = int(row['Quantity'])
        price = float(row['Price'])
        sales = quantity * price

        if product in total_sales:
            total_sales[product] += sales
        else:
            total_sales[product] = sales

    return total_sales

# Function to write the results to a CSV file
def write_results(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Total Sales'])

        for product, sales in results.items():
            writer.writerow([product, sales])

# Main function
def main():
    # Read data from the input CSV file
    with open('input.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Calculate total sales
    total_sales = calculate_total_sales(data)

    # Write results to the output CSV file
    write_results(total_sales, 'output.csv')

    print("Data processing complete. Results saved to output.csv.")

if __name__ == '__main__':
    main()
