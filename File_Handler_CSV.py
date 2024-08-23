import csv
class File_Handler_CSV():
    def __init__(self,file):
        self.file=file
        
    def load_product_data(self):
        try:
            with open(self.file, 'r') as f:
                reader = csv.DictReader(f)
                data=list(reader)
                print("Product Data Loaded Successfully:")
                return data
        except FileNotFoundError:
            print("Error: The file does not exist.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def save_product_data(self,data):
        try:
            with open(self.file, 'w',newline="") as f:
                fieldnames=["Product SKU","Product Name","Brand","Quantity"]
                writer=csv.DictWriter(f,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
                print("Product Data Saved Successfully.")
        except Exception as e:
            print(f"An unexpected error occurred while saving data: {e}")