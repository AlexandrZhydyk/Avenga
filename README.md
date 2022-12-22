# Avenga Internship task

Task:

Here is a dataset: "https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc?resource=download". 
Using Apache Spark (Scala or Python), get the following report:
|-- Vendor: string (nullable = true) - name of vendor
|-- Payment Type: string (nullable = true) - name of payment type
|-- Payment Rate: double (nullable = true) - payment_total / passengers count per vendor and payment type
|-- Next Payment Rate: double (nullable = true) - next record(bigger) payment rate for vendor
|-- Max Payment Rate: double (nullable = true) - max payment rate for vendor
|-- Percents to next rate: string (nullable = true) - how many points (in percents) is necessary to achieve the next record payment rate

Explanation:
1) Rename data in columns VendorID and payment_type.
2) Creating a table with payment_rate per vendor and payment type,
 excluding unknown vendor and not respective data as null or month that isn't July.
3) Creating a table with avg payment_rate per day for vendor.
4) Calculate growth rate of payment_rate per day: growth rate =
 = (payment_rate today - payment_rate yesterday)/payment_rate yesterday.
5) Calculate avg growth rate per day and multiply it by 30 days in month to find
 month grow in percent (percents_to_next_rate column).
6) Creating a table with avg payment_rate per vendor per month and max_payment_rate.
7) Adding and editing data to the resulting table.

