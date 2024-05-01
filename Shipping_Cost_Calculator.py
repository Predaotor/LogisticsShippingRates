#Shipping Cost Calculator

## Input package weight and shipping rate
weight=float(input("Enter the package weight in kilograms: "))
rate=float(input("Enter the shipping rate per kilogram: "))

##Calculate the shipping cost
shipping_cost=weight*rate

##Display the result
pring(f"Shipping cos: {shipping_cost} USD")
